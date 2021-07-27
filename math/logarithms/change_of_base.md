---
title: Change of Base
layout: page
exclude: true
---
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>

You can **calculate the log in an arbitrary base using the log in another base**. The example below shows calculating the log of \\( x \\) for base \\( b \\) by using the log function for base \\( a \\).

\\[ log_b(x) = \frac{log_a(x)}{log_a(b)} \\]

## Proof

## Intuition

Remember, when you see the multiplication of \\( log \\) functions this is equivalent to raising exponent to an exponent.

So,

\\[ log_2(16) \cdot log_2(4) = 8 \\]

Which is the same as saying 

\\[ (2^4)^2 = 2^{4 \cdot 2} = 2^8 = 256 \\]

Then let's consider a concrete example related to the change of base above.

\\[ log_8(64) \cdot log_2(8) = log_2(64) \\]

When we see \\( log_2(8) \\) this is saying: *how many times do I have to multiply \\( 2 \\) by itself to get \\( 8 \\)?* Then we apply the exponent of \\( log_8(64) \\) to this value, which is just \\( 8 \\).

\\[ (2^3)^2 = 8^2 = 64 = 2^{3 \cdot 2} = 2^6 \\]

By working with the log exponents we can see that by taking products of the exponents - which is actually raising an exponent *to* another exponent we can create values as *composites* of exponential functions described by their logs.

This can be easily re-arranged to be in the change of base form.

\\[ log_8(64) = \frac{log_2(64)}{log_2(8)} \\]

\\[ 2 = \frac{6}{3} \\]

Again, this makes sense because *any* log can be just broken down into any product.

Here we're saying given that I know \\( 2^6 = 64 \\) what can I products can I break down the exponent of \\( 6 \\) into such that one those products is the new base.

This makes more sense with a larger number

\\[ 4096 = 2^12 \\]

Which can be re-written as

\\[ (2^3)^4 \\]

So

\\[ log_2 4096 = 12 \\]

\\[ log_4(4096) = \frac{log_2(4096)}{log_2(4)} \\]

By dividing by the amount that gives you the new base you can then work out what you need to do raise the new amount to

For example \\( 2^12 \\) can be written arbitrarily as \\( (2^1.2)^10 \\)
