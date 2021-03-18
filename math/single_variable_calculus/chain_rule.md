---
title: Chain Rule
layout: page
exclude: true
---

<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>

The **chain rule** is used for taking the derivative of functions *inside* other functions i.e. derivatives in the domain of **function composition**. For example, the function:


[\\ sin(x^2) \\]

is a **composition** of the two functions (lets call them `g` and `h`):


[\\ g(x) = sin(x) \\]

[\\ h(x) = x^2 \\]

With the function `h` plugged into the `x` input on function `g`.

The **chain rule** states that **the derivative of two composed functions is the derivative of the outer function multiplied by the derivative of the inner function**. So in the example of above this would mean that:

[\\ sin(x^2)' = \\]

[\\ cos(x^2)2x \\]

More generally:

\\[ g(h(x))' = \\]

\\[ g'(h(x))h(x)' \\]

Intuitively this makes sense because **the derivative of a function that takes another funtion** will be **that function's derivative adjusted proportionally by the derivative of the input function**. This is why the input to the derivative of the outer function remains constant, that change is reflected by multiplying the outer function's derivative by that of the inner function, while the input has to remain static for this propertional change of *just* the derivative to take effect.

## Proof

We can prove that taking the derivative of a composition of functions is a product of the derivatives of the individual functions by using some basic algebra. For example if we have the function composition \\( f(g(x)) \\) then the \\( f \\) function's derivative is expressed in terms of a change in \\( g \\) - in other words, a \\( \Delta g \\) and the \\( g \\) function's derivative is expressed in terms of a change in \\( x \\) or \\( \Delta x \\).

So, the derivative we want is \\( f' \\) which can be stated as

\\[ f' = \frac{\Delta f}{\Delta x} \\]

This is algebraically equivalent to the product of the two derivatives

\\[ \frac{\Delta f}{\Delta x} = \frac{\Delta f}{\Delta g} \cdot \frac{\Delta g}{\Delta x} \\]

The two \\( \Delta g \\) numerator and denominator cancel here showing that they are equivalent. Thus proving the chain rule.