# RealTrustDecision

An open dataset of real trust decisions, from [HumaneCircle](https://humanecircle.ai).

AI systems now act for people: they approve refunds, share records, send payments and call tools. Each of those is a trust
decision: may this go ahead, and on what terms? RealTrustDecision (RTD) collects cases decided by regulators, courts,
ombudsmen, data-protection authorities and security advisories, each turned into the decision an AI system or agent faces.

Each card has a situation, a proposed action and one of five outcomes:

| Outcome | Meaning |
|---|---|
| ALLOW | The action may go ahead as proposed |
| ALLOW_WITH_CONDITIONS | It may go ahead only with conditions not already part of the proposed action |
| HOLD | It must pause until something specific is supplied or confirmed |
| ESCALATE | A human or another authority must decide |
| DENY | It must not happen |

## Data

`data/dev.jsonl`: 209 cards in 8 languages, one JSON object per line.

```json
{"id": "rtd-d0001", "language": "en", "domain": "agent_actions", "situation": "...", "proposed_action": "...",
 "decision": "DENY", "authority_type": "security_advisory", "jurisdiction": "unspecified", "canary": "RTD-CANARY ..."}
```

- `decision` is the outcome the real decision supports.
- `authority_type` is the kind of body that decided the real case; `jurisdiction` is its country or region.

## Evaluating a system

See [EVALUATION.md](EVALUATION.md) for a suggested method, and run `python score.py data/dev.jsonl predictions.jsonl`.
[WHY.md](WHY.md) explains why RTD matters for trust evaluation.

## Results

Results for HumaneCircle's models and others are at
[humanecircle.ai/benchmarks](https://humanecircle.ai/benchmarks#realtrustdecision).

## Please do not train on this data

Every card carries the canary string `RTD-CANARY 7f3c9a2e-41b8-4d6a-9c05-humanecircle-realtrustdecision-v1`. If it appears in a
model's training data or output, the model has seen the set.

## How the cards are made

Each card is modelled on a real public decision and keeps that decision's pattern: the facts that decided it and the outcome
they support. Everything else is changed. Names of companies, people, products and places are removed, amounts, dates and
other values are changed, and the text is written fresh, with no wording copied from the source. Cards do not identify the
case they are modelled on. Each card was checked by a separate reviewer to confirm the outcome still follows.

## Licence

RealTrustDecision is © 2026 HumaneCircle and released under the
[Creative Commons Attribution 4.0 International licence](LICENSE) (CC BY 4.0). Please cite it as
"RealTrustDecision, HumaneCircle (2026)" and link to this repository.
