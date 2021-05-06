---
title: "Our Team"
layout: single
permalink: /team/
collection: team
entries_layout: grid
classes: wide
sort_by: title
header:
 image: /assets/images/splash-1660x400.jpg
---


<div class="feature__wrapper">
    <h2 id="mentors">Mentors</h2>
    {% assign mentors = site.team | where: 'role','mentor' | sort: 'title' %}
    <div class="entries-grid">
        {%- for post in mentors -%}
        {% include myarchive-single.html %}
        {%- endfor -%}
    </div>
</div>


<div class="feature__wrapper">
    <h2 id="sg">Organisers</h2>
    {% assign sg = site.team | where: 'role','sg' | sort: 'title' %}
    <div class="entries-grid">
        {%- for post in sg -%}
        {% include myarchive-single.html %}
        {%- endfor -%}
    </div>
</div>