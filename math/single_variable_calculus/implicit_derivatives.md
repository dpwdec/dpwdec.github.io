---
title: Implicit Derivatives
layout: page
exclude: true
---

<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>

It is possible to take derivatives of functions where the function that produces an output is *not* explicitly defined.

Consider the equation for a circle

\\[ x^2 + y^2 = 1 \\]

This isn't *really* a function where we can state \\( y \\) in terms of \\( x \\) because it produces an output where each \\( x \\) input has two \\( y \\) outputs. This is because any vertical line for a valid input cuts the circle in two places.

However, we can re-arrange the function to state \\( y \\) *more* explicitly.

\\[ x^2 + y^2 = 1 \\]

\\[ y^2 = 1 - x^2 \\]

\\[ y = \pm\sqrt{1 - x^2} \\]

We can't take a derivative of this because its still not a function because it has two branches - one positive and one negative - however, if we drop the \\( \pm \\) and pick and branch we create a semi-circular segment of the original equation which we *can* differentiate.

\\[ y = \sqrt{1 - x^2} \\]

We've now re-arranged the equation to state \\( y \\) in terms of \\( x \\).

## The explicit approach

First let's **try and take the and we can now take an explicit derivative** of this function (which you should already know how to do) so that we can appreciate the elegance of the implicit solution afterwards.

First re-arrange the function use a rational exponent:

\\[ y = (1 - x^2)^{\frac{1}{2}} \\]

Then apply the **chain rule** to take the derivative of the function.

\\[ y' = \frac{1}{2}(1 - x^2)^{-\frac{1}{2}}\cdot-2x \\]

\\[ y' = -x(1 - x^2)^{-\frac{1}{2}} \\]

Turn the now negative rational exponent into a fractional function with a square root

\\[ y' = \frac{-x}{\sqrt{1 - x^2}} \\]

When static \\( y \\) explicitly above we found that \\( y = \sqrt{1 - x^2} \\) which is the demominator of this derivative. So it can be re-written as

\\[ y' = \frac{-x}{y} \\]

This explicitly solves the derivative.

## The implicit approach

The above approach required a lot of re-arranging and deciding on branches of original equation to take the derivative of to come to final answer. Instead, we can **take the derivative of the original equation directly** and *implicitly* take the derivative of \\( y \\) in terms of \\( x \\) in the process.

First, **take the derivative of sides of the equation**.

\\[ x^2 + y^2 = 1 \\]

\\[ \frac{d}{dx}(x^2 + y^2) = \frac{d}{dx}1 \\]

Apply the sum rulke to take the derivative of each of the terms in the left side of the equation

\\[ \frac{d}{dx}x^2 + \frac{d}{dx}y^2 = \frac{d}{dx}1 \\]

In this case the derivative of \\( x^2 \\) and \\( 1 \\) are easy. They equal \\( 2x \\) and \\( 0 \\) respectively. But *how do we deal with the second variable \\( y \\) in this situation?* We treat the extra variable as a function expressed in terms of \\( x \\) which we wrote out above. Every time you see \\( y \\) in the equation it actually implicitly stands for its definition in terms of \\( x \\) as \\( y = \sqrt{1 - x^2} \\). If that's the case then we can just treat it as a nested function which means \\( y^2 \\) just means raising a function called \\( y \\) to power of \\( 2 \\) and so we can simply apply the chain rule here with the caveat that we don't yet *know* what the derivative of \\( y \\) is so we just state it as \\( y' \\) or \\( \frac{d}{dx}y \\) to stand in for the unknown derivative.

\\[ 2x + 2y\cdot\frac{d}{dx}y = 0 \\]

Now we want to re-arrange this derivative to be in terms of \\( \frac{d}{dx}y \\) to solve for that and give us the actual derivative that we wanted all along.

\\[  2y\cdot\frac{d}{dx}y = -2x \\]

\\[ y\cdot\frac{d}{dx}y = -x \\]

\\[ \frac{d}{dx}y = \frac{-x}{y} \\]

This solves the derivative of \\( y \\) implicitly with much less headache the original explciit approach where we had to re-arrange the original equation and substitute that equation back into the function at the end.