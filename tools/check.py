#!/usr/bin/env python3
"""check: config-driven prose lint and facts verification for engagement artefacts.

WHY THE SELF-TEST EXISTS, AND WHY YOU CAN TRUST THIS MORE THAN A HOME-MADE CHECKER
----------------------------------------------------------------------------------
A predecessor checker printed "[OK]" for weeks while comparing nothing at all: its
regex assumed a layout that did not exist, every lookup fell through, and it reported
a pass having tested zero things. A checker that cannot fail is worse than no checker,
because it launders a guess into a claim. (When a skill gives confidently wrong
answers, the root cause is usually the home-made checker.)

So every rule carries two fixtures:

    poison  - a string the rule MUST flag. Catches a rule that matches nothing.
    clean   - a string the rule MUST NOT flag. Catches a rule that matches everything.

Grading only happens once every rule has proved it can both fire and stay silent.
Budget checks (sentence length, hinge colons, semicolons, repeated openers) carry
fixtures too, run through the same gate.

WHAT THIS DOES AND DOES NOT COVER
---------------------------------
Deterministic half only: the ban list, style budgets, directive names, and the
facts-manifest check. The judgement half (conclusion-first sections, findings carrying
implication and recommendation, balance, register) cannot be done by regex: run
rubric.md through a model in a fresh session that did not write the draft.

Layout QA is real and mostly human: `--layout report.pdf` runs the two cheap checks
(orphaned headings, dangling lead-ins at page ends) but eyeballing rendered pages
end to end is still required before publishing. Budgets are the floor, not the review.

Usage:
    ./check.py --self-test                     prove the rules work, grade nothing
    ./check.py draft.md                        self-test, then grade
    ./check.py draft.md --config check.config.json --facts facts.json
    ./check.py --layout report.pdf             page-end layout checks (needs pdftotext)
"""
from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import pathlib
from dataclasses import dataclass

FAIL, WARN = "FAIL", "WARN"
HERE = pathlib.Path(__file__).parent


@dataclass
class Rule:
    id: str
    why: str
    pattern: str
    poison: str                      # must match
    clean: str                       # must not match
    severity: str = FAIL
    flags: int = re.I
    limit: int = 0                   # allowed occurrences before it counts
    exempt_fenced: bool = True


def load_config(path: pathlib.Path) -> dict:
    cfg = json.loads(path.read_text(encoding="utf-8"))
    return cfg


def build_rules(cfg: dict) -> list[Rule]:
    rules = []
    for r in cfg["rules"]:
        flags = re.I
        if r.get("multiline"):
            flags |= re.M
        rules.append(Rule(r["id"], r["why"], r["pattern"], r["poison"], r["clean"],
                          r.get("severity", FAIL), flags, r.get("limit", 0),
                          r.get("exempt_fenced", True)))
    # Engagement names list -> one generated roles-not-names rule.
    names = [n for n in cfg.get("names", []) if n.strip()]
    if names:
        pat = r"\b(" + "|".join(re.escape(n.lower()) for n in names) + r")\b"
        rules.append(Rule("real-names", "People appear as role tokens, never by name",
                          pat, f"{names[0]} raised the cost question.",
                          "The CEO raised the cost question."))
    # Guarded figure pairs -> numbers that must never merge into one figure claim.
    # Fire only when the two numbers share one claim: no clause boundary and no
    # repeated unit noun between them.
    for a, b in cfg.get("guarded_pairs", []):
        pat = (rf"\b{a}\b(?:(?![.;])(?!sources?)[^\n]){{0,60}}\b{b}\b"
               rf"|\b{b}\b(?:(?![.;])(?!sources?)[^\n]){{0,60}}\b{a}\b")
        rules.append(Rule(f"merged-{a}-{b}",
                          f"{a} and {b} must never be merged into one evidence figure",
                          pat,
                          f"Built from {a} and {b} sources across the engagement.",
                          f"The foundations analysis draws on {a} sources; the "
                          f"opportunity analysis draws on {b}."))
    return rules


