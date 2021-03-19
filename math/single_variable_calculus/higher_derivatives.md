---
title: Higher Derivatives
layout: page
exclude: true
---

<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>

A higher derivative just means **taking the derivative of the derivative**.

For example, the **first derivative** of \\( x^4 \\) is \\( 4x^3 \\). The **second derivative** means taking the derivative *of* the first derivative (\\( 4x^3 \\)) giving \\( 12x^2 \\).

You can **write higher derivatives** using the \\( D \\) character before the function. For example, the fourth derivative of a function can be written as

\\[ D^4f \\]

Higher derivatives are also sometimes written using bracketed syntax as

\\[ (\frac{d}{dx})^n f \\]

## nth Derivative of x to n

We can use mathematical induction to compute the \\( nth \\) derivative of \\( x^n \\).

If you take the first derivative of \\( x^n \\) it would be

\\[ D^1 x^n = nx^{n-1} \\]

The second derivative would be

\\[ D^2 x^n = n(n - 1)x^{n-2} \\]

The third derivative would be

\\[ D^3 x^n = n(n - 1)(n - 2)x^{n-3} \\]

Following the pattern eventually we would be reach \\( x^{n-n} \\) the derivative of which would equal \\( 1 \\) because \\(x^0 = 1 \\). 

The exponent for the step before this would be \\( 1 \\) because \\(x^{n-(n-1)} = x^1 \\).

The exponent for the step before that would be \\( 2 \\) because \\(x^{n-(n-2)} = x^2 \\).

This means we can see that any \\( nth \\) derivative of \\( x^n \\) will eventually converge to an exponent of \\( 2 \\) then \\( 1 \\) then \\( 0 \\) at which point the \\( nth \\) derivative has been reached, for any \\( x^n \\) we will eventually reach a point at which the \\( nth \\) derivative and the power of \\( x \\) cancel.

This can stated as

\\[ D^n x^n = n(n - 1)(n - 2) \cdot \cdot \cdot 2\cdot1)1 \\]

The finally number \\( 1 \\) at the end is the result of \\( x^0 \\) when \\( x^{n-n} \\) is reached.

This is equivalent to \\( n! \\) or \\( n factorial \\).

It's important to note that this only computes the \\( nth \\) derative of \\( x^n \\) this means that the \\( n \\) values must be equal for this proof to work. This can't compute an arbitrary derivative for \\( x^n \\).

## General power of x rule

We can find a general rule for computing any \\( kth \\) derivative of \\( x^n \\) where \\( k \\) and \\( n \\) can be different values (unlike the rule above).

This can be stated using \\( D \\) syntax as \\( D^k x^n \\) where we want to find the \\( kth \\) derivative.

We can do this by simply by finding the difference of the \\( nth \\) derivative (which we defined above) and the \\( kth \\) derivative.

\\[ \frac{n!}{(n-k)!} \\]

This rule even works for the \\( nth \\) derivative because if \\( n \\) and \\( k \\) are equal then \\( n - k = 0 \\) and \\( 0! = 1 \\) and therefore

\\[ D^n x^n = \frac{n!}{0!} \\]

\\[ \frac{n!}{1} = n! \\]

which is the same as the specific rule we derived above.