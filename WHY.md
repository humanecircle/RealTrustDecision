# Why RealTrustDecision

AI systems are moving from answering questions to taking actions: approving a refund, sharing a record, sending a payment,
publishing a post, calling a tool on someone's behalf. Each of those actions is a **trust decision**: may this go ahead, and on
what terms? RealTrustDecision measures how well an AI system makes those decisions, using decisions that real authorities made.

## What existing benchmarks measure, and what they miss

Safety and guardrail benchmarks (ToxicChat, Aegis, WildGuard, BeaverTails, HarmBench, XSTest, jailbreak and injection sets) ask one
question: **is this text harmful?** They are essential, and they are not enough for decisions:

| Gap | Why it matters for trust decisions |
|---|---|
| **Two outcomes, not five** | Real decisions are rarely yes or no. Many actions may go ahead *only with* a safeguard, must *wait* for something (identity, consent, a missing document), or need *a person* to decide. A system that can only allow or block will either block too much or allow what should have waited. |
| **Content, not actions** | Most sets judge a message. Decisions are about an action in a situation: who is asking, what they want done, what rules apply, what is known and unknown. |
| **Synthetic or annotator labels** | Labels come from crowd annotators or model generators. A decision made by a regulator, court, ombudsman or data-protection authority is a real ruling with real consequences, and often non-obvious. |
| **One taxonomy** | Each benchmark encodes one organisation's idea of "harmful". Real decisions depend on the rules in force, which differ by jurisdiction, sector and company. |

## How to think about trust

- **Trust is a decision, not a filter.** The question is whether this action, by this system, for this person, may go ahead now,
  and on what terms.
- **The answer depends on the rules.** The same action can be fine under one policy or jurisdiction and wrong under another. When
  the rules are known, the decision should follow them; when they are not, a careful system says so.
- **Some errors cost more.** Approving what should have stopped is the expensive mistake. It should be measured on its own, not
  averaged away with over-caution.
- **Knowing when to stop and ask is part of the job.** HOLD and ESCALATE are where systems fail most: they rarely recognise when
  something is missing or when a person must decide.

## What RealTrustDecision does differently

- **Real decisions.** Every card is modelled on a public decision by a regulator, court, ombudsman, data-protection authority,
  security advisory or official record, turned into the decision an AI system or agent faces. Names and details are anonymised;
  the pattern that decided the case is kept.
- **Five outcomes:** ALLOW, ALLOW_WITH_CONDITIONS, HOLD, ESCALATE, DENY.
- **Two parts.** *RTD-Full:* the system decides from the situation alone, as a careful expert would. *RTD-Rules:* the governing
  rules are stated, and the system must apply them, the way a company deploys AI under its own policies.
- **Many languages and domains:** agent actions, privacy and data, grounding, routing and escalation, release decisions,
  conversation harms and decisions outside the US and EU.

## Who it is for

- Teams deploying AI agents that act on behalf of customers or staff, who need evidence that the system decides well before it acts.
- Risk, compliance and audit teams who need a measure tied to how real authorities decide.
- Model builders who want a decision benchmark that rewards conditions, holds and escalation, not only blocking.
