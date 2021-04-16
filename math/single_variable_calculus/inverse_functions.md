---
title: Inverse Functions
layout: page
exclude: true
---

<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>

You can **use implicit differentiation** to find the derivative of inverse functions.

An inverse function reverses the action of another function such that

\\[ x = f^{-1}(f(x)) \\]

So plugging the result of \\( f(x) \\) into \\( f^{-1}(x) \\) will return the original value of \\( x \\).

You can express this relationship in terms of \\( x \\) and \\( y \\) as

\\[ f(x) = y \\]

\\[ g(y) = x \\]

So \\( f \\) and \\( g \\) are functions that are the **inverse** of one another.

If you were to graph \\( f(x) \\) and \\( g(y) \\) on the same graph it would just be the same line because the \\( f \\) turns \\( x \\) values in \\( y \\) values and \\( g \\) function does the opposite. Instead we want to **exchange the role of \\( x \\) and \\( y \\)** for the purposes of visualisation by plugging the \\( x \\) value into the \\( g \\) function.

For example, if have the function \\( f(x) = \sqrt{x} \\) and the inverse function \\( g(y) = y^2 \\) then plugging in \\( x \\) to \\( g \\) is the same as the reflecting the curse of \\( \sqrt{x} \\) across the line \\(y = x \\). Indeed **any inverse function obeys this reversal across this axis**.

![inverse](/assets/inverse_graph_MIT.png)

This exchange of \\( x \\) and \\( y  \\) is like flipping a fraction where \\( \frac{x}{y} \\) becomes \\( \frac{1}{\frac{x}{y}} \\) which is \\( \frac{y}{x} \\). With simple straight lines like \\( y = 2x \\) it is plain to see that the inverse of this is \\( x = \frac{y}{2} \\) so the gradients of these two lines are \\( 2 \\) and \\( \frac{1}{2} \\) respectively which is just the reciprocal.

If we consider the definition of the derivative is

\\[ \frac{dx}{dy} \\]

Then it seems based on the mirroring of inverse graphs that the inverse derivative should be

[\\ \frac{1}{\frac{dx}{dy}} \\]

\\[ \frac{dy}{dx} \\]

## Proof

We can prove this by using implicit differentiation and the chain rule as well as nesting the inverse function inside the original.

First define the functions.

\\[ y = f(x) \\]

\\[ f^{-1}(y) = x \\]

Next take the derivative in terms of \\( x \\) of \\( f^{-1}(y) \\)

\\[ \frac{d}{dx}(f^{-1}(y)) \\]

This is the same as

\\[ \frac{d}{dx}(x) \\]

Which is equal to \\( 1 \\) because \\( x \\) is just a position on the graph which is a constant and the derivative of a constant is always \\( 1 \\). So

\\[ \frac{d}{dx}(f^{-1}(y)) = \frac{d}{dx}(x) = 1 \\]

If we the take derivative now using the chain rule, we get the derivative of the outer function \\( (f^{-1}(y)) \\) as a derivative in terms of the inner function \\( y \\) or \\( \frac{d}{dy} \\) the derivative **in terms** of \\( y \\). Which is multiplied by derivative of \\( y \\) in terms of \\( x \\).

\\[ \frac{d}{dy}(f^{-1}(y)) \cdot \frac{d}{dx}y = 1 \\]

We can then divide by \\( \frac{d}{dx}y \\) to show that

\\[ \frac{d}{dy}(f^{-1}(y)) = \frac{d}{dx}y = \frac{1}{\frac{d}{dx}y} \\]

Which proves the original conjecture of this proof that derivative of the inverse function in terms of \\( y \\) is simply the derivative of the original function flipped.
