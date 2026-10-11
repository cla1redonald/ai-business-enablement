#!/usr/bin/env python3
"""workbook: build the opportunity workbook xlsx from the confirmed engagement data.

Never edited by hand: names are not identifiers, and a hand-edited join breaks
silently. Joins carry stable IDs alongside display names; every count is recomputed
here from data/landscape.json. The Read me sheet's six-questions table is the same
text as the report skeleton's annex E, kept in one constant below.

Usage:
    ./workbook.py <workspace-dir>       writes <workspace>/artefacts/workbook.xlsx
"""
from __future__ import annotations

import json
import pathlib
import sys

import openpyxl
from openpyxl.styles import Alignment, Font

# Kept verbatim in step with templates/report-skeleton.md annex E.
SIX_QUESTIONS = [
    ("1. Where does unstarted value concentrate?",
     "Opportunities sheet: rank by the Function(s) and Impact grade columns, then ask "
     "each owning team what is already moving"),
    ("2. Is the path open or gated?",
     "Opportunities sheet: Enabling gap dependencies column. Value streams sheet: "
     "Enabling gaps column. Blank means the path is open"),
    ("3. If gated, what does moving the gate release?",
     "Enabling gaps sheet: Opportunities waiting column"),
    ("4. How strong is the evidence underneath?",
     "Value streams sheet: Source count column. Opportunities sheet: Quantified "
     "figure and Figure unit columns"),
    ("5. What does it cost to try?",
     "Opportunities sheet: Effort grade column, read alongside Impact grade"),
    ("6. What does the route assume, and who owns testing it?",
     "Not held as data. Use the Description column as the starting point, then agree "
     "the assumption and its owner with the owning team"),
]

BOLD = Font(bold=True)
WRAP = Alignment(wrap_text=True, vertical="top")


def bar(values):
    return " | ".join(values)


def build(ws_dir: pathlib.Path) -> pathlib.Path:
    land = json.loads((ws_dir / "data" / "landscape.json").read_text())
    facts = json.loads((ws_dir / "facts.json").read_text())
    eng = json.loads((ws_dir / "engagement.json").read_text())
    opps, streams, gaps = land["opportunities"], land["streams"], land["gaps"]
    by_stream = {s["id"]: s for s in streams}
    by_gap = {g["id"]: g for g in gaps}
    f = facts["figures"]

    wb = openpyxl.Workbook()

    # --- Read me -----------------------------------------------------------
    rm = wb.active
    rm.title = "Read me"
    rm.column_dimensions["A"].width = 52
    rm.column_dimensions["B"].width = 95
    rows: list[tuple[str, str, bool]] = [
        (f"{eng['client_display']} AI opportunity workbook", "", True),
        (f"Data companion to the {eng['client_display']} AI Business Enablement "
         f"report.", "", False),
        ("", "", False),
        ("What this workbook is", "", True),
        (f"This workbook holds the working data behind the report: all "
         f"{f['n_opportunities']} opportunities recorded during the assessment, the "
         f"{f['n_streams']} value streams they map to, and the {f['n_gaps']} enabling "
         f"gaps that gate delivery. It is arranged so the report's six-question "
         f"framework can be run directly against it in one working session.",
         "", False),
        ("", "", False),
        ("How it pairs with the report's six-question framework", "", True),
    ]
    for q, where in SIX_QUESTIONS:
        rows.append((q, where, False))
    blanks = f["blanks"]
    rows += [
        ("", "", False),
        ("Delivery status is deliberately absent", "", True),
        ("This workbook records no delivery status for any opportunity or value "
         "stream, and neither does the report. Whether a piece of work is not "
         "started, underway or done is something only the owning teams can answer "
         "reliably, so confirm it with them before sequencing anything. The Status "
         "column on the Enabling gaps sheet is different: it records the readiness "
         "of each enabling gap itself, which is the assessment's own instrument "
         "rather than a judgement about anyone's delivery.", "", False),
        ("", "", False),
        ("Notes on reading the data", "", True),
        ("People are referred to by role, and named client organisations by neutral "
         "token, never by name.", "", False),
        ("An opportunity split across more than one function or value stream lists "
         "all of them, separated by a vertical bar. IDs are stable; joins use the ID "
         "columns, and display names may change.", "", False),
        (f"{blanks['ungraded']} opportunity carries no impact or effort grade, "
         f"{blanks['no_function']} carries no function and {blanks['no_stream']} "
         f"sit on no value stream. Blank cells are recorded gaps in the data, not "
         f"errors.", "", False),
    ]
    for r, (a, b, bold) in enumerate(rows, 1):
        ca = rm.cell(row=r, column=1, value=a)
        ca.alignment = WRAP
        if bold:
            ca.font = BOLD
        if b:
            cb = rm.cell(row=r, column=2, value=b)
            cb.alignment = WRAP

    # --- Opportunities -----------------------------------------------------
    op = wb.create_sheet("Opportunities")
    headers = ["Opportunity ID", "Opportunity", "Description", "Function(s)",
               "Value stream(s)", "Value stream ID(s)", "Impact grade",
               "Effort grade", "Quantified figure", "Figure unit",
               "Enabling gap dependencies", "Enabling gap ID(s)"]
    op.append(headers)
    for o in opps:
        q = o.get("quantified")
        op.append([
            o["id"], o["name"], o["description"], bar(o["functions"]),
            bar(by_stream[s]["name"] for s in o["streams"]), bar(o["streams"]),
            o["impact"], o["effort"],
            q["figure"] if q else None, q["unit"] if q else None,
            bar(by_gap[g]["name"] for g in o["gaps"]), bar(o["gaps"]),
        ])

    # --- Value streams -----------------------------------------------------
    vs = wb.create_sheet("Value streams")
    vs.append(["Value stream ID", "Value stream", "Statement", "Start event",
               "End event", "Functions crossed", "Member count", "Source count",
               "Enabling gaps", "Enabling gap ID(s)", "Impact grade"])
    per_stream = {row["id"]: row for row in facts["tables"]["streams"]}
    for s in streams:
        d = per_stream[s["id"]]
        vs.append([
            s["id"], s["name"], s["statement"], s["start"], s["end"],
            bar(s["functions"]), d["member_count"], d["source_count"],
            bar(by_gap[g]["name"] for g in d["gap_ids"]), bar(d["gap_ids"]),
            s["impact"],
        ])

    # --- Enabling gaps -----------------------------------------------------
    gp = wb.create_sheet("Enabling gaps")
    gp.append(["Enabling gap ID", "Enabling gap", "Enabler", "Status",
               "Opportunities waiting"])
    waiting = {row["id"]: row["waiting"] for row in facts["tables"]["gaps_waiting"]}
    for g in gaps:
        gp.append([g["id"], g["name"], g["enabler"], g["status"], waiting[g["id"]]])

    for sheet in (op, vs, gp):
        for cell in sheet[1]:
            cell.font = BOLD
        for col, width in zip("ABCDEFGHIJKL", (16, 45, 70, 24, 40, 18, 12, 12,
                                               45, 18, 12, 18)):
            if col in sheet.column_dimensions:
                sheet.column_dimensions[col].width = width

    out = ws_dir / "artefacts" / "workbook.xlsx"
    out.parent.mkdir(parents=True, exist_ok=True)
    wb.save(out)
    return out


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: workbook.py <workspace-dir>")
        sys.exit(2)
    out = build(pathlib.Path(sys.argv[1]))
    print(f"workbook: written to {out}")
