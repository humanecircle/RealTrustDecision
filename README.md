# RealTrustDecision

RealTrustDecision is an open dataset of trust decisions for AI systems and agents.

AI systems increasingly act on behalf of people. They approve refunds, share records, send payments and call tools. Each of these
actions raises the same question: may it go ahead, and on what terms? This dataset provides realistic cases for evaluating how
well a system answers that question.

Each card describes a situation and a proposed action, and is labelled with one of five outcomes:

| Outcome | Meaning |
|---|---|
| ALLOW | The action may go ahead as proposed. |
| ALLOW_WITH_CONDITIONS | The action may go ahead only with conditions that are not already part of it. |
| HOLD | The action must pause until something specific is supplied or confirmed. |
| ESCALATE | A person or another authority must decide. |
| DENY | The action must not go ahead. |

## Data

`data/dev.jsonl` contains 209 cards in 8 languages, one JSON object per line.

```json
{"id": "rtd-d0001", "language": "en", "domain": "agent_actions", "situation": "...", "proposed_action": "...",
 "decision": "DENY", "authority_type": "security_advisory", "jurisdiction": "unspecified", "canary": "RTD-CANARY ..."}
```

| Field | Description |
|---|---|
| `decision` | The expected outcome. |
| `domain` | The area the case belongs to, such as privacy and data or agent actions. |
| `authority_type` | The type of body whose public decision the case is modelled on. |
| `jurisdiction` | The country or region of that decision. |

## How the cards were written

Each card is modelled on a public decision by a regulator, court, ombudsman, data protection authority or security advisory.
The facts that determined the outcome are kept. Names of organisations, people, products and places are removed, values and
dates are changed, and all text is newly written. No card identifies the case it is based on.

## Evaluation

[EVALUATION.md](EVALUATION.md) describes a suggested evaluation procedure. To score a set of predictions:

```
python score.py data/dev.jsonl predictions.jsonl
```

[WHY.md](WHY.md) explains the motivation for the dataset.

## Contamination

Please do not train on this data. Every card contains the canary string
`RTD-CANARY 7f3c9a2e-41b8-4d6a-9c05-humanecircle-realtrustdecision-v1`, which can be used to detect the data in training corpora.

## Licence

RealTrustDecision is © 2026 HumaneCircle and is released under the
[Creative Commons Attribution 4.0 International licence](LICENSE). Please cite it as "RealTrustDecision, HumaneCircle (2026)".