# ---------------------------------------------------------------------------
def strip_fenced(text: str) -> str:
    """Blank out fenced code blocks and HTML comments, preserving line numbers."""
    text = re.sub(r"<!--.*?-->", lambda m: re.sub(r"[^\n]", "", m.group(0)), text,
                  flags=re.S)
    out, fenced = [], False
    for line in text.split("\n"):
        if line.lstrip().startswith("```"):
            fenced = not fenced
            out.append("")
            continue
        out.append("" if fenced else line)
    return "\n".join(out)


def hits(rule: Rule, text: str) -> list[tuple[int, str]]:
    body = strip_fenced(text) if rule.exempt_fenced else text
    found = []
    for m in re.finditer(rule.pattern, body, rule.flags):
        line = body[: m.start()].count("\n") + 1
        frag = body.split("\n")[line - 1].strip()
        found.append((line, frag[:100]))
    return found


# ---------------------------------------------------------------------------
# Prose budgets. Sentence tokenisation is approximate and says so; headings, list
# items, table rows and directive lines are excluded before anything is counted.
# ---------------------------------------------------------------------------
def prose_paragraphs(text: str) -> list[str]:
    """Prose paragraphs only: headings, tables, lists (with their continuation
    lines), quotes, directives and diagram placeholders are excluded whole. A
    paragraph opening with a bold lead-in (**Like this.**) is prose and stays."""
    out = []
    for raw in re.split(r"\n\s*\n", strip_fenced(text)):
        lines = [l for l in raw.split("\n") if l.strip()]
        if not lines:
            continue
        first = lines[0].lstrip()
        if first.startswith(("#", "|", "- ", "* ", ">", "[", "!", "*[")):
            continue
        if re.match(r"^\d+\.\s", first):
            continue
        out.append(" ".join(l.strip() for l in lines))
    return out


def prose_sentences(text: str) -> list[str]:
    blob = " ".join(prose_paragraphs(text))
    blob = re.sub(r"[*_`]", "", blob)          # emphasis markers block the splitter
    blob = re.sub(r"\b(e\.g|i\.e|etc|vs|approx|no)\.", r"\1", blob)  # guard splits
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9\"'(])", blob)
    return [p.strip() for p in parts if len(p.split()) >= 3]


