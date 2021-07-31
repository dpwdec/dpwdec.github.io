---
title: Change of Base
layout: page
exclude: true
---
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>

You can **calculate the log in an arbitrary base using the log in another base**. The example below shows calculating the log of \\( x \\) for base \\( b \\) by using the log function for base \\( a \\).

\\[ log_b(x) = \frac{log_a(x)}{log_a(b)} \\]

This can be reformulated as

\\[ log_b(x) \cdot log_a(b) = log_a(x) \\]

## Proof

## Intuition

Remember, when you see the multiplication of two \\( log \\) functions this is equivalent to raising an exponent to another exponent.

For example,

\\[ log_2(16) \cdot log_2(4) = 8 \\]

Is another way of expressing

\\[ (2^4)^2 = 2^{4 \cdot 2} = 2^8 = 256 \\]

Before dealing with the change of base formula itself, first let's consider a more intuitive reformulation of the same change of base using concrete numbers (rather than algebraic expressions).

For example, the following expression shows the relation of the base 8 \\( log )\\ with base 2 \\( log \\). (Although there is nothing intrinsic about the numbers 2 and 8, they just have a nice relationship for purposes of an example.)

\\[ log_8(64) \cdot log_2(8) = log_2(64) \\]

When we see \\( log_2(8) \\) this is the same as saying: *how many times do I have to multiply \\( 2 \\) by itself to get \\( 8 \\)?* The answer is of course 3 times. Which is just

\\[ 2 \cdot 2 \cdot 2 \\]

The same is true for \\( log_8(64) \\). *How many times do I have to multiply \\( 8 \\) to get \\( 64 \\)?* 2 times.

\\[ 8 \cdot 8 \\]

We can therefore, substitute the log expression above into an exponent expression using the logs above. Such that \\( 2 \cdot 2 \cdot 2 \\) replaces \\( log_2(8) \\). It's then multiplied by \\( log_8(64) \\). *Importantly, here, we can't just simply multiply by \\( 8 \cdot 8 \\) because, as we established above, when you multiply exponents, as in the case of \\( log \\) expressions. This is the same as raising an exponent to another exponent.*

So, because \\( 2 \cdot 2 \cdot 2 = 8 \\) we can express \\( log_8(64) \\) as the \\( log_2(8) \\) expressions multiplied by itself.

\\[ (2 \cdot 2 \cdot 2) \cdot (2 \cdot 2 \cdot 2) = 64 \\]

By first finding out what we need to raise our actual base to (2) to get our desired base (8) we have shown as relation between these two bases. But also, from the expression above it becomes clear that we are actually multiplying \\( 2 \\) six times by itself, or just \\( 2^6 \\). This explains why the exponent multiplication is equal to actually base of the target result (64).

In summary

\\[ (2^3)^2 = 8^2 = 64 = 2^{3 \cdot 2} = 2^6 \\]

By working with the log exponents we can see that by taking products of the exponents - which is actually raising an exponent *to* another exponent we can create values as *composites* of exponential functions described by their logs.

This entire idea can **be restated algebraically as**

\\[ log_b(x) \cdot log_a(b) = log_a(x) \\]

Now, to get into the main issue of the **change of base** formula. The above expression that we started with

\\[ log_8(64) \cdot log_2(8) = log_2(64) \\]

This can be easily re-arranged to be into the change of base form.

\\[ log_8(64) = \frac{log_2(64)}{log_2(8)} \\]

If we didn't actually easily know the result of \\( log_8(64) \\) we could easily compute it using the fraction on the right side of the equation.

\\[ \frac{6}{3} = 2 \\]

Again, this makes sense because *any* log can be just broken down into any product. Here we're saying given that I know \\( 2^6 = 64 \\) what products can I break down the exponent of \\( 6 \\) in base \\( 2 \\) such that one those products is the new base.

This can be made even clear with a larger exponent that is more amenable to being easily broken up. Take for example

\\[ 2^12 = 4096 \\]

Which can be re-written as

\\[ (2^2)^6 \\]

Therefore

\\[ log_2(4096) = 12 \\]

\\[ log_4(4096) = \frac{log_2(4096)}{log_2(4)} \\]

\\[ \frac{12}{2} = 6 \\]

So

\\[ 4^6 = 4096 \\]

By dividing the exponent of the original base (2) by the amount that gives you the new base (4) you can then work out what you need to do raise the new base to, to get the target number we're trying to compute the \\( log \\) of in this new base.

We can do this with almost any value

\\[ 2^12 = 4096 \\]

\\[ (2^3)^4 = 4096 \\]

\\[ log_8(4096) = \frac{log_2(4096)}{log_2(8)} \\]

\\[ \frac{12}{3} = 4 \\]

Or something quite arbitrary that is less easy to compute arithmetically

\\[ log_5.2(4096) = \frac{log_2(4096)}{log_2(5.2)} \\]

\\[ \frac{12}{2.37851162325} = 5.0451718977 \\]

\\[ (2^{2.37851162325})^{5.0451718977} = 4096 \\]

Essentially for any arbitrary value that wish to find the log of a value for, taking the log of it in the old base will return some value that is the amount that you need to raise it the old base to get to that value. Then dividing the log of the thing you want to calculate in the old base is like doing the reverse of that, you find what the multiplier would be if you just raise the old base to equal the new base.

As an addendum, here is an example that makes use of exponents directly instead of using logs and is just another restatement of the ideas outlined above but as an attempt to make the relationship between logs and exponents clearer. 

In the example below, \\( a \\) is the base that we can compute, \\( x \\) is the exponent to raise \\( a \\) to get our target base \\( b \\), \\( y \\) is the exponent to raise \\( b \\) to our target amount and \\( z  \\) is the exponent to raise \\( a \\) to our target amount.

\\[ (a^x)^y = a^z \\]

It follows that

\\[ x \cdot y = z \\]

And, if we know \\( z \\) and \\( x \\) the 

\\[ y = \frac{z}{x} \\]