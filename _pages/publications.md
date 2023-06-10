---

layout: page
permalink: /publications/
title: publications
sections:
  - bibquery: "@article"
    text: "Journal Papers"
  - bibquery: "@inproceedings"
    text: "Conference and workshop papers"
  - bibquery: "@misc|@phdthesis|@mastersthesis"
    text: "Theses"
years: [2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015,2014,2013,2012,2011,2010]
social: true
nav: true
nav_order: 4
---

<div class="publications">

{%- for section in page.sections %}
  <a id="{{section.text}}"></a>
  <p class="bibtitle">{{section.text}}</p>
    <h1> "{{section.text}}"</h1>
  {%- for y in page.years %}

    {%- comment -%}  Count bibliography in actual section and year {%- endcomment -%}
    {%- capture citecount -%}
    {%- bibliography_count -f {{site.scholar.bibliography}} -q {{section.bibquery}}[year={{y}}] -%}
    {%- endcapture -%}

    {%- comment -%} If exist bibliography in actual section and year, print {%- endcomment -%}
    {%- if citecount !="0" %}

      <h2 class="year">{{y}}</h2>
      {% bibliography -f {{site.scholar.bibliography}} -q {{section.bibquery}}[year={{y}}] %}

    {%- endif -%}

  {%- endfor %}

{%- endfor %}

</div>
