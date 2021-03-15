---
title: Reciprocals
layout: page
exclude: true
---

<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>

You can **use the quotient rule \\( \frac{u'v - v'u}{v^2} \\) to compute the derivative of a reciprocal**.

A reciprocal function is in the form \\( \frac{1}{f} \\). So for this \\( u = 1 \\) and \\( v = f \\).

Before substituting into the quotient rule form we find the derivative of \\( u \\) which for \\( 1 \\) is \\( 0 \\) because the derivative of any constant is zero. \\(v \\) is just a general function \\( f \\) so this just \\( f' \\).

Substituting we get

\\[ \frac{0 \cdot v - 1 \cdot v'}{v^2} \\]

\\[ \frac{-v'}{v^2} \\]

We can then bring the \\( v^2 \\) divisor up as a multiplier by raising it to the negative power so that we have

\\[ -v^{-2}v' \\]

This gives a general formula for computing the derivatives of reciprocal functions.

## nx case

The general formula \\( -v^{-2}v' \\) can be applied to derivatives in the \\( x^n \\) format to yield insights about the rule for taking derivatives of an \\( x^n \\) function.

By substituing into the reciprocal formula we see that

\\[ \frac{d}{dx} \frac{1}{x^n} = -(x^n)^{-2}(nx^{n-1}) \\]

Then multiplying out indices is the first term

\\[ = -x^{-2n}(nx^{n-1}) \\]

Using the additive rules that apply when muiltiplying indices we know that \\( x^{-2n} \cdot x^{n-1} \\) is \\( -2n + n-1 \\) and \\( -2n + n = -n \\) so the indices in this expression resolve to \\( -n-1 \\).

So, evaluating the whole expression we get

\\[ = -nx^{-n-1} \\]

The general \\( \frac{d}{dx} x^n \\) formula is \\( nx^{n-1} \\) and as \\( \frac{1}{x^n} = x^{-n} \\) we can show that **formula holds true even for negative powers of \\( n \\)** because if \\( n \\) is negative it simply resolves to \\( -nx^{-n-1} \\) and by applying the quotient rule to generaly reciprocals and then the \\( x^n \\) formula we have shown why.



