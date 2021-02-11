---
title: Trigonometric Function Derivatives
layout: page
exclude: true
---

<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.2.0/p5.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.20/lodash.min.js"></script>

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

But **why does \\( \frac{cos(\Delta x - 1)}{\Delta x} \\) evaluate to \\( 0 \\) but \\( \frac{sin(\Delta x)}{\Delta x}) \\) evaluates to \\( 1 \\)?** Its not immediately clear as it seems like both of them just approach something like \\( \frac{0}{0} \\) which would be \\( undefined \\). The **important intuition here** is the ratios between the denominator and numerator and the rate at which \\( cos \\) and \\( sin \\) approach the respective limits in comparison to \\( \Delta x \\).

In the \\( sin \\) case, both \\( sin(\Delta x) \\) and \\( \Delta x \\) approach zero at the same rate even at very small amounts. For example, \\( sin(0.005) \approx 0.0049999 \\) and \\( \frac{0.0049999}{0.005} \approx 1 \\) there this part of the expression approximates \\( 1 \\) as the \\( \lim_{\Delta x \to 0} \\) but *never* for the actual case of \\( 0 \\).

<iframe frameBorder="0" height=200 srcdoc="<html>
  <head>
    <script src='https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.2.0/p5.min.js'></script>
    <script src='https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.20/lodash.min.js'></script>
  </head>
  <body>
    <div id='sine_ratio'></div>
    <script src='https://cdn.jsdelivr.net/gh/dpwdec/sketch_visualisations/sine_ratio/sine_ratio.js'></script>
  </body>
</html>"></iframe>

In the \\( cos \\) case, \\( \frac{cos(\Delta x - 1)}{\Delta x} \\) and \\( \Delta x \\) diverge. The difference between \\( \Delta x \\) and \\( \frac{cos(\Delta x - 1)}{\Delta x} \\) is large, with **the subtractive numerator function being much much smaller** than the denominator. So when they are divided you get an even more tiny number that gets closer and closer to \\( 0 \\). For example \\( cos(0.001) = 0.9999995 \\) but \\( cos(0.001) - 1 = -4.99999958e-7 \\) an extremely tiny number, while \\( \Delta x \\) is still just \\( 0.001 \\), so, \\( \frac{-4.99999958e-7}{0.001} \\) is *another* tiny number that just gets closer and closer to zero.

<iframe frameBorder="0" height=200 srcdoc="<html>
  <head>
    <script src='https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.2.0/p5.min.js'></script>
    <script src='https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.20/lodash.min.js'></script>
  </head>
  <body>
    <div id='cos_ratio'></div>
    <script src='https://cdn.jsdelivr.net/gh/dpwdec/sketch_visualisations/cos_ratio/cos_ratio.js'></script>
  </body>
</html>"></iframe>

We can also leverage a visual interpretation of the \\( sin(\Delta x) \\) to see why dividing by \\( \Delta x \\) evaluates to \\( 1 \\). In the example below \\( \theta \\) represents the arc length of the circle in radians which, if we view its change as \\( \Delta x \\) has the same relationship with \\( sin(\theta ) \\) as \\( \frac{sin(\Delta x)}{\Delta x} \\). From the visualisation below, we can see that as \\( \theta \\) reaches very small values the line representing \\( sin(\theta) \\) overlaps the arc *almost* exactly and becomes almost equal to it. And, dividing to things that are *almost* equal, *almost* equals \\( 1 \\). With limits we can simply evaluate this to \\( 1 \\).

<iframe frameBorder="0" height="500" width="500" srcdoc="<html>
  <head>
    <script src='https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.2.0/p5.min.js'></script>
    <script src='https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.20/lodash.min.js'></script>
  </head>
  <body>
    <div id='cos_ratio'></div>
    <script src='https://cdn.jsdelivr.net/gh/dpwdec/sketch_visualisations/sine_ratio/sine_ratio_geometry.js'></script>
  </body>
</html>"></iframe>