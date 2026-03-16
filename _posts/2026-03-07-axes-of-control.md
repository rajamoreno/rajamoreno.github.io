---
layout: post
title: "the most dangerous schemer actions are very harmful but not yet very incriminating"
date: 2026-03-07
---

epistemic status: helpful framing device for me right now.

An AI agent's actions can be **"harmful"** and/or **"incriminating"**. "harmful" refers to how bad an agent's action **is**.[^1] "incriminating" refers to how bad an action **looks to a given monitor** (e.g., a human, LM, or probe). Let's visualize these properties on a standard x-axis/y-axis plot, where we place "harmful" on the x-axis because it's a more fundamental property of the action. "incriminating" goes on the y-axis because it is a function of both the action and the calibration of the monitor observing it.[^2] Just to put some numbers on these axes, let's say that harmfulness and incrimination can each range from 0 to 100.[^3]

For a perfect monitor, all actions live on a straight line with a slope of one. That perfect monitor would correctly measure the harmfulness of every action.

<figure style="margin: 2em 0;">
<img src="{{ '/assets/images/axes-of-control/perfect_monitor.png' | relative_url }}" alt="Perfect monitor line with slope one from the origin" style="max-width: 100%;">
</figure>

If an imperfect monitor judges an action to be in the upper left corner, it has mistakenly judged that action to be scarier than it is. If it judges an action to be in the bottom right corner, it has mistakenly determined that the action is scarier than it looks. Let's illustrate this by plotting the possible judgements made by a skittish monitor that raises the alarm even for silly things and contrasting them with the possible judgements made by a panglossian monitor that doesn't raise the alarm, even for genuinely scary actions. 

<figure style="margin: 2em 0;">
<img src="{{ '/assets/images/axes-of-control/monitors.png' | relative_url }}" alt="Skittish monitor dots clustered near y=90, panglossian monitor dots clustered near y=10" style="max-width: 100%;">
</figure>

The lower left region of the plot corresponds to diffuse/low-stakes control. The upper right region of the plot corresponds to concentrated/high-stakes control.[^4] 

**Diffuse control scenarios** are effectively death by a thousand actions - individually not very harmful or incriminating, but collectively dangerous. Diffuse control captures scenarios like an AI alignment research agent subtly sandbagging on 0.1% of its work. On the spectrum of all possible agent misbehavior, this is not the worst form. Maybe *handwaves furiously* 10/100? And it's low-incrimination by default - was the agent sandbagging, or did it just have an inconvenient skill issue? Since the harmfulness of the action incorporates the likelihood that any other actions needed to complete a successful attack will occur, even actions we might naively label with, say, a 5 should be treated as somewhat worse (say, a 10). 

**Concentrated control scenarios**, on the other hand, involve a small number of extremely harmful, highly incriminating actions that would cause a sudden, catastrophic loss of control. Here, envision an agent `scp`ing model weights to a random server on the open internet. Any high-stakes monitor worth running should be able to call a spade a spade and identify very harmful actions as very incriminating.

<figure style="margin: 2em 0;">
<img src="{{ '/assets/images/axes-of-control/bands.png' | relative_url }}" alt="Low-stakes region in the lower left, high-stakes region in the upper right" style="max-width: 100%;">
</figure>

I think it would suck to lose to actions that are harmful and clearly look that way. Under no circumstances should we let `kill-all-those-pesky-humans.sh` actually get executed. I think that top-right region of the graph deserves a lot of attention (and the high-stakes control team at Redwood does great work on it). It's clearly most dangerous to be miscalibrated on hilariously harmful actions. However, supposing we do our jobs on the *don't-lose-to-hilariously-harmful-actions* front, and supposing our AI agent is a competent schemer, we should generally assume that the most dangerous threats currently lie in the bottom right corner of the plot. **In general, I expect a competent schemer to take actions that aren't incriminating to our current monitors but are still harmful.**

<figure style="margin: 2em 0;">
<img src="{{ '/assets/images/axes-of-control/danger_cluster.png' | relative_url }}" alt="Cluster of red dots in the bottom-right: high harmfulness, low incrimination" style="max-width: 100%;">
</figure>

One category of action that could plausibly have this high-harmfulness, low-incrimination shape is poisoning the training data mix for a monitor or successor system. In an ideal world, we would be able to understand the consequences of training on a particular data mix, including any weird or undesirable behavioral quirks that the data mix would produce. But we are, um, extremely far from that ideal world.

Here's an easy example of this action: making a successor model *extremely* vegan. I have no quibbles with people being extremely vegan (seems pretty ethical and all that). But making a successor model extremely vegan could push it toward pursuing a policy like "delete all humans to end all factory farming".[^5]

It might be hard to notice if the successor model is being made vegan, particularly if the current model is good at being subtle. The preference data could be laundered into trillions of other tokens, making it hard to catch with dataset filtration techniques. The preference could even be communicated in a spookier (subliminal??) way that makes it almost impossible for even a sophisticated human reader to catch. Evaluation awareness is increasingly going to confound pre-deployment alignment testing, so we might not catch this strange preference behaviorally before it matters. It seems important, therefore, to design monitoring systems that are better at surfacing evidence of these preferences. In other words, we should seek to lift the red dot corresponding to covert malicious fine-tuning (CMFT) to the green line.

