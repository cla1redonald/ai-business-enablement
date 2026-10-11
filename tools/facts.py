#!/usr/bin/env python3
"""facts: build the facts manifest for an engagement workspace.

Every count and figure any artefact may publish, derived from the confirmed data and
never typed, each group carrying its provenance. Artefacts read this file; check.py
verifies human-written artefacts against it. If a number is not derivable here, it is
not publishable without a human confirming it by hand.

Usage:
    ./facts.py <workspace-dir>          writes <workspace>/facts.json
"""
from __future__ import annotations

import json
import pathlib
import sys
from collections import defaultdict

CONVERSATION_SUBTYPES = {"discovery interview", "consultant-led session"}
ENABLER_ORDER = ["Trusted information", "Hosting and identity",
                 "Control and accountability", "Proof", "Adoption and capacity"]


def build(ws: pathlib.Path) -> dict:
    land = json.loads((ws / "data" / "landscape.json").read_text())
    ready = json.loads((ws / "data" / "readiness.json").read_text())
    eng = json.loads((ws / "engagement.json").read_text())

    opps, streams, gaps = land["opportunities"], land["streams"], land["gaps"]
    stream_ids = {s["id"] for s in streams}
    gap_ids = {g["id"] for g in gaps}

    # Referential integrity: a broken join is a build failure, never a warning.
    for o in opps:
        for sid in o["streams"]:
            assert sid in stream_ids, f"{o['id']} references unknown stream {sid}"
        for gid in o["gaps"]:
            assert gid in gap_ids, f"{o['id']} references unknown gap {gid}"
        q = o.get("quantified")
        assert q is None or (q.get("figure") is not None and q.get("unit")), \
            f"{o['id']}: quantified must carry figure AND unit, or be null"

    gated = [o for o in opps if o["gaps"]]
    memberships = sum(len(o["streams"]) for o in opps)
    multi = [o for o in opps if len(o["streams"]) > 1]
    quantified = [o for o in opps if o.get("quantified")]

    waiting = {g["id"]: 0 for g in gaps}
    for o in opps:
        for gid in o["gaps"]:
            waiting[gid] += 1

    per_stream = []
    for s in streams:
        members = [o["id"] for o in opps if s["id"] in o["streams"]]
        s_gaps = sorted({gid for o in opps if s["id"] in o["streams"]
                         for gid in o["gaps"]})
        per_stream.append({
            "id": s["id"], "name": s["name"], "impact": s["impact"],
            "member_count": len(members), "source_count": len(s["sources"]),
            "gap_count": len(s_gaps), "gap_ids": s_gaps,
        })

    # Share-weighted function table: an opportunity split across n functions counts
    # 1/n to each, so nothing is double counted.
    weight: dict[str, float] = defaultdict(float)
    for o in opps:
        fns = o["functions"]
        for fn in fns:
            weight[fn] += 1.0 / len(fns)
    function_table = [{"function": fn, "weighted": round(w, 1)}
                      for fn, w in sorted(weight.items(), key=lambda kv: -kv[1])]

    blanks = {
        "ungraded": len([o for o in opps if o["impact"] is None]),
        "no_function": len([o for o in opps if not o["functions"]]),
        "no_stream": len([o for o in opps if not o["streams"]]),
    }

    # Readiness roll-up, canonical enabler order.
    areas = ready["areas"]
    assert len(areas) == 20, f"readiness must carry exactly 20 areas, got {len(areas)}"
    rollup = []
    for enabler in ENABLER_ORDER:
        rows = [a for a in areas if a["enabler"] == enabler]
        assert len(rows) == 4, f"{enabler}: expected 4 areas, got {len(rows)}"
        rollup.append({"enabler": enabler,
                       "in_place": sum(1 for a in rows if a["rating"] == "in place"),
                       "partial": sum(1 for a in rows if a["rating"] == "partial"),
                       "gap": sum(1 for a in rows if a["rating"] == "gap"),
                       "blocked": sum(1 for a in rows if a["rating"] == "blocked")})
    rating_totals = {r: sum(1 for a in areas if a["rating"] == r)
                     for r in ("in place", "partial", "gap", "blocked")}

    # Sources and observations, from the observation files (one per accepted source).
    obs_files = sorted((ws / "observations").glob("obs-*.json"))
    n_obs, n_conv, n_docs = 0, 0, 0
    per_source_obs = {}
    for f in obs_files:
        d = json.loads(f.read_text())
        n_obs += len(d["observations"])
        per_source_obs[d["source"]] = len(d["observations"])
        if d["sub_type"] in CONVERSATION_SUBTYPES:
            n_conv += 1
        elif d["sub_type"] == "document":
            n_docs += 1

    return {
        "schema_version": "0.1",
        "client": eng["client_display"],
        "period": eng["period"],
        "evidence_period": eng["evidence_period"],
        "figures": {
            "n_opportunities": len(opps),
            "n_streams": len(streams),
            "n_streams_high": sum(1 for s in streams if s["impact"] == "High"),
            "n_streams_medium": sum(1 for s in streams if s["impact"] == "Medium"),
            "n_gaps": len(gaps),
            "n_gated": len(gated),
            "n_open": len(opps) - len(gated),
            "n_memberships": memberships,
            "n_multi_stream": len(multi),
            "n_quantified": len(quantified),
            "n_sources": n_conv + n_docs,
            "n_conversations": n_conv,
            "n_documents": n_docs,
            "n_observations": n_obs,
            "blanks": blanks,
            "readiness_totals": rating_totals,
        },
        "quantified_figures": [
            {"id": o["id"], "figure": o["quantified"]["figure"],
             "unit": o["quantified"]["unit"]} for o in quantified],
        "verified_evidence_figures": eng.get("verified_figures", []),
        "tables": {
            "functions_weighted": function_table,
            "streams": per_stream,
            "gaps_waiting": [{"id": g["id"], "name": g["name"],
                              "enabler": g["enabler"], "status": g["status"],
                              "waiting": waiting[g["id"]]} for g in gaps],
            "readiness_rollup": rollup,
            "observations_per_source": per_source_obs,
        },
        "provenance": {
            "figures": "derived from data/landscape.json, data/readiness.json and "
                       "observations/*.json by tools/facts.py; nothing typed",
            "weighting": "functions_weighted is share-weighted: an opportunity split "
                         "across n functions counts 1/n to each",
            "counting": "n_memberships sums stream memberships and exceeds "
                        "n_opportunities when opportunities sit on more than one "
                        "stream; gaps_waiting sums past n_gated when opportunities "
                        "wait on more than one gap",
            "verified_evidence_figures": "figures quoted from sources, confirmed by "
                                         "the consultant against the cited source; "
                                         "carried from engagement.json, each with "
                                         "its context",
        },
    }


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: facts.py <workspace-dir>")
        sys.exit(2)
    ws = pathlib.Path(sys.argv[1])
    manifest = build(ws)
    out = ws / "facts.json"
    out.write_text(json.dumps(manifest, indent=2) + "\n")
    f = manifest["figures"]
    print(f"facts: {f['n_opportunities']} opportunities, {f['n_streams']} streams "
          f"({f['n_streams_high']} high, {f['n_streams_medium']} medium), "
          f"{f['n_gaps']} gaps, {f['n_gated']} gated, {f['n_observations']} "
          f"observations from {f['n_conversations']} conversations and "
          f"{f['n_documents']} documents -> {out}")
