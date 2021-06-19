---
title: Mathjax
layout: page
exclude: true
---

Mathjax is a javascript library for rendering latex equations in markdown documents. It uses the kramdown library making it automatically compatible with Jekyll.

You can **create bold math symbols** by using `mathbf` flag.
```latex
\mathbf{x = v}
```

To **create a new line** you must use *FOUR* backlashes `\\\\`. This is because Markdown turns all double backslashes into single backslashes, which are then passed to the Mathjax renderer. So writing `\\` for latex new line results in only one `\` backslash, so for a double backslash you need to escape both.
```latex
a + b \\\\
b + a
```