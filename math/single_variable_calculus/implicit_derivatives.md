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

## Implicit derivative without substitution

You can **take an implicit derivative of a function** that doesn't require you to subtitute the function for the value of \\( y \\) in the final derivative but instead use the value of \\( y \\) at a point directly. This is confusing as previous work with derivatives explored functions like \\( \frac{d}{dx}x^2 = 2x \\) where a single value for \\( x \\) was plugged into the derivative to find the rate of change at the point, for example at \\( 3 \\) the slope is \\( 6 \\). However, the following example has a derivative in terms of \\( x \\) *and* \\( y \\) so a point in those terms has to substituted to get the value of the slope.

This example uses the function

\\[ y^3 + x^3 = 3xy \\]

It's possible to solve this in terms of \\( y \\) but difficult and messy, so let's just go straight to solving implicitly by taking the deriative of this entire function. Note, that we have to idea what value of \\( y \\) is for this function in terms of \\( x \\).

\\[ \frac{d}{dx}( y^3 + x^3 = 3xy ) \\]

\\[ 3y^2 \frac{d}{dx}y + 3x^2 = 3y + 3x\frac{d}{dx}y \\]

We use the product rule \\( u'v + v'u \\) on the right side of the function. The first \\( x \\) dissapears because \\( (x^1)' = 1 \cdot x^0 = 1 \\) and the quotient always remains when taking the derivative of a non constant term.

Next group the \\( \frac{d}{dx}y \\) terms and \\( x \\) / \\( y \\) terms.

\\[ 3y^2 \frac{d}{dx}y - 3x\frac{d}{dx}y = 3y - 3x^2 \\]

Factorise out of the \\( \frac{d}{dx}y \\).

\\[ \frac{d}{dx}y(3y^2 - 3x) = 3y - 3x^2 \\]

Divide by \\( 3y^2 - 3x \\) to separate the \\( \frac{d}{dx}y \\)

\\[ \frac{d}{dx}y = \frac{3y - 3x^2}{3y^2 - 3x} \\]

The derivative of \\( y \\) is therefore

\\[ \frac{d}{dx}y = \frac{y - x^2}{y^2 - x} \\]

Which gives a function in terms of \\( x \\) and \\( y \\) into which we can substitute values to find the derivative at that point. For example, at point \\( (\frac{4}{3}, \frac{2}{3}) \\) the derivative is

\\[ \frac{
    \frac{2}{3} - \frac{16}{9}
}{
    \frac{4}{9} - \frac{4}{3}
} \\]

\\[ = \frac{6 - 16}{4 - 12} = \frac{5}{4} \\]

We can therefore see that we can solve derivative problems even without ever knowing the value of a function input or output in explicit terms.