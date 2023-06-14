---
layout: page
title: teaching
permalink: /teaching/
description: Here is the list of the courses that I have taught so far. Each course has its own teaching materials created by me. Currently, these materials are in Turkish, but they will be converted into English soon.
nav: true
nav_order: 2
horizontal: false
---

<!-- pages/projects.md -->
<div class="projects">

<!-- Display projects without categories -->
  {%- assign sorted_projects = site.teaching | sort: "importance" -%}
  <!-- Generate cards for each project -->
  {% if page.horizontal -%}
  <div class="container">
    <div class="row row-cols-2">
    {%- for project in sorted_projects -%}
      {% include projects_horizontal.html %}
    {%- endfor %}
    </div>
  </div>
  {%- else -%}
  <div class="grid">
    {%- for project in sorted_projects -%}
      {% include projects.html %}
    {%- endfor %}
  </div>
  {%- endif -%}
</div>
