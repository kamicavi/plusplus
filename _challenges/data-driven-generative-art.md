---
badge: Intermediate p5.js
published: true
theme: audio
number: 2
excerpt: Data + code = digital delights
level: Intermediate
mentors:
  - Charlotte
  - Ewan
tags:
  - digital art
  - p5js
  - arduino 
  - microcontroller
  - sensor
  - audio
  - generative art
  - data
  - animation
  - javascript
title: Data-driven Generative Art
sidebar: true
header:
  teaser: /assets/images/intermediate.png
---
Building on the [Generative Art]({{ "/challenges/generative-art/" | absolute_url }}) challenge, you should now add an extra ingredient to your p5.js artwork. As well as using random numbers to achieve unpredictability, use an external data source to help make your images. Ideally, this external data source should contain a lot of variation and perhaps also some randomness. Examples might be:
* digitized audio
* sensor data from a microcontroller (e.g., Arduino)
* an API that streams data, such as Twitter or [a weather API]({{ "/challenges/weather-forecasting/"}}).

This challenge overlaps with the more familiar task of data visualisation. But there's an importance difference. Data visualisation usually tries to inform the viewer. But your program should delight your audience by appealing to their imagination and sense of fun.

## Resources

### Getting API data into p5.js

* [Example from p5.js reference of getting data via an API](https://p5js.org/reference/#/p5/httpGet)
* [General discussion about external APIs in JavaScript](https://www.youtube.com/playlist?list=PLRqwX-V7Uu6YxDKpFzf_2D84p0cyk4T7X)


### Music/audio visualization

* [Visualizing Music with p5.js](https://therewasaguy.github.io/p5-music-viz/)
* [Make a Music Visualization](https://codeburst.io/p5-js-tutorial-for-beginners-make-a-music-visualization-bb747c4cd402)
* [Music visualization with p5.js](https://www.youtube.com/watch?v=00kQX4m28IU) -- only provides code for the Processing language (Java).
* [Sound visualisation with The Coding Train](https://youtu.be/2O3nm0Nvbi4)
* [Loading audio into p5js](http://creativecode.dannewoo.com/week-12-audio/)

### Connecting p5.js to a microcontroller

* [p5.j5](https://github.com/monteslu/p5.j5) interfaces with Arduino boards
* [p5.serialport](https://github.com/p5-serial/p5.serialport) connects p5.js to the serial port on your computer
* [Pi Art](https://github.com/alphydan/piArt) connects a RPi sense-hat to p5.js
* [p5.js and Arduino serial communication](https://youtu.be/feL_-clJQMs)





