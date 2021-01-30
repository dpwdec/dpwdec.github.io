---
title: Trigonometric Function Derivatives
layout: page
exclude: true
---

<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>

The **derivative of the sine function is the cosine function**.

\\[ \lim_{x \to 0} \frac{d}{dx} sin x = cos x \\]

The **derivative of the cosine function is the negative of the sine funtion**.

\\[ \lim_{x \to 0} \frac{d}{dx} cos x = -sin x \\]


## Algebraic Proof

We can find the derivatives of these trigonometric functions using the \\( f(x)' = \frac{f(x + \Delta x) - f(x)}{\Delta x} \\) formula and substituting in the sine and cosine functions.

### Derivative of sine function

First substitute \\( sin(x) \\) into the derivative formula.

\\[ \frac{d}{dx} sin(x) = \frac{sin(x + \Delta x) - sin(x)}{\Delta x}  \\]

At this point theres not much more we can do algebraically manipulate this expression, so we **use the sum the difference rules** from the **trigonometric identities** to expand the expression.

\\[  \frac{sin(x)cos(\Delta x) + cos(x)sin(\Delta x) - sin(x)}{\Delta x}  \\]

We re-arrange to group the \\( -sin(x) \\) onto the left hand expression so that we can factorise easily.

\\[  \frac{sin(x)cos(\Delta x) - sin(x) + cos(x)sin(\Delta x)}{\Delta x}  \\]

Then factorise into two distinct expressions.

\\[  sin(x)\frac{cos(\Delta x) - 1)}{\Delta x} + cos(x)\frac{sin(\Delta x)}{\Delta x}  \\]

The left hand expression evaluates to \\( sin(x) \cdot 0 \\) which equals \\( 0 \\) and the right hand expression evaluates to \\( cos(x) \cdot 1 \\) which equals \\( cos(x) \\). Therefore the whole expression evalutes to \\( 0 + cos(x) \\). Therefore:

\\[ \lim_{x \to 0} \frac{d}{dx} sin x = cos x \\]

The first expression \\( sin(x)\frac{cos(\Delta x) - 1)}{\Delta x} \\) evaluates to \\( 0 \\) because \\( \lim_{x \to 0} cos(\Delta x) - 1 = 0 \\) because \\( cos(0) = 1 \\) and as the numerator approach \\( 0 \\) the result of the division is *also* \\( 0 \\).

TODO: Add explanation of why \frac{sin(\Delta x)}{\Delta x} goes to 1