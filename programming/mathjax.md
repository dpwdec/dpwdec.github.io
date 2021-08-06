---
title: Mathjax
layout: page
exclude: true
---

<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>

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

You can **add a square root with a different base** by putting the root in square brackets after the `sqrt` keyword.
```latex
\sqrt[3]{9}
```

You can **typeset the \\( \Sigma \\) or summation notation** with a target above and a base below the \\( \Sigma \\) symbol using the `\sum` elements. Confusingly its *not* the `\Sigma` element as this will treat the \\( \Sigma \\) as an algebraic element that has an exponent or base.
```latex
\sum^{n}_{x}
```

Which produces

\\[ \sum^{n}_{x} \\]

The incorrect way is
```
\Sigma^{n}_{x}
```

Which produces

\\[ \Sigma^{n}_{x} \\]