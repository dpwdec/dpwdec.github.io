---
title: Product Rule
layout: page
exclude: true
---

<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>

The **product rule** states that the derivative of two functions that are multiplied together is the **first function multipled by the derivative of the second function, plus the derivative of the first function multiple by the second function**. This can be remembered with the nemonic:

> right d left plus left d right

The derivative is therefore given by:

\\[ g(x)h(x)' = g(x)\frac{dh}{dx} + h(x)\frac{dg}{dx} \\]

or

\\[ u'v + v'u \\]

Examples:

\\[ (4t^{2} - t)(t^3 - 8t^2 + 12)' = \\]
\\[ (4t^{2} - t)(3t^2 - 16t) + (t^3 - 8t^2 + 12)(8t - 1) = \\]
\\[ 20t^4 - 132t^3 + 24t^2 + 96t - 12 \\]

## Proof



## Multiple Products

This **generalises further to finding the derivate of expressions with more than two functions multipled together** so that you take the derivate of each individual function multiplied by the other functions and added together for each combination of functions, in the form:

\\[ g(x)h(x)f(x)' = g(x)'h(x)f(x) + g(x)h(x)'f(x) + g(x)h(x)f(x)' \\]