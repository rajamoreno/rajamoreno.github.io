---
layout: post
title: "arbitration with ai"
date: 2026-02-24
---

*Epistemic status: lightly held musings. I know almost zero about arbitration and could just be completely missing the point here.*

One key bottleneck to adoption of AI tools in the law is the longstanding and important role of the trial in the American legal system. Here's my inelegant rephrasing of my partner's arguments to this effect: AI systems are not yet legal persons and are therefore presumptively ineligible to be members of the bar and argue in court. And even if that were not true, as long as human judges want themselves and human juries to hear arguments from human litigators, those human litigators are going to be gainfully employed. I think this is a pretty good argument for at least the medium term (5-8 years?), because the American legal system is pretty small-c conservative and the idea of fundamentally reformatting our public justice system on that timescale feels undesirable/politically infeasible, even for someone who thinks things are pretty crazy right now and are likely to get crazier.[^1] Notice that I just said "public justice system".[^2] I wonder whether the gap in AI capabilities will make the next few years a great time to establish an AI-driven arbitration practice.

The cost of the judicial system is borne by the taxpayer. The cost of arbitration is borne by one or more of the parties involved in the arbitration. If all parties feel like they will get a better deal out of choosing arbitration, at lower time and dollar cost, they might have a reason to opt in to arbitration and opt out of classic litigation. Arbitration is currently expensive because the time of the w.l.o.g. skilled former judges/experienced attorneys who do arbitration is expensive.[^3] This is an overdetermined observation, but I think that AI could be a significant productivity enhancer for today's human arbitrators. Suppose there existed a system that could do the following things:

- Securely collect relevant documents from each party to the dispute. (MVP: secure file upload portal. Improvement: that plus an agentic interviewing system that identifies documents or evidence that might be relevant but isn't yet uploaded.)
- Filter, categorize, and score the documents.
- Analyze the documents from all parties to produce rich, grounded summaries of each party's position, the relevant supporting evidence, and the likely range of fair outcomes.
- Be a live interface to all documents; enable better and richer search across all key evidence.

I claim that such a system should make a human arbitrator at least twice as efficient.

More speculatively, AI could act as the actual arbiter. It could be the thing described above, but also return the "fairest" resolution of the dispute to both parties given available evidence. This skill seems quite difficult to develop (and difficult to get buy-in for from consumers of legal services) but could be valuable at the right cost. You'd need to solve a bunch of fun technical problems (e.g., data filtering and monitoring to make sure people aren't trying to jailbreak the judges). You'd also probably need some human review at the beginning. But assuming reasonably good solutions to those technical problems, this system could get negotiations moving more quickly.

Another model could look like having two people's agents enter the secure environment and duke it out in front of a panel of judges and classifiers that eventually coalesce around a suggestion.[^4] If we can build something like this, we could practice solving these kinds of trust and coordination and negotiation problems in a way that might be useful for hard coordination around AI safety in the future. I might write more about this soon.

[^1]: Just in case it doesn't come through in this piece, I think this is probably conditioned on the bad x-risk thingy not happening in the next ~2 years.

[^2]: I haven't yet decided whether I'm going to do code quotes (Kenobi said "Hello there".) or standard English grammar quotes ("Kenobi said "Hello there.") and may make arbitrary choices for fun and glory until I figure out which impulse wins out.

[^3]: I should also investigate what online dispute resolution is - it seems like another alternative to the expense of in-person arbitration in some settings?

[^4]: This general thought is inspired by but lower quality than existing discourse in the AI safety community that I loosely remember encountering from the likes of Wei Dai, Andrew Critch, Scott Alexander, Allan Dafoe, etc.