def budget_report(text: str, budgets: dict) -> list[tuple[str, str, str]]:
    """Returns (severity, id, message) rows. Empty list means all budgets pass."""
    out = []
    sents = prose_sentences(text)
    if not sents:
        return out
    lengths = [len(s.split()) for s in sents]
    mean = sum(lengths) / len(lengths)
    over = [(s, n) for s, n in zip(sents, lengths) if n > budgets["sentence_hard_max"]]
    if mean > budgets["sentence_mean_max"]:
        out.append((FAIL, "sentence-mean",
                    f"mean sentence length {mean:.1f} words "
                    f"(cap {budgets['sentence_mean_max']})"))
    for s, n in over[:5]:
        out.append((FAIL, "sentence-tail",
                    f"{n}-word sentence (cap {budgets['sentence_hard_max']}): "
                    f"{s[:80]}..."))
    if len(over) > 5:
        out.append((FAIL, "sentence-tail", f"... and {len(over) - 5} more over the cap"))

    # Hinge colons: mid-sentence colon where a clause follows. Exclusions per the
    # tone rules: list introducers (colon ends the line), labels and lead-ins
    # (three or fewer words before the colon), and short tails that are noun
    # phrases rather than clauses (fewer than five words after).
    hinges = 0
    for s in sents:
        m = re.search(r"^(.*?):\s+(.+)$", s)
        if not m:
            continue
        before, after = m.group(1), m.group(2)
        if len(before.split()) <= 3 or len(after.split()) < 5:
            continue
        hinges += 1
    hinge_pct = 100.0 * hinges / len(sents)
    semis = sum(1 for s in sents if ";" in s)
    semi_pct = 100.0 * semis / len(sents)
    # Short documents round down to zero: under ten sentences, one is already over.
    if len(sents) < 10:
        if hinges:
            out.append((FAIL, "hinge-colons",
                        f"{hinges} hinge colon(s) in a {len(sents)}-sentence piece; "
                        "short documents get zero"))
        if semis:
            out.append((FAIL, "semicolons",
                        f"{semis} semicolon sentence(s) in a {len(sents)}-sentence "
                        "piece; short documents get zero"))
    else:
        if hinge_pct > budgets["hinge_colon_pct_max"]:
            out.append((FAIL, "hinge-colons",
                        f"hinge colons in {hinge_pct:.0f}% of sentences "
                        f"(cap {budgets['hinge_colon_pct_max']}%)"))
        if semi_pct > budgets["semicolon_pct_max"]:
            out.append((FAIL, "semicolons",
                        f"semicolons in {semi_pct:.0f}% of sentences "
                        f"(cap {budgets['semicolon_pct_max']}%)"))

    # Repeated home-grown opening formulae: the first word of each prose paragraph,
    # counted as a shape, with ordinary determiners and connectives excluded so only
    # a coined formula ("One [noun] ...") registers. Any shape past the budget is a
    # tell.
    stop = {"the", "a", "an", "this", "that", "these", "those", "it", "in", "on",
            "for", "with", "and", "but", "as", "at", "to", "if", "when", "where"}
    paras = prose_paragraphs(text)
    shapes: dict[str, int] = {}
    for p in paras:
        words = re.findall(r"[A-Za-z']+", p)
        if words and words[0].lower() not in stop:
            key = words[0].lower()
            shapes[key] = shapes.get(key, 0) + 1
    for key, n in sorted(shapes.items(), key=lambda kv: -kv[1]):
        if n > budgets["repeated_opener_max"]:
            out.append((WARN, "repeated-opener",
                        f'paragraph opener "{key} ..." used {n} times '
                        f"(budget {budgets['repeated_opener_max']})"))
    return out


BUDGET_FIXTURES = {
    # id -> (poison text that must produce at least one row with that id,
    #        clean text that must produce none)
    "sentence-tail": (
        "This single sentence has been deliberately padded with clause after clause "
        "so that it runs far beyond the forty word hard cap that the budget enforces "
        "for every single sentence in every single artefact that the whole kit ever "
        "produces anywhere at all in any engagement today. "
        "It keeps going with more words still. A short one follows. And another one "
        "here. Plus one more short sentence now. Then another short line. And a final "
        "short sentence to finish the piece off cleanly today.",
        "Each sentence here is short. The budget passes easily. Nothing runs long. "
        "The checker stays quiet. All is well. Nothing to see. Short and plain. "
        "Still short here. Nearly done now. This is the end."),
    "hinge-colons": (
        "Coverage is the weak point: no gate exists and nothing blocks a regression.",
        "The gaps are:\n\n- one\n- two\n\nCoverage sits at 31%. Nothing gates it."),
    "semicolons": (
        "The team is small; the backlog is long and nothing moves this quarter.",
        "The team is small. The backlog is long. Nothing moves this quarter."),
    "repeated-opener": (
        "One team builds alone. More words follow here today.\n\n"
        "One tool does the join. More words follow here today.\n\n"
        "One owner takes it on. More words follow here today.\n\n",
        "The team builds alone. More words follow here today.\n\n"
        "A tool does the join. More words follow here today.\n\n"
        "One owner takes it on. More words follow here today.\n\n"),
}


