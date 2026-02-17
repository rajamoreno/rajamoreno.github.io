---
layout: page
title: Bog
permalink: /blog/
---

Welcome to my [bog](https://en.wikipedia.org/wiki/Bog), where I write random stuff for fun and glory (if you want $$\LaTeX$$, find that under [research](/research/)).

{% for post in site.posts %}
<article style="margin-bottom: 2em;">
  <h2 style="margin-bottom: 0.2em;"><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
  <time style="font-size: 0.85em; color: #666;">{{ post.date | date: "%B %-d, %Y" }}</time>
  <p>{{ post.excerpt | strip_html | truncatewords: 40 }}</p>
</article>
{% endfor %}
