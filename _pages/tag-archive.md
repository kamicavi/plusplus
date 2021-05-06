---
permalink: /tags/
layout: tags
#classes: wide
title: Challenges by Tag
---


{% include collect-tags.html %}


<p>
{%- for tag in tags -%}
  <a href="#{{ tag | slugify }}"> {{ tag }} </a>, 
{%- endfor -%}
</p>

<hr/>

{% comment %}


{% for tag in tags %}
  <h2 id="{{ tag | slugify }}">{{ tag }}</h2>

   {% for challenge in site.challenges %}
     {% if challenge.tags contains tag %}
     {% assign teaser = challenge.teaser %}

<div class="entries-list">
<div class="list__item">
  <article class="archive__item" itemscope itemtype="https://schema.org/CreativeWork">
    {% if  teaser %}
      <div class="archive__item-teaser">
        <img src="{{ teaser | relative_url }}" alt="">
      </div>
    {% endif %}
    <h2 class="archive__item-title no_toc" itemprop="headline">
        <a href="{{ challenge.url | relative_url }}" rel="permalink">{{ title }}</a>

    </h2>
    {% include page__meta.html type=list %}
    {% if post.excerpt %}<p class="archive__item-excerpt" itemprop="description">{{ post.excerpt | markdownify | strip_html | truncate: 160 }}</p>{% endif %}
  </article>
</div>
</div>

{% endif %}
{% endfor %}
{% endfor %}

{% endcomment %}

<div class="entries-list">

{% for tag in tags %}
  <h2 id="{{ tag | slugify }}">{{ tag }}</h2>

   {% for challenge in site.challenges %}
     {% if challenge.tags contains tag %}
      <div class="list__item">
       <h3>
       <a href="{{ challenge.url }}">
       {{ challenge.title }}
       </a>
     </h3>
   </div>
     {% endif %}
   {% endfor %}

{% endfor %}
</div>


<div class="entries-list">

{% for tag in tags %}
  <h2 id="{{ tag | slugify }}">{{ tag }}</h2>
  <ul>
   {% for challenge in site.challenges %}
     {% if challenge.tags contains tag %}
     <li>
     <h3>
     <a href="{{ challenge.url }}">
     {{ challenge.title }}
     </a>
     </h3>
     </li>
     {% endif %}
   {% endfor %}
  </ul>
{% endfor %}
</div>


