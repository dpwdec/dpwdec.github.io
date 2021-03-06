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

You can prove that \\( (uv)' = u'v + v'u \\) by using the multiplication of these functions with the \\( \frac{dy}{dx} \\) formula. In the example below I use the functions \\( f \\) and \\( g \\). First we substitute into the change in \\( x \\) formula with the two functions multiplied together.

\\[ \frac{f(x + \Delta x)g(x + \Delta x) - f(x)g(x)}{\Delta x} \\]

We then add by \\( f(x + \Delta x)g(x) \\) and \\( -f(x + \Delta x)g(x) \\) which equals \\( 0 \\) but allows us to group terms together. This results in:

\\[ \frac{f(x + \Delta x)g(x + \Delta x) -f(x + \Delta x)g(x) + f(x + \Delta x)g(x) - f(x)g(x)}{\Delta x} \\]

Next, factorise the resulting terms.

\\[ \frac{f(x + \Delta x)(g(x + \Delta x) - g(x))}{\Delta x} + \frac{ g(x)(f(x + \Delta x) - f(x))}{\Delta x} \\]

Bring the first term of each fraction outside of the divisor to separate them.

\\[ f(x + \Delta x)\frac{g(x + \Delta x) - g(x)}{\Delta x} + g(x)\frac{ f(x + \Delta x) - f(x)}{\Delta x} \\]

We now have the derivative defined in four distinct units: \\( f(x + \Delta x) \\), \\( \frac{(g(x + \Delta x) - g(x))}{\Delta x} \\), \\( g(x) \\) and \\( \frac{f(x + \Delta x) - f(x)}{\Delta x} \\). This format is starting to look suspiciously like \\( u'v + v'u \\). The last piece of puzzle is to define individuals limits for each part of this expression and use the limit sum rule to combine them.

\\[ \lim_{x \to 0} f(x + \Delta x) = f(x) \\]

\\[ \lim_{x \to 0} \frac{(g(x + \Delta x) - g(x))}{\Delta x} = g'(x) \\]

\\[ \lim_{x \to 0} g(x) = g(x) \\]

\\[ \lim_{x \to 0} \frac{f(x + \Delta x) - f(x)}{\Delta x} = f'(x) \\]

So therefore, if we place the limits into the original long form expression

\\[ \lim_{x \to 0} f(x + \Delta x) \lim_{x \to 0} \frac{g(x + \Delta x) - g(x)}{\Delta x} + \lim_{x \to 0} g(x) \lim_{x \to 0} \frac{ f(x + \Delta x) - f(x)}{\Delta x} \\]

By substituting for equivalent expressions defined above we can see that

\\[ = f(x)g'(x) + g(x)f'(x) \\]

Which is the same as \\( (f(x)g(x))' \\) thus proving the product rule.

## Multiple Products

This **generalises further to finding the derivate of expressions with more than two functions multipled together** so that you take the derivate of each individual function multiplied by the other functions and added together for each combination of functions, in the form:

\\[ g(x)h(x)f(x)' = g(x)'h(x)f(x) + g(x)h(x)'f(x) + g(x)h(x)f(x)' \\]

### Visualising the Product Rule

You can **visualise the product rule** using simple geometric shapes. For example, in the case of two functions being multiplied together you can imagine this as a rectangle who's length is given by the first function and who's width is given by the second function. The example below shows a box, the length of which is given by the function `sin(x)` and the height of which is given by `x^2`.

```
┏━━sin(x)━━┓
┏━━━━━━━━━━┓ ┓
┃          ┃ ┃
┃          ┃ x^2
┃          ┃ ┃
┗━━━━━━━━━━┛ ┛
```

If you were to increase `x` slightly you would get 3 new pieces of area: `A`, `B` and `C`.

```
┏━━━━━━━━━━┓ ┏━┓
┃          ┃ ┃ ┃
┃          ┃ ┃A┃
┃          ┃ ┃ ┃
┗━━━━━━━━━━┛ ┗━┛
┏━━━━━━━━━━┓ ┏━┓
┃     B    ┃ ┃C┃
┗━━━━━━━━━━┛ ┗━┛
```

The areas of these different sections are:

\\[ A = \Delta sin(x)x^2 \\]

\\[ B = sin(x)\Delta x^2 \\]

\\[ C = \Delta sin(x) \Delta x^2 \\]

We can ignore `C` because the change of a `Δ` value raised to a power is negligible. That means the whole change of this expression over a tiny `Δx` is the area of `A` plus the area of `B` which is the same as product rule outlined above. So the solution would be:

\\[ cos(x)x^2 + sin(x)2x \\]

This geometric intuition can be **generalised to three dimensions** to implicate what happens with a higher number of functions. In that case you would end up with *three* cuboids that describe the derivative of the function.