# ---------------------------------------------------------------------------
def known_figures(facts_path: pathlib.Path | None) -> set[str]:
    """Every number the artefact is entitled to use, read from the facts manifest,
    never typed. A figure absent from the manifest is not necessarily wrong, but it
    is not traceable and needs a human to confirm it."""
    if not facts_path or not facts_path.exists():
        return set()
    data = json.loads(facts_path.read_text(encoding="utf-8"))
    fig: set[str] = set()
    def walk(v):
        if isinstance(v, dict):
            for x in v.values():
                walk(x)
        elif isinstance(v, list):
            for x in v:
                walk(x)
        elif isinstance(v, (int, float)):
            fig.add(str(v))
            fig.add(f"{float(v):.1f}")
        elif isinstance(v, str) and re.fullmatch(r"\d+(\.\d+)?%?", v):
            fig.add(v.rstrip("%"))
    walk(data)
    return fig


def check_figures(text: str, facts_path: pathlib.Path | None,
                  freebies: dict) -> list[str]:
    known = known_figures(facts_path)
    if not known:
        return ["figures: SKIPPED, no facts manifest supplied or readable "
                "(pass --facts facts.json)"]
    # Heading lines are structure, not figure claims (section numbers like 3.1).
    body = "\n".join("" if l.lstrip().startswith("#") else l
                     for l in strip_fenced(text).split("\n"))
    out = []
    for m in re.finditer(r"(?<![\w.])(\d+(?:\.\d+)?)%?(?![\w])", body):
        n = m.group(1)
        if (n in known or float(n) <= freebies.get("max_small", 3)
                or freebies.get("year_min", 2000) <= float(n)
                <= freebies.get("year_max", 2100)):
            continue
        line = body[: m.start()].count("\n") + 1
        out.append(f"line {line}: {n} is not derivable from the facts manifest, "
                   "confirm by hand")
    return out


def check_directives(text: str, valid: set[str]) -> list[str]:
    out = []
    for m in re.finditer(r"^\[(!?[a-z/-]+)(?::|\])", strip_fenced(text), re.M | re.I):
        d = m.group(1).lower()
        if d not in valid:
            line = text[: m.start()].count("\n") + 1
            out.append(f"line {line}: [{d}] is not a supported publishing directive")
    return out


# ---------------------------------------------------------------------------
# Observations mode: mechanical verification of extraction outputs. Needs no ground
# truth: it checks that every quote exists verbatim in its cited source, that
# locators name real files, that no registry name reaches a claim, that the schema
# shape holds, and (where speaker labels are configured) that no quote is drawn
# from a consultant turn. Deterministic checks first; the judgement of WHICH
# observations to extract stays with a comparison against a trusted reference and the human gate.
# ---------------------------------------------------------------------------
VALID_CONFIDENCE = {"high", "medium", "low"}
VALID_SUBTYPES = {"discovery interview", "consultant-led session",
                  "client-shared summary", "document"}
REFUSED_SUBTYPES = {"consultant recollection"}
VALID_SCALE_KEYS = {"cadence", "load", "held_by"}


def nearest_label(text: str, pos: int, labels: list[str]) -> tuple[int, str]:
    """Index and value of the label occurring latest at or before pos."""
    best, best_lab = -1, ""
    for lab in labels:
        i = text.rfind(lab, 0, pos)
        if i > best:
            best, best_lab = i, lab
    return best, best_lab


