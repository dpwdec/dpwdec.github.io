---
title: Rational Exponents
layout: page
exclude: true
---

<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>

You can **take the deriative of functions which use rational exponents** i.e. fractional exponents in the form

\\[ y = x^{\frac{m}{n}} \\]

You can do this by simply applying the \\( nx^{n-1} \\) rule. For example,

\\[ x^{\frac{1}{2}}' \\]

\\[ = \frac{1}{2}x^{-\frac{1}{2}} \\]

## Proof

We can prove this works by considering the general case for rational exponents

\\[ y = x^{\frac{m}{n}} \\]

and then using the chain rule and other derivative rules to prove that taking the derivative of this function is the same as the \\( nx^{n-1} \\) rule.

First, if we can't differentiate the \\( \frac{m}{n} \\) directly we can instead raise both sides of the function to power of \\( n \\) to remove fractional component.

\\[ y^n = (x^{\frac{m}{n}})^n \\]

We then multiply \\( \frac{m}{n} \\) and \\( n \\) to get \\( m \\).

\\[ y^n = x^m \\]

These are now both regular exponents so we can try and implicitly find the derivative of \\( y \\) by taking the derivative of boths sides of the function.

\\[ \frac{d}{x}y^n = \frac{d}{x}x^m \\]

Because \\( y \\) is itself a function that is raised to \\( n \\) we apply the chain rule to it and get \\( ny^{n-1} \\) (the outer function) multiplied by the derivative of \\( y \\) (the inner function). This value \\( \frac{d}{x}y \\) is what we currently don't know and are trying to find! Because that was the original derivative we were trying to take at the very beginning but didn't know how to.

\\[ ny^{n-1}\frac{d}{x}y = mx^{m-1} \\]

By dividing by \\( ny^{n-1} \\) we can isolate \\( \frac{d}{x}y \\) and get

\\[ \frac{d}{x}y = \frac{m}{n}\frac{x^{m-1}}{y^{n-1}} \\]

We can then *subsitute* the value of \\(y \\) as \\( y = x^{\frac{m}{n}} \\) into this equation as it was originally defined in terms of \\( x \\) to remove it completely.

\\[ \frac{d}{x}y = \frac{m}{n}\frac{x^{m-1}}{(x^{\frac{m}{n}})^n-1} \\]

Next we can multiply the exponents \\( \frac{m}{n} \\) and \\( n - 1 \\) in the demominator

\\[ \frac{d}{x}y = \frac{m}{n} \frac{x^{m - 1}}{x^{\frac{m}{n} \cdot n - 1}} \\]

This multiplication is the same as \\( \frac{m}{n} \cdot \frac{n-1}{1} \\) which equals \\( \frac{m(n - 1)}{n} \\)

\\[ \frac{d}{x}y = \frac{m}{n} \frac{x^{m - 1}}{x^{\frac{m(n - 1)}{n}}} \\]

Next we can combine the two parts of the fraction by turning the demominator into a negative exponent.

\\[ \frac{d}{x}y = \frac{m}{n} x^{m - 1 - \frac{m(n - 1)}{n}} \\]

To be able to do fractional division between \\( \frac{m -1}{1} \\) and \\( \frac{m(n - 1)}{n} \\) we can multiply \\( \frac{m -1}{1} \\) by \\( n \\) which results in

\\[ \frac{d}{x}y = \frac{m}{n} x^{\frac{n(m - 1)}{n} - \frac{m(n - 1)}{n}} \\]

Which is the same as

\\[ \frac{d}{x}y = \frac{m}{n} x^{\frac{n(m - 1) - m(n - 1)}{n}} \\]

Then multiply out to

\\[ \frac{d}{x}y = \frac{m}{n} x^{\frac{nm - n - nm + m}{n}} \\]

We simplifies to

\\[ \frac{d}{x}y = \frac{m}{n} x^{\frac{m - n}{n}} \\]

The fractional exponent is equivalent to

\\[ \frac{d}{x}y = \frac{m}{n} x^{\frac{m}{n} - \frac{n}{n}} \\]

And \\( \frac{n}{n} \\) is equivalent to \\( 1 \\) which means this resolves to

\\[ \frac{d}{x}y = \frac{m}{n} x^{\frac{m}{n} - 1} \\]

This is exactly the derivative that is show at the top of this section and is the same as the \\( nx^{n-1} \\) rule, thus proving the rule works even for rational exponents.






