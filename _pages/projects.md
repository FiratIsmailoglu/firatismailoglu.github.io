---
layout: page
title: projects
permalink: /projects/
description: Here is the list of the projects I have been involved in.
nav: true
nav_order: 2
horizontal: false
---
   
<!-- pages/projects.md -->
<div class="projects">
<!-- Display projects without categories -->
  {%- assign sorted_projects = site.projects| sort: "importance" -%}
  <!-- Generate cards for each project -->
  {% if page.horizontal -%}
  <div class="container">
    <div class="row row-cols-2">
    {%- for project in sorted_projects -%}
       {% if  project.course==0 -%}
      {% include projects_horizontal.html %}
        {%- endif -%}
    {%- endfor %}
    </div>
  </div>
  {%- else -%}
  <div class="grid">
    {%- for project in sorted_projects -%}
     {% if  project.course==0 -%}
      {% include projects.html %}
     {%- endif -%}
    {%- endfor %}
  </div>
  {%- endif -%}
</div>