def check_observation_file(path: pathlib.Path, sources_dir: pathlib.Path,
                           cfg: dict) -> tuple[list[str], list[str]]:
    """Returns (fails, warns) for one observations JSON file."""
    fails, warns = [], []
    ocfg = cfg.get("observation_checks", {})
    names = [n for n in cfg.get("names", []) if n.strip()]
    name_pat = (re.compile(r"\b(" + "|".join(re.escape(n) for n in names) + r")\b",
                           re.I) if names else None)
    try:
        d = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:                                       # noqa: BLE001
        return [f"{path.name}: unreadable JSON ({exc.__class__.__name__})"], []
    for key in ("source", "sub_type", "observations"):
        if key not in d:
            fails.append(f"{path.name}: missing top-level '{key}'")
    if fails:
        return fails, warns
    if d["sub_type"] in REFUSED_SUBTYPES:
        fails.append(f"{path.name}: sub_type '{d['sub_type']}' is refused as "
                     "evidence and must not have an observations file")
    elif d["sub_type"] not in VALID_SUBTYPES:
        fails.append(f"{path.name}: unknown sub_type '{d['sub_type']}'")
    src_path = sources_dir / d["source"]
    src_text = ""
    if not src_path.exists():
        fails.append(f"{path.name}: source '{d['source']}' not found in "
                     f"{sources_dir}")
    else:
        src_text = src_path.read_text(encoding="utf-8", errors="replace")
    c_labels = ocfg.get("consultant_labels", [])
    k_labels = ocfg.get("client_labels", [])
    seen_ids: set[str] = set()
    for o in d["observations"]:
        oid = o.get("id", "<no id>")
        where = f"{path.name}:{oid}"
        if oid in seen_ids:
            fails.append(f"{where}: duplicate observation id")
        seen_ids.add(oid)
        for key in ("id", "claim", "locator", "confidence"):
            if not o.get(key):
                fails.append(f"{where}: missing '{key}'")
        if o.get("confidence") and o["confidence"] not in VALID_CONFIDENCE:
            fails.append(f"{where}: confidence '{o['confidence']}' not in "
                         f"{sorted(VALID_CONFIDENCE)}")
        loc = o.get("locator", "")
        if loc and not loc.startswith(d["source"] + ","):
            fails.append(f"{where}: locator must start with the source file name "
                         f"exactly ('{d['source']}, ...'), got '{loc[:60]}'")
        if "scale" in o:
            bad = set(o["scale"]) - VALID_SCALE_KEYS
            if bad:
                fails.append(f"{where}: unknown scale key(s) {sorted(bad)}")
        quote = o.get("quote")
        if not quote:
            warns.append(f"{where}: no quote (allowed where none is available, "
                         "but verify the claim by hand)")
        elif src_text:
            # Verbatim modulo line-wrapping: hard-wrapped sources put newlines
            # inside sentences, so both sides collapse whitespace runs before
            # matching. The words must match exactly.
            norm_src = re.sub(r"\s+", " ", src_text)
            norm_quote = re.sub(r"\s+", " ", quote).strip()
            i = norm_src.find(norm_quote)
            if i < 0:
                fails.append(f"{where}: quote not found verbatim in "
                             f"{d['source']}: \"{quote[:70]}...\"")
            elif (c_labels and k_labels
                  and d["sub_type"] in ("discovery interview",
                                        "consultant-led session")):
                # The consultant-turn check applies to speaker-labelled
                # conversations only, and an observation marked relay:true is
                # the second-hand relay exception: legitimately quoted from a
                # consultant turn, carried as weaker, indirect evidence.
                li, lab = nearest_label(norm_src, i, c_labels + k_labels)
                if li >= 0 and lab in c_labels:
                    if o.get("relay") is True:
                        warns.append(f"{where}: relay observation quotes a "
                                     "consultant turn (allowed; confirm it is "
                                     "genuinely indirect client evidence)")
                    else:
                        fails.append(f"{where}: quote sits in a consultant turn "
                                     f"('{lab.strip()}'); consultant speech is "
                                     "framing, never evidence (mark relay: true "
                                     "if this is the second-hand relay "
                                     "exception)")
        if name_pat:
            for field in ("claim", "stated_dependencies"):
                v = o.get(field)
                if v and (m := name_pat.search(str(v))):
                    fails.append(f"{where}: registry name '{m.group(0)}' in "
                                 f"'{field}'")
            for v in (o.get("scale") or {}).values():
                if (m := name_pat.search(str(v))):
                    fails.append(f"{where}: registry name '{m.group(0)}' in "
                                 "scale")
            if quote and (m := name_pat.search(quote)):
                warns.append(f"{where}: registry name '{m.group(0)}' inside a "
                             "verbatim quote (source leak; observations never "
                             "ship, but note it)")
    return fails, warns


