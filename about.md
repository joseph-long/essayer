---
title: About
layout: default
---

<link rel="stylesheet" type="text/css" href="assets/css/about.css">

<table>
{% for platform in site.data.platforms %}
<tr>
  <td>{{platform.name}}</td>
  <td><a target="_blank" rel="noopener noreferrer" href="{{platform.href_fmt | replace: '<handle>', platform.handle}}">{{platform.handle}}</a></td>
</tr>
{% endfor %}
</table>
