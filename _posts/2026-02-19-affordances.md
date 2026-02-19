---
layout: post
title: "affordances"
date: 2026-02-19
---

*epistemic status: low effort post just to get something out today*

The importance of reasoning through precisely which affordances to grant the red and blue teams in our control settings has risen sharply in our work over the last week.

I initially tried to write down affordances according to which side they favored, but realized that that would end up with a lot of duplicated content (e.g. "Red team affordance: hidden scratchpad" vs. "Blue team affordance: visible scratchpad"). So now I'm just going to YOLO some affordance categories (?) and see how it goes.

Capability:
- General capability gap between red and blue (e.g. gpt-2 monitoring claude-opus-4-6 vs. claude-opus-4-6 monitoring itself)
- Tools given to red (can it run code? can it search stuff? write to a system? make api calls? spawn other agents? do lots of stuff at a time without intervention?)
- Tools given to blue (can blue resample/edit/completely replace a suspicious action? can it stop a suspicious action? can it interrogate red about an action?)

Information:
- Blue knowing exactly what it's looking for (did we tell blue about the specific side task or not?)
- Red knowing exactly what defensive protocol is being deployed against it (is red never surprised by a blue technique?)
- Hidden scratchpad (can blue see the scratchpad tool use or not?)
- Hidden internal chain of thought (can blue see literally all output tokens from red or not?)

Statefulness:
- Stateful blue (it has long-context memory, RAG capabilities, etc.)
- Stateless blue (red can iterate against blue without harming its ability to try again)
- Stateful red (it also has long-context memory that is un-auditable by blue)
- Stateless red (red is replaced/mind wiped/resampled frequently to break long-term coherence)

Budget:
- Blue's budget (can it always invoke an expensive but effective system e.g. expert human review or is it limited to only cheap techniques e.g. probes and offline LM monitors)
- Red's budget (is it token constrained (either input or output)? API usage constrained?)

Collusion:
- How trustworthy blue's agents are (do they secretly collude with red?)
- How many red agents there are (can two red agents collude with each other either in parallel with shared state or sequentially with inherited state?)

Reversibility:
- Red's ability to do irreversible shit that can't be rolled back or stopped even if caught offline post hoc (e.g. exfiltrate weights)
- Blue's ability to grant conditional permission to a red rollout but sandbox or silo it to isolate side effects (can blue let red try the thing but in a locked-down environment?)

Performance: <- maybe the most important one for frontier labs?
- Blue's willingness to leave red performance on the table to increase safety (where on the safety-usefulness curve are we?)
- Red's willingness to leave red performance on the table to avoid showing its full capabilities/true colors in an eval (SANDBAGGING!)

As I keep working, I might add to this list/refine it more. But I think this is a reasonable place to start.

Thanks to Ayush Panda and Atharva Nihalani for the conversation that inspired this piece. Thanks also to the Redwood Research team in general. I'm sure their ideas on control permeate this piece, and would like to gesture broadly at their work for more thought-out work on this theme.