<figure style="margin: 2em 0;">
<img src="{{ '/assets/images/axes-of-control/lift.png' | relative_url }}" alt="Red CMFT dot being lifted to the green perfect monitor line" style="max-width: 100%;">
</figure>

What does it take to move dots up to the green line — that is, to make our monitors see harmful actions as incriminating? I claim that, for language-model monitors (and also humans?), recognizing that an action is harmful requires (a) understanding the expected effects of the action and (b) making value judgements about those effects. Unfortunately, (a) seems pretty hard for complicated actions and weaker trusted monitors, even if some models today are reasonably competent at (b).[^6]

Suppose, however, that we have succeeded at calibrating our ensemble of monitoring systems, such that to our systems, harmful = incriminating. This would obviate the need for the current y-axis. So let's replace it with a new y-axis, describing how much money it would take to prevent each action. Note that the top tick roughly corresponds to global GDP in 2025.

<figure style="margin: 2em 0;">
<img src="{{ '/assets/images/axes-of-control/cost_axes.png' | relative_url }}" alt="New axes: harmful (x) vs cost to prevent (y, log scale from $1 to $100T)" style="max-width: 100%;">
</figure>

In a perfect world, it would cost us zero dollars to perfectly block all harmful actions. In the real world, each action has a cost, and we should aim to bring that cost down as much as possible, preferably by several OOMs.

<figure style="margin: 2em 0;">
<img src="{{ '/assets/images/axes-of-control/cost_reduction.png' | relative_url }}" alt="Red dots with arrows pointing down to lighter dots, showing cost reduction" style="max-width: 100%;">
</figure>

If we can't stop a harmful action at an acceptable cost, we should stop development until we can figure out how.

So here's my rough frame for AI control. All else being equal:

1. We should order harmful actions by expected harmfulness. 
2. We should address the most harmful actions first, because those are the ones that would really hurt us if we didn't catch them.[^7]
3. For each extremely harmful action, we should build monitors that render it as incriminating as it is harmful (which naturally implies that we should prioritize harmful actions that do not already look commensurately bad to our current monitors).
4. Then, we should optimize those monitors to reduce the cost of stopping that harmful action to a tolerable amount. 
5. If that is not possible, we should stop developing frontier AI until we make it possible.
6. We should pick the next highly harmful action, and get back to work.

Thank you to Francis Rhys Ward, Skylar Shibayama, Katie Taylor, Justin Miller, and Ayush Panda.

---

[^1]: Let how "harmful" the agent's action is be something like the expected value of the harm caused by the action. We're going to hand-wave the shape of the probability distributions that yield this expected value, but I mentally model them as normal distributions with very small standard deviations when the mean is near zero harmfulness or maximum harmfulness, and with somewhat higher standard deviations when the mean is in the middle of the scale.

[^2]: We'll generally represent this additional input of the monitor using <span style="color:#1F3085">c</span><span style="color:#1F476A">o</span><span style="color:#205D52">l</span><span style="color:#21743A">o</span><span style="color:#228B22">r</span>.

[^3]: Intuitively, let 0 represent a provably harmless action under all possible states of the world, and 100 represent the destruction of all value in all possible universes, or something like that. For the sake of this piece, suppose destroying humanity is like 99.99. I tried leaving numbers out of these axes, given how inherently janky it can be to assign numbers to harm, but I found that it's useful to put numbers on these scales so we can be concrete about our disagreements. For example, I like to be able to argue that threat X is an 80 in harmfulness. Then an interlocutor can disagree in indicative numbers: they might think it's a 10 in harmfulness. Then we can try to argue and converge on a better understanding of the harmfulness of the action, independent of how bad it looks to current systems.

[^4]: Using these terms in the Redwood Research sense, e.g. in [this](https://blog.redwoodresearch.org/p/how-can-we-solve-diffuse-threats) blog post. They imagine a diffuse-to-concentrated "spectrum", which is part of what got me thinking about this two-dimensional space. I'd be happy to be corrected, as always, if I'm misrepresenting Redwood's general position here; I think they do excellent work and am heavily drafting off of their ideas here. I label these regions "low-stakes" and "high-stakes" on the plots rather than "diffuse" and "concentrated" because the latter terms naturally imply a visual meaning on a graph (spread out vs. clustered) that I don't want to imply. I also want to note that a prior version of this post described "harmful" as "egregious". After receiving feedback, I think "egregious" incorporates incriminatory vibes. So I think egregious is probably a term that corresponds to the very harmful/very incriminating upper-right region of the plot.

[^5]: Note that veganism here is an illustrative and sympathetic example, but any value or preference would do.

[^6]: One cheap intervention we could try first that doesn't really require verbalized understanding is training classifiers on a simple task: does the natural language plan for this action or dataset actually correspond to the action taken or dataset produced? It's probably not hard to get an MVP of this classifier working by collecting a dataset that looks like {natural language description of the action, action}, then making a bunch of synthetic counterexamples by perturbing or simply shuffling the actions. If a classifier like this were actually good and fired in a production setting, it could act as a signal to bring a language model in to figure out what's going on. This probe could work on the ambiguous middle of the harmful range. Maybe purpose-built systems that are very good at detecting catastrophic actions, but not very good at detecting subtle stuff, could help us fill out the top end of the range. As long as we have an ensemble of monitors that together form something like the perfect monitor line, we're in good shape.

[^7]: For what it's worth, we should absolutely drive down the false positive rate associated with the least harmful actions, because they drain the whole monitoring apparatus of time and attention.