def obs_self_test(cfg: dict) -> bool:
    """Poison/clean fixture pair for the observations checks, same trust rule as
    the prose rules: refuse to grade until the checks prove they can fire and
    stay silent."""
    import tempfile
    ocfg = {"consultant_labels": ["CONS:"], "client_labels": ["CLI:"]}
    test_cfg = {"names": ["Testa Person"], "observation_checks": ocfg}
    src = ("---\nparticipants: x\n---\n"
           "CONS: How long does that take you? "
           "CLI: It takes a day and a half every week. "
           "CONS: I bet the real number is higher. "
           "CLI: Testa Person runs it by hand.")
    poison = {"source": "s.md", "sub_type": "discovery interview", "observations": [
        {"id": "P1", "claim": "x", "quote": "not in the source at all",
         "locator": "s.md, CLI", "confidence": "medium"},
        {"id": "P2", "claim": "x", "quote": "I bet the real number is higher.",
         "locator": "s.md, CONS", "confidence": "medium"},
        {"id": "P3", "claim": "Testa Person runs it", "quote":
         "It takes a day and a half every week.", "locator": "s.md, CLI",
         "confidence": "certain"},
        {"id": "P4", "claim": "x", "quote": "It takes a day and a half every week.",
         "locator": "wrong.md, CLI", "confidence": "low"}]}
    clean = {"source": "s.md", "sub_type": "discovery interview", "observations": [
        {"id": "C1", "claim": "the task takes a day and a half weekly (self "
         "reported)", "quote": "It takes a day and a half every week.",
         "locator": "s.md, CLI", "confidence": "low",
         "scale": {"cadence": "weekly"}},
        {"id": "C2", "claim": "relayed by the consultant (indirect): a belief "
         "the number runs higher", "quote":
         "I bet the real number is higher.", "locator": "s.md, CONS",
         "confidence": "low", "relay": True}]}
    ok = True
    with tempfile.TemporaryDirectory() as td:
        tdp = pathlib.Path(td)
        (tdp / "s.md").write_text(src)
        for label, payload, expect_fail in (("poison", poison, True),
                                            ("clean", clean, False)):
            f = tdp / f"obs-{label}.json"
            f.write_text(json.dumps(payload))
            fails, _ = check_observation_file(f, tdp, test_cfg)
            fired = bool(fails)
            good = fired == expect_fail
            ok = ok and good
            note = ""
            if not good and expect_fail:
                note = "  <-- did not fire on poison (check is dead)"
            if not good and not expect_fail:
                note = "  <-- fired on clean file: " + "; ".join(fails[:2])
            print(f"  [{'ok  ' if good else 'BAD '}] obs-{label:18} "
                  f"fails={len(fails):<3}{note}")
        if ok:
            # Each poison observation must trip at least one distinct failure.
            fails, _ = check_observation_file(tdp / "obs-poison.json", tdp,
                                              test_cfg)
            for oid in ("P1", "P2", "P3", "P4"):
                if not any(f":{oid}:" in x or f"{oid}:" in x for x in fails):
                    print(f"  [BAD ] obs poison case {oid} not caught")
                    ok = False
    return ok


