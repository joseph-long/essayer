---
title: About
layout: base
---

<link rel="stylesheet" type="text/css" href="assets/css/about.css">


{% for platform in site.data.platforms %}
<span class="platform">{{platform.name}}</span>
<a class="handle"
   target="_blank"
   rel="noopener noreferrer"
   href="{{platform.href_fmt | replace: '<handle>', platform.handle}}">
  {{platform.handle}}
</a>
{% endfor %}
