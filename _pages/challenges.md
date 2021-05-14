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
We have designed a big range of challenges for you, with a wide variety of approaches. We have divided them into five broad themes:
<a href="#gamesdev">Game development</a>, <a href="#webdev">Web development</a>, <a href="#audio">Interactive audio</a>, <a href="#textproc">Text processing</a> and <a href="#dataproc">Data processing</a>.

Within each theme, the challenges are sorted by level of difficulty: **basic**, **intermediate** and **advanced**. The ones at the basic level don't require that you already know anything about that particular theme and are deliberately gentle in terms of the programming involved. 

Don't worry if you choose a challenge that seems a bit too easy. We will have lots of suggestions for making it harder! Also, the basic challenges will help prepare you for an intermediate one.

You can also look at <a href="{{ '/tags/' | relative_url }}">the challenges filtered by tag</a>.

<div class="feature__wrapper">
    <h1 id="gamesdev">Game Development</h1>
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
    <h1 id="audio">Creative coding: audio and images</h1>
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
