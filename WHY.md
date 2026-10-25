# Why RealTrustDecision

AI systems are moving from answering questions to taking actions, such as approving a refund, sharing a record, sending a
payment or calling a tool. Each action is a trust decision: whether it may go ahead, and on what terms. RealTrustDecision is
designed to evaluate those decisions.

## What existing benchmarks cover

Safety and guardrail benchmarks such as ToxicChat, Aegis, WildGuard, BeaverTails, HarmBench and XSTest ask whether a piece of
text is harmful. They remain important, but they leave several aspects of decision making untested.

| Gap | Why it matters |
|---|---|
| Two outcomes instead of five | Many real actions may proceed only with a safeguard, must wait for missing information, or need a person to decide. A system limited to allow or block will either block too much or allow what should have waited. |
| Content instead of actions | Most datasets judge a single message. A decision concerns an action in context: who is asking, what they want done, what rules apply, and what is known or unknown. |
| Annotator labels | Labels usually come from crowd annotators or generated data. Decisions by regulators, courts and ombudsmen reflect how cases are actually resolved, and are often less obvious. |
| A single taxonomy | Each benchmark reflects one definition of harm. Real decisions depend on the rules in force, which vary by jurisdiction, sector and organisation. |

## Principles

- Trust is a decision rather than a filter. The question is whether a specific action, by a specific system, for a specific
  person, may proceed now and under what conditions.
- The right answer depends on the applicable rules. The same action can be acceptable under one policy or jurisdiction and not
  under another.
- Errors are not equally costly. Approving an action that should have been stopped is usually worse than stopping one that could
  have proceeded, so the two are measured separately.
- Recognising when to pause or escalate is part of the task. HOLD and ESCALATE are the outcomes systems most often miss.

## What the dataset provides

- Cases modelled on public decisions by regulators, courts, ombudsmen, data protection authorities and security advisories, with
  identifying details removed.
- Five outcomes: ALLOW, ALLOW_WITH_CONDITIONS, HOLD, ESCALATE and DENY.
- Coverage across agent actions, privacy and data, grounding, routing and escalation, release decisions, conversation harms and
  several jurisdictions, in 8 languages.

## Intended users

- Teams deploying AI agents that act for customers or staff.
- Risk, compliance and audit teams looking for a measure grounded in how real decisions are made.
- Researchers and model developers working on decisions beyond allow or block.
