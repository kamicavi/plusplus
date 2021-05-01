---
layout: single
title: Challenges
permalink: /challenges/
classes: wide
header:
 image: /assets/images/splash-1660x400.jpg
# toc: true
# toc_label: "Themes"
# toc_icon: "cat"
# toc_sticky: true
---
# Overview 

We have designed a big range of challenges for you, with a wide variety of approaches. We have divided them into five broad themes:
* <a href="#gamesdev">Games development</a>
* <a href="#webdev">Web development</a>
* <a href="#audio">Interactive audio</a>
* <a href="#textproc">Text processing</a>
* <a href="#dataproc">Data processing</a>

Within each theme, the challenges are sorted by level of difficulty: basic, intermediate and advanced. The ones at the basic level don't require that you already know anything about that particular theme and are fairly gentle in terms of the programming involved. 

Don't worry if you choose a challenge that seems a bit too easy. We will have lots of suggestions for making it harder!

<div class="feature__wrapper">
    <h1 id="gamesdev">Games Development</h1>
    {% assign textproc = site.challenges | where: 'theme','gamesdev' | sort: 'number' %}
    <div class="entries-grid">
        {%- for post in textproc -%}
        {% include myarchive-single.html %}
        {%- endfor -%}
    </div>
</div>
<div class="feature__wrapper">
    <h1 id="webdev">Web Development</h1>
    {% assign webdev = site.challenges | where:'theme','webdev' | sort: 'number' %}
    <div class="entries-grid">
        {%- for post in webdev -%}
        {% include myarchive-single.html %}
        {%- endfor -%}
    </div>
</div>
<div class="feature__wrapper">
    <h1 id="audio">Interactive Audio</h1>
    {% assign audio = site.challenges | where:'theme','audio' | sort: 'number' %}
    <div class="entries-grid">
        {%- for post in audio -%}
        {% include myarchive-single.html %}
        {%- endfor -%}
    </div>
</div>
<div class="feature__wrapper">
    <h1 id="textproc">Text Processing</h1>
    {% assign textproc = site.challenges | where:'theme','textproc' | sort: 'number' %}
    <div class="entries-grid">
        {%- for post in textproc -%}
        {% include myarchive-single.html %}
        {%- endfor -%}
    </div>
</div>
<div class="feature__wrapper">
    <h1 id="dataproc">Data Processing</h1>
    {% assign dataproc = site.challenges | where:'theme','dataproc' | sort: 'number' %}
    <div class="entries-grid">
        {%- for post in dataproc -%}
        {% include myarchive-single.html %}
        {%- endfor -%}
    </div>
</div>
{% comment %}
<!-- modified version of archive-single.html -->
{% if post.header.teaser %}
{% capture teaser %}{{ post.header.teaser }}{% endcapture %}
{% else %}
{% assign teaser = site.teaser %}
{% endif %}
{% if post.id %}
{% assign title = post.title | markdownify | remove: "<p>" | remove: "</p>" %}
{% else %}
{% assign title = post.title %}
{% endif %}
<div class="grid__item">
    <article class="archive__item" itemscope itemtype="https://schema.org/CreativeWork">
        {% if teaser %}
        <div class="archive__item-teaser">
            <img src="{{ teaser | relative_url }}" alt="">
        </div>
        {% endif %}
        <h2 class="archive__item-title no_toc" itemprop="headline">
            {% if post.link %}
            <a href="{{ post.link }}">{{ title }}</a> <a href="{{ post.url | relative_url }}" rel="permalink"><i class="fas fa-link" aria-hidden="true" title="permalink"></i><span class="sr-only">Permalink</span></a>
            {% else %}
            <a href="{{ post.url | relative_url }}" rel="permalink">{{ title }}</a>
            {% endif %}
        </h2>
        {% include page__meta.html type=grid %}
        {% if post.excerpt %}<p class="archive__item-excerpt" itemprop="description">{{ post.excerpt | markdownify | strip_html | truncate: 160 }}</p>{% endif %}
    </article>
</div>
<!-- end modified version of archive-single.html -->
{% endcomment %}
{% comment %}
% assign entries = site[include.collection] %}
{% if include.sort_by %}
{% assign entries = entries | sort: include.sort_by %}
{% endif %}
{% if include.sort_order == 'reverse' %}
{% assign entries = entries | reverse %}
{% endif %}
{%- for post in entries -%}
{%- unless post.hidden -%}
{% include archive-single.html %}
{%- endunless -%}
{%- endfor -%}
{% endcomment %}