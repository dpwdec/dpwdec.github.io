---
title: Markdown
layout: page
exclude: true
---

You can **set the output port for your jekyll preview server** using `jekyll serve --port 4000`.

## Wrapping markdown in HTML

**By default most markdown compilers will ignore markdown compilation of elements wrapped in HTML elements**, such as a `div`. To indicate to the compiler that you want the elements inside the div rendered you must set the `markdown` element flag to equal `"1"`.
```md
<div markdown="1">
  # some markdown text to be rendered here
</div>
```


<!--stackedit_data:
eyJoaXN0b3J5IjpbMTAxMTI3ODEzMF19
-->