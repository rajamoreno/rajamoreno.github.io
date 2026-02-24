---
layout: page
title: Bog
permalink: /blog/
---

<figure style="margin: 0 0 1.5em 0; max-width: 1000px;">
<img src="{{ '/assets/images/ody-314-bog-wreckage.jpg' | relative_url }}" alt="Bog Wreckage by Brian Snoddy" style="max-width: 100%; border-radius: 8px;">
<figcaption style="font-size: 0.75em; color: #666; margin-top: 0.5em;"><em>Bog Wreckage</em>, Brian Snoddy, 2001. From <em>Odyssey</em>, <a href="https://gatherer.wizards.com/OD/en-us/314/bog-wreckage">Wizards of the Coast</a>.</figcaption>
</figure>

Welcome to my [bog](https://en.wikipedia.org/wiki/Bog), where I write random stuff for fun and glory (if you want $$\LaTeX$$, find that under [research](/research/)).

{% for post in site.posts %}
<article style="margin-bottom: 2em;">
  <h2 style="margin-bottom: 0.2em;"><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
  <time style="font-size: 0.85em; color: #666;">{{ post.date | date: "%B %-d, %Y" }}</time>
  <p>{{ post.excerpt | strip_html | truncatewords: 40 }}</p>
</article>
{% endfor %}
