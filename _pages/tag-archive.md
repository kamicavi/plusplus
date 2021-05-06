---
permalink: /tags/
layout: tags
classes: wide
title: Challenges by Tag
---


{% include collect-tags.html %}


<p>
{%- for tag in tags -%}
  <a href="#{{ tag | slugify }}" class="page__taxonomy-item" rel="tag">{{ tag }}</a>
{%- endfor -%}
</p>

<hr/>

{% for tag in tags %}

<div class="feature__wrapper">
    <h3 id="{{ tag | slugify }}">{{ tag }}</h3>
    <div class="entries-grid">
        {%- for post in site.challenges -%}
          {% if post.tags contains tag %}
            {% include myarchive-single.html %}
          {% endif %}
        {%- endfor -%}
    </div>
</div>

{% endfor %}
