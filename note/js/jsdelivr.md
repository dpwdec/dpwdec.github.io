---
title: jsdelivr
layout: page
exclude: true
---

Jsdelivr is an "open source CDN" that allows you to remotely load Javascript into a browser, it can load this code **directly from any public github repo** and allows you to quickly get scripts into websites. This is useful because loading in `src` code from Github source files is blocked by default with a set of headers. For example you could not use the following link `https://raw.githubusercontent.com/dpwdec/sketch_visualisations/master/sine_ratio/sine_ratio.js` to load Javascript into a page as a `<script>` source, even if you *can* view the code manually.'

Jsdelivr also seems quite opinionated about what it *will* work with, for example, I was not able to get it to load HTML code as the `src` for an `iframe` element. Instead it just displayed the raw html content as text. Presum
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTM0MjM3ODUxOCwtMjI3NTkwNTAxXX0=
-->