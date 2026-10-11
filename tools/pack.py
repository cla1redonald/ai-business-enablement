#!/usr/bin/env python3
"""pack: build the versioned, immutable client pack from an engagement workspace.

Composes the deliverable folder (report, workbook, maps, briefs, summaries), writes
its README and agent-facing CLAUDE.md from the kit templates filled from the facts
manifest, audits the result for draft markers, unfilled slots and stray names, zips
it, and refuses ever to overwrite an existing baseline. Baselines are immutable:
changes are the next version, in a new folder.

Usage:
    ./pack.py <workspace-dir> --version 1
"""
from __future__ import annotations

import datetime
import json
import pathlib
import re
import shutil
import sys
import zipfile

HERE = pathlib.Path(__file__).parent
TEMPLATES = HERE.parent / "templates"

DRAFT_MARKERS = ["DRAFT", "TODO", "TBC", "FIXME", "lorem ipsum"]
TEXT_SUFFIXES = {".md", ".html", ".txt", ".csv", ".json"}


def fill(template: pathlib.Path, slots: dict[str, str]) -> str:
    text = template.read_text()
    # The leading HTML comment is template guidance, not deliverable content.
    text = re.sub(r"^<!--.*?-->\s*", "", text, flags=re.S)
    for key, value in slots.items():
        text = text.replace(key, str(value))
    return text


def audit(pack_dir: pathlib.Path, names: list[str]) -> list[str]:
    problems = []
    name_pat = (re.compile(r"\b(" + "|".join(re.escape(n) for n in names) + r")\b",
                           re.I) if names else None)
    for f in sorted(pack_dir.rglob("*")):
        if not f.is_file() or f.suffix.lower() not in TEXT_SUFFIXES:
            continue
        text = f.read_text(errors="replace")
        rel = f.relative_to(pack_dir)
        for marker in DRAFT_MARKERS:
            if re.search(rf"\b{re.escape(marker)}\b", text):
                problems.append(f"{rel}: draft marker '{marker}'")
        for m in re.finditer(r"\{[a-z_][a-z0-9_ ]{1,40}\}", text, re.I):
            problems.append(f"{rel}: unfilled slot {m.group(0)}")
        if name_pat:
            for m in name_pat.finditer(text):
                problems.append(f"{rel}: stray name '{m.group(0)}'")
    return problems


def build(ws: pathlib.Path, version: int) -> int:
    eng = json.loads((ws / "engagement.json").read_text())
    facts = json.loads((ws / "facts.json").read_text())
    f = facts["figures"]
    client_slug = re.sub(r"[^A-Za-z0-9]+", "_", eng["client_display"]).strip("_")

    pack_name = f"{client_slug}_AI_Business_Enablement_V{version}"
    pack_dir = ws / "packs" / pack_name
    if pack_dir.exists():
        print(f"REFUSED: {pack_dir} already exists. Baselines are immutable; "
              f"build V{version + 1} instead.")
        return 2

    art = ws / "artefacts"
    report_src = art / "report.md"
    workbook_src = art / "workbook.xlsx"
    for required in (report_src, workbook_src):
        if not required.exists():
            print(f"REFUSED: missing artefact {required}")
            return 2

    report_file = f"{client_slug}_AI_Business_Enablement_Report_V{version}.md"
    workbook_file = f"{client_slug}_Opportunity_Workbook_V{version}.xlsx"

    pack_dir.mkdir(parents=True)
    shutil.copy2(report_src, pack_dir / report_file)
    shutil.copy2(workbook_src, pack_dir / workbook_file)
    for sub in ("maps", "briefs", "summaries"):
        src = art / sub
        if src.exists():
            shutil.copytree(src, pack_dir / {"maps": "value-stream-maps",
                                             "briefs": "enabling-gap-briefs",
                                             "summaries": "call-summaries"}[sub])

    blanks = f["blanks"]
    blank_sentence = (f"{blanks['ungraded']} opportunity has no impact or effort "
                      f"grade, {blanks['no_function']} has no function, "
                      f"{blanks['no_stream']} sit on no stream.")
    slots = {
        "{Client token}": eng["client_display"],
        "{client token}": eng["client_display"],
        "{report_file}": report_file,
        "{workbook_file}": workbook_file,
        "{consultancy}": eng["consultancy"],
        "{consultant name}": eng.get("consultant_display", "the consultant"),
        "{period}": eng["period"],
        "{evidence_period}": eng["evidence_period"],
        "{date}": datetime.date.today().isoformat(),
        "{n_opportunities}": f["n_opportunities"],
        "{n_streams}": f["n_streams"],
        "{n_gaps}": f["n_gaps"],
        "{n_conversations}": f["n_conversations"],
        "{n_documents}": f["n_documents"],
        "{n_observations}": f["n_observations"],
        "{n_multi}": f["n_multi_stream"],
        "{multi_phrase}": (f"{f['n_multi_stream']} opportunity sits"
                           if f["n_multi_stream"] == 1
                           else f"{f['n_multi_stream']} opportunities sit"),
        "V{n}": f"V{version}",
        "{The blank-cell counts, from the facts manifest.}": blank_sentence,
        "{n_maps}": len(list((pack_dir / "value-stream-maps").glob("*.html"))
                        if (pack_dir / "value-stream-maps").exists() else []),
        "{n_briefs}": len(list((pack_dir / "enabling-gap-briefs").glob("*.html"))
                          if (pack_dir / "enabling-gap-briefs").exists() else []),
    }
    (pack_dir / "README.md").write_text(fill(TEMPLATES / "pack-readme.md", slots))
    (pack_dir / "CLAUDE.md").write_text(fill(TEMPLATES / "pack-claude.md", slots))

    problems = audit(pack_dir, eng.get("names", []))
    if problems:
        print(f"AUDIT FAILED: {len(problems)} problem(s). Pack left in place for "
              "inspection; fix and rebuild before delivering.")
        for p in problems[:20]:
            print(f"  {p}")
        return 1

    zip_path = pack_dir.with_suffix(".zip")
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for file in sorted(pack_dir.rglob("*")):
            if file.is_file():
                z.write(file, file.relative_to(pack_dir.parent))
    print(f"pack: {pack_dir} built and audited clean; {zip_path.name} written. "
          "This baseline is now immutable: changes are the next version.")
    return 0


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) < 1:
        print("Usage: pack.py <workspace-dir> --version <n>")
        sys.exit(2)
    version = 1
    if "--version" in args:
        i = args.index("--version")
        version = int(args[i + 1])
    sys.exit(build(pathlib.Path(args[0]), version))
