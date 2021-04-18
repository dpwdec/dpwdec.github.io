---
title: Quotient Rule
layout: page
exclude: true
---

<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>

The **quotient rule** can be used to take the derivative of two functions that are divided by each other. It is stated as

\\[ (\frac{u}{v})' = \frac{u'v - v'u}{v^2} \\]

## Proof

You can **prove the quotient rule** by substituting into the standard change in x formula that gives the derivatives for all differentiable functions.

\\[ \frac{\frac{u(x + \Delta x)}{v(x + \Delta x)} - \frac{u(x)}{v(x)}}{\Delta x} \\]

This is complicated expression, so the first step is to simplify the numerator by isolating it as

\\[ \frac{u(x + \Delta x)}{v(x + \Delta x)} - \frac{u(x)}{v(x)} \\]

We can then add in a \\( u(x) \\) and \\( -u(x) \\) to the first term of the expression resulting in a change of \\( 0 \\) but giving us more terms to work with, similar to the approach with the product rule proof.

\\[ \frac{u(x) + u(x + \Delta x) - u(x)}{v(x) + v(x + \Delta x) - v(x)} - \frac{u(x)}{v(x)} \\]

The expression is again becoming very complicated so we can simplify it again by defining some intermediary variables. These will be \\( u \\), \\( v \\), \\( \Delta u \\) and \\( \Delta v \\). They will mean

\\[ u = u(x) \\]

\\[ v = v(x) \\]

\\[ \Delta u = u(x + \Delta x) - u(x) \\]

\\[ \Delta v = v(x + \Delta x) - v(x) \\]

Substituting in again, we get a new expression, written in terms of variables. *Don't forget, you an always expand these variables to return to the expressions written in terms of \\( x \\).*

\\[ \frac{u + \Delta u}{v + \Delta v} - \frac{u}{v} \\]

We can now **create a common denominator** for the expression by multiplying the denominators together and cross multiplying with the numerators.

\\[ \frac{v(u + \Delta u) - u(v + \Delta v)}{v(v + \Delta v)} \\]

Next **multiply out** the numerator, also called `distribution`.

\\[ \frac{uv + v(\Delta u) - uv + u(\Delta v)}{v(v + \Delta v)} \\]

The \\( uv \\) and \\( -uv \\) cancel.

\\[ \frac{v(\Delta u) - u(\Delta v)}{v(v + \Delta v)} \\]

Now that the numerator is simplified we can use it in our original expression.

\\[ \frac{\frac{v(\Delta u) - u(\Delta v)}{v(v + \Delta v)}}{\Delta x} \\]

Next, bring the divisor out as a multiplier.

\\[ \frac{1}{\Delta x}\frac{v(\Delta u) - u(\Delta v)}{v(v + \Delta v)} \\]

The multiplier can then we applied to a each of the numerator terms.

\\[ \frac{v(\frac{\Delta u}{\Delta x}) - u(\frac{\Delta v}{\Delta x})}{v(v + \Delta v)} \\]

We can now resolve are variables back to their original form.

\\[ \frac{v(x)(\frac{u(x + \Delta x) - u(x)}{\Delta x}) - v(\frac{v(x + \Delta x) - v(x)}{\Delta x})}{v(x)(v(x) + v(\Delta x) - v(x))} \\]

And deal with the divisor, in which the \\( v(x) \\) and \\( -v(x) \\) cancel to give

\\[ \frac{v(x)(\frac{u(x + \Delta x) - u(x)}{\Delta x}) - v(\frac{v(x + \Delta x) - v(x)}{\Delta x})}{v(x)v(\Delta x)} \\]

This now looks very similar to standard derivative definitions are the quotient rule definition. By writing with limits we know that.

\\[ \lim_{x \to 0}  \frac{u(x + \Delta x) - u(x)}{\Delta x} = u'(x) \\]

\\[ \lim_{x \to 0}  \frac{v(x + \Delta x) - v(x)}{\Delta x} = v'(x) \\]

\\[ \lim_{x \to 0} u(x) = u(x) \\]

\\[ \lim_{x \to 0} v(x) = v(x) \\]

\\[ \lim_{x \to 0} v(x + \Delta x) = v(x) \\]

Substituting this into the equation we get

\\[ \lim_{x \to 0} \frac{v(x)v'(x) - v'(x)u(x)}{v(x)v(x)} \\]

Which is equivalent to

\\[ (\frac{u}{v})' = \frac{u'v - v'u}{v^2} \\]

Thus proving the quotient rule.