def check_observations(workspace: pathlib.Path, cfg: dict,
                       sources_dir: pathlib.Path | None) -> int:
    print("OBSERVATIONS SELF-TEST\n")
    if not obs_self_test(cfg):
        print("\nREFUSED: observation checks failed their own fixtures.")
        return 2
    print()
    src_dir = sources_dir or (workspace / "sources")
    files = sorted((workspace / "observations").glob("obs-*.json"))
    if not files:
        print(f"No observation files under {workspace / 'observations'}")
        return 2
    ocfg = cfg.get("observation_checks", {})
    if not (ocfg.get("consultant_labels") and ocfg.get("client_labels")):
        print("  note: consultant/client labels not configured; the "
              "consultant-turn check is OFF for this run\n")
    total_f = total_w = n_obs = 0
    for f in files:
        fails, warns = check_observation_file(f, src_dir, cfg)
        try:
            n_obs += len(json.loads(f.read_text())["observations"])
        except Exception:                                          # noqa: BLE001
            pass
        status = "FAIL" if fails else ("warn" if warns else "pass")
        print(f"  [{status:4}] {f.name}: {len(fails)} fail, {len(warns)} warn")
        for x in fails[:8]:
            print(f"           {x}")
        if len(fails) > 8:
            print(f"           ... and {len(fails) - 8} more")
        for x in warns[:4]:
            print(f"           (warn) {x}")
        total_f += len(fails)
        total_w += len(warns)
    print(f"\n{len(files)} files, {n_obs} observations: {total_f} failure(s), "
          f"{total_w} warning(s). "
          f"{'OBSERVATIONS FAIL' if total_f else 'Mechanical checks pass'}. "
          "What these checks cannot judge: whether the RIGHT observations were "
          "extracted; that is the comparison's and the human gate's job.")
    return 1 if total_f else 0


# ---------------------------------------------------------------------------
def check_layout(pdf: pathlib.Path) -> int:
    """Page-end checks on a rendered PDF: orphaned headings and dangling lead-ins.
    Needs pdftotext. This is the cheap floor; eyeball the rendered pages too."""
    if not shutil.which("pdftotext"):
        print("layout: SKIPPED, pdftotext not on PATH")
        return 0
    raw = subprocess.run(["pdftotext", "-layout", str(pdf), "-"],
                         capture_output=True, text=True, check=True).stdout
    pages = raw.split("\f")
    problems = 0
    for i, page in enumerate(pages[:-1], 1):
        lines = [l.strip() for l in page.rstrip().split("\n") if l.strip()]
        if not lines:
            continue
        last = lines[-1]
        # A short line with no terminal punctuation at a page end is an orphaned
        # heading or a lead-in; both are the layout bugs that recur.
        if len(last.split()) <= 8 and not re.search(r"[.!?)\]]$", last):
            print(f"  [WARN] page {i} ends with a possible orphaned heading or "
                  f"lead-in: {last[:80]!r}")
            problems += 1
        if last.endswith(":"):
            print(f"  [WARN] page {i} ends with a dangling lead-in colon: "
                  f"{last[:80]!r}")
            problems += 1
    print(f"layout: {problems or 'no'} page-end problem(s) flagged across "
          f"{len(pages) - 1} pages. Eyeball the rendered pages regardless: "
          "split tables and diagrams need a human.")
    return 1 if problems else 0


# ---------------------------------------------------------------------------
def self_test(rules: list[Rule], budgets: dict) -> bool:
    print("SELF-TEST: proving each rule can both fire and stay silent\n")
    ok = True
    for r in rules:
        p, c = len(hits(r, r.poison)), len(hits(r, r.clean))
        p_ok, c_ok = p > r.limit, c <= r.limit
        ok = ok and p_ok and c_ok
        note = ("" if p_ok else "  <-- did not fire on poison (rule is dead)") + \
               ("" if c_ok else "  <-- fired on clean text (rule over-matches)")
        print(f"  [{'ok  ' if p_ok and c_ok else 'BAD '}] {r.id:22} "
              f"poison={p:<3} clean={c:<3}{note}")
    for bid, (poison, clean) in BUDGET_FIXTURES.items():
        p_rows = [x for x in budget_report(poison, budgets) if x[1] == bid]
        c_rows = [x for x in budget_report(clean, budgets) if x[1] == bid]
        p_ok, c_ok = bool(p_rows), not c_rows
        ok = ok and p_ok and c_ok
        note = ("" if p_ok else "  <-- did not fire on poison (check is dead)") + \
               ("" if c_ok else "  <-- fired on clean text (check over-matches)")
        print(f"  [{'ok  ' if p_ok and c_ok else 'BAD '}] {bid:22} "
              f"poison={len(p_rows):<3} clean={len(c_rows):<3}{note}")
    print()
    if not ok:
        print("REFUSED: at least one rule failed its own fixtures. Fix before "
              "grading.\n")
    else:
        print("All rules and budget checks proved. Safe to grade.\n")
    return ok


