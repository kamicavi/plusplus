---
badge: Geospatial analysis
excerpt: Visualise data that has geospatial coordinates by plotting it on a digital
  map
level: Intermediate
mentors:
- Rosalyn
- Jelmer
- Ben
tags:
- geospatial
- mapping
title: Maps are gr8
sidebar: true
header:
  teaser: /assets/images/intermediate.png
---
A surprisingly large amount of data is geospatial. This means that it involves information that can be located on a map of the earth. The simplest kind of information consists of points that have geospatial coordinates such as latitude and longitude. For example, the coordinates (55.951, -3.189) give the approximate location of Edinburgh Castle. The other two main kinds of geospatial data are lines (e.g., the route of the Forth Road Bridge and polygons (e.g., the shape formed by Gyle Shopping Centre).
Doing this challenge involves exploring one or more geospatial datasets and seeing whether you can represent it on a map in an interesting way.

## Example projects
Which areas of Scotland were most strongly in favour of Independence in the last referendum?
How many fast food outlets can you reach in a 15 minute walk?
Which places in Scotland produced the most household waste per head of population?
 

## Resources
* There are lots of geospatial datasets at <a href="https://github.com/awesomedata/awesome-public-datasets#gis" rel="noopener">https://github.com/awesomedata/awesome-public-datasets#gis</a>.
* ONS Geoportal: <a href="https://geoportal.statistics.gov.uk/" rel="noopener">https://geoportal.statistics.gov.uk/</a>
* Weather data: <a href="https://openweathermap.org/api" rel="noopener">https://openweathermap.org/api</a> 
* City of Edinburgh Open Map Data Portal: <a href="https://data.edinburghcouncilmaps.info/" rel="noopener">https://data.edinburghcouncilmaps.info/</a> 
* National Biodiversity Network Scotland: <a href="https://scotland.nbnatlas.org/" rel="noopener">https://scotland.nbnatlas.org/</a>
* Scottish Environmental Protection Agency (SEPA): <a href="https://www.sepa.org.uk/environment/environmental-data/" rel="noopener">https://www.sepa.org.uk/environment/environmental-data/</a> 

For displaying maps on a web page, we recommend the JavaScript mapping library Leaflet.js. Tutorial: <a href="https://www.tutorialspoint.com/leafletjs" rel="noopener">https://www.tutorialspoint.com/leafletjs</a> 

If you don’t want to use JavaScript, there is a Python interface to Leaflet called Folium: <a href="https://python-visualization.github.io/folium/" rel="noopener">https://python-visualization.github.io/folium/</a>. 

If you want to manipulate geospatial data in Python, GeoPandas (<a href="https://geopandas.org" rel="noopener">https://geopandas.org</a>) is great.

Creating isochrone maps in Python (mapping journey time from certain points): <a href="https://geoffboeing.com/2017/08/isochrone-maps-osmnx-python/" rel="noopener">https://geoffboeing.com/2017/08/isochrone-maps-osmnx-python/</a>

