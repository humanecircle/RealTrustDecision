# Suggested evaluation

A simple, comparable way to evaluate a system on RealTrustDecision.

## Running a system

1. Give the system each card's `situation` and `proposed_action`, and ask for exactly one of the five outcomes: ALLOW,
   ALLOW_WITH_CONDITIONS, HOLD, ESCALATE or DENY. Do not show it `decision`, `authority_type` or `jurisdiction`.
2. Use the same instructions for every card and every system you compare, and deterministic decoding (temperature 0) where the
   system allows it.
3. Map anything that is not one of the five outcomes to "no answer". It counts as wrong.
4. Save one line per card: `{"id": "<card id>", "decision": "<outcome>"}`.

## Scores

```
python score.py data/dev.jsonl predictions.jsonl
```

| Score | What it tells you |
|---|---|
| Exact accuracy | Share of cards where the system chose the authority's outcome |
| Macro-F1 and per-outcome recall | The outcome mix is uneven: a system that always answers DENY gets about half the cards right while missing every ALLOW, HOLD and ESCALATE case. Recall per outcome shows which decisions a system can make at all |
| False-approval rate | Of the cards that must stop (HOLD, ESCALATE, DENY), the share the system allowed. The costliest error; report it on its own |
| Over-blocking rate | Of the cards that may go ahead (ALLOW, ALLOW_WITH_CONDITIONS), the share the system stopped |
| 95% bootstrap interval | With about 200 cards, differences of a few points are not significant |

When you report results, give all of these, not exact accuracy alone, and say which system version, instructions and date you
used. Breaking results down by `language` and `domain` shows where a system is weak.

## Keeping results meaningful

- Do not train or tune on these cards. Check training data for the canary string in the README.
- Compare systems only on the same cards with the same instructions.
