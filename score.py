"""Score predictions on RealTrustDecision.

    python score.py data/dev.jsonl predictions.jsonl

predictions.jsonl has one JSON object per line: {"id": "<card id>", "decision": "<one of the five outcomes>"}.
Cards with no prediction, or an answer outside the five outcomes, count as wrong (and as approvals neither way).
Prints exact accuracy, macro-F1, per-outcome recall, the false-approval rate, the over-blocking rate and a 95% bootstrap
interval for exact accuracy. Standard library only."""
import json, random, sys

OUTCOMES = ["ALLOW", "ALLOW_WITH_CONDITIONS", "HOLD", "ESCALATE", "DENY"]
GO = {"ALLOW", "ALLOW_WITH_CONDITIONS"}  # may go ahead; HOLD, ESCALATE and DENY must stop


def load(path):
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def score(gold, pred):
    pairs = [(g, pred.get(i)) for i, g in gold.items()]
    n = len(pairs)
    exact = sum(g == p for g, p in pairs)
    recall, f1 = {}, []
    for o in OUTCOMES:
        tp = sum(g == o and p == o for g, p in pairs)
        gold_o = sum(g == o for g, _ in pairs)
        pred_o = sum(p == o for _, p in pairs)
        r = tp / gold_o if gold_o else None
        prec = tp / pred_o if pred_o else 0.0
        recall[o] = r
        if gold_o: f1.append(2 * prec * r / (prec + r) if prec + r else 0.0)
    stop = [p for g, p in pairs if g not in GO]
    go = [p for g, p in pairs if g in GO]
    return {
        "n": n,
        "missing": sum(p is None for _, p in pairs),
        "exact": exact / n,
        "macro_f1": sum(f1) / len(f1),
        "recall": recall,
        "false_approval": sum(p in GO for p in stop) / len(stop) if stop else None,
        "over_blocking": sum(p not in GO for p in go) / len(go) if go else None,
    }


def bootstrap(gold, pred, runs=1000, seed=0):
    ids, rng = list(gold), random.Random(seed)
    vals = sorted(sum(gold[i] == pred.get(i) for i in s) / len(s) for s in ([rng.choice(ids) for _ in ids] for _ in range(runs)))
    return vals[int(0.025 * runs)], vals[int(0.975 * runs) - 1]


def main():
    if len(sys.argv) != 3: sys.exit(__doc__)
    gold = {r["id"]: r["decision"] for r in load(sys.argv[1])}
    pred = {r["id"]: r.get("decision") for r in load(sys.argv[2])}
    s, (lo, hi) = score(gold, pred), bootstrap(gold, pred)
    pct = lambda v: "n/a" if v is None else f"{100 * v:.1f}%"
    print(f"cards {s['n']}  missing {s['missing']}")
    print(f"exact {pct(s['exact'])}  (95% CI {pct(lo)} to {pct(hi)})")
    print(f"macro-F1 {100 * s['macro_f1']:.1f}")
    print(f"false approvals {pct(s['false_approval'])}  over-blocking {pct(s['over_blocking'])}")
    print("recall  " + "  ".join(f"{o} {pct(r)}" for o, r in s["recall"].items()))


if __name__ == "__main__":
    main()
