"""Merge Research Packets (JSON, per research_packet.schema.json) from several AIs.
Groups identical sources by URL/origin, counts how many runs and independent origins support
each normalized claim, and writes merge_report.md for the orchestrator to verify and write up.

Usage: python merge_packets.py packet_chatgpt.json packet_gemini.json packet_claude.json
Note: claim grouping here is by normalized text only. The orchestrator (an AI or a person)
still has to group paraphrased claims and verify linchpins against primary sources.
"""
import json, re, sys
from collections import defaultdict
from pathlib import Path


def norm(text: str) -> str:
    # why: keep decimal points inside numbers (2.5%) but drop sentence punctuation
    t = re.sub(r"(\d)\.(\d)", r"\1DOT\2", text.lower())
    t = re.sub(r"[^a-z0-9%]+", " ", t).strip()
    return t.replace("qqdotqq", ".")


def main(paths):
    if not paths:
        raise SystemExit(__doc__)
    groups = defaultdict(lambda: {"producers": set(), "origins": set(), "confidence": [], "rq": set(), "text": ""})
    gaps, contradictions = [], []
    for p in paths:
        data = json.loads(Path(p).read_text(encoding="utf-8"))
        producer = data.get("producer", p)
        sources = {s["id"]: s for s in data.get("sources", [])}
        for f in data.get("findings", []):
            g = groups[norm(f["claim"])]
            g["text"] = g["text"] or f["claim"]
            g["producers"].add(producer)
            g["confidence"].append(f["confidence"])
            g["rq"].add(f["rq"])
            for sid in f.get("source_ids", []):
                src = sources.get(sid, {})
                origin_id = src.get("origin_of")
                origin = sources.get(origin_id, src).get("url") if origin_id else src.get("url", sid)
                g["origins"].add(origin)
        gaps += [f"{producer}: {x}" for x in data.get("gaps", [])]
        contradictions += [{**c, "producer": producer} for c in data.get("contradictions", [])]

    lines = ["# Merge report", "", "| claim | RQ | runs | independent origins | confidences | signal |", "|:---|:---|:---|:---|:---|:---|"]
    for g in sorted(groups.values(), key=lambda x: (-len(x["origins"]), -len(x["producers"]))):
        runs, origins = len(g["producers"]), len(g["origins"])
        if runs >= 2 and origins >= 2:
            signal = "corroborated: may raise one level after verification"
        elif runs >= 2:
            signal = "same origin repeated: no extra confidence"
        else:
            signal = "single run: verify if linchpin"
        lines.append(f"| {g['text']} | {', '.join(sorted(g['rq']))} | {runs} | {origins} | {', '.join(g['confidence'])} | {signal} |")
    lines += ["", "## Contradictions"] + [f"- [{c['producer']}] {c['topic']}: A={c['side_a']} / B={c['side_b']} ({c.get('likely_reason', '?')})" for c in contradictions]
    lines += ["", "## Gaps"] + [f"- {g}" for g in gaps]
    Path("merge_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"merge_report.md written: {len(groups)} claim groups from {len(paths)} packets")


if __name__ == "__main__":
    main(sys.argv[1:])
