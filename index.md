---
title: Des essais
layout: default
---

{% for post in site.posts %}
<div style="margin-bottom: 2em;">
  <a href="{{ post.url | prepend: site.baseurl }}">{{ post.title | upcase }}</a>
  <p>{{ post.excerpt }}</p>
</div>
{% endfor %}