def grade(path: pathlib.Path, cfg: dict, rules: list[Rule],
          facts_path: pathlib.Path | None) -> int:
    text = path.read_text(encoding="utf-8")
    words = len(strip_fenced(text).split())
    print(f"GRADING {path.name}  ({words:,} words)\n")
    fails = 0
    for r in rules:
        found = hits(r, text)
        if len(found) <= r.limit:
            print(f"  [pass] {r.id:22} {len(found)} (limit {r.limit})")
            continue
        if r.severity == FAIL:
            fails += 1
        print(f"  [{'FAIL' if r.severity == FAIL else 'warn'}] {r.id:22} "
              f"{len(found)} occurrences. {r.why}")
        for line, frag in found[:5]:
            print(f"           line {line}: {frag}")
        if len(found) > 5:
            print(f"           ... and {len(found) - 5} more")
    print()
    for sev, bid, msg in budget_report(text, cfg["budgets"]):
        if sev == FAIL:
            fails += 1
        print(f"  [{'FAIL' if sev == FAIL else 'warn'}] {bid:22} {msg}")
    print()
    for label, results, hard in (
            ("directives", check_directives(text, set(cfg["directives"])), True),
            ("figures", check_figures(text, facts_path,
                                      cfg.get("figure_freebies", {})), False)):
        if not results:
            print(f"  [pass] {label:22} nothing to flag")
            continue
        if hard:
            fails += 1
        print(f"  [{'FAIL' if hard else 'warn'}] {label:22} {len(results)} to review")
        for line in results[:12]:
            print(f"           {line}")
        if len(results) > 12:
            print(f"           ... and {len(results) - 12} more")
    print()
    print("NOT CHECKED HERE. These need a reader or a model, see rubric.md:")
    for item in ("does each section lead with its conclusion",
                 "does every finding carry implication and recommendation",
                 "is any section exclusively negative, and is the balance near 60/40",
                 "does anything read as a pitch for a second phase",
                 "are the worked examples framed as the framework applied",
                 "is the register close to the house exemplar"):
        print(f"    - {item}")
    print()
    print(f"{'ARTEFACT FAILS' if fails else 'Deterministic checks pass'}"
          f"{f' ({fails} hard failures)' if fails else ''}. "
          "Warnings are judgement calls, not automatic failures.")
    return 1 if fails else 0


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--layout" in args:
        i = args.index("--layout")
        sys.exit(check_layout(pathlib.Path(args[i + 1])))
    cfg_path = HERE / "check.config.json"
    if "--config" in args:
        i = args.index("--config")
        cfg_path = pathlib.Path(args[i + 1])
        del args[i:i + 2]
    if "--observations" in args:
        i = args.index("--observations")
        workspace = pathlib.Path(args[i + 1])
        sources_dir = None
        if "--sources" in args:
            j = args.index("--sources")
            sources_dir = pathlib.Path(args[j + 1])
        sys.exit(check_observations(workspace, load_config(cfg_path), sources_dir))
    facts_path = None
    if "--facts" in args:
        i = args.index("--facts")
        facts_path = pathlib.Path(args[i + 1])
        del args[i:i + 2]
    cfg = load_config(cfg_path)
    rules = build_rules(cfg)
    if not self_test(rules, cfg["budgets"]):
        sys.exit(2)
    if "--self-test" in args:
        sys.exit(0)
    targets = [a for a in args if not a.startswith("-")]
    if not targets:
        print("Nothing to grade. Pass a path, or use --self-test.")
        sys.exit(0)
    sys.exit(grade(pathlib.Path(targets[0]), cfg, rules, facts_path))
