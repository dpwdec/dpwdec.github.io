---
title: Logarithms
layout: page
exclude: true
---
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>

Logarithms are an **inverse function of exponents** that allow you to express the reverse of that exponential function so as to find the exponent of that function. 

For example, if you have some function \\( v = b^{p} \\) where we know the value of \\( v \\) and \\( b \\) and we want to find \\( p \\). (These letters are chosen because they stands for *value*, *base* and *power* respectively!) You can **take the logarithm of \\( \mathbf{v} \\) in a base of \\( \mathbf{b} \\)** to find \\( p \\). Which is like asking: to what power must I raise \\( b \\) to in order to get \\( v \\)? This is given by \\( p = log_b v \\). This is said as "\\( p \\) is equal to the log of \\( v \\) in base \\( b \\)".

Expressed more formally, this is:

\\[ p = log_b v \text{ is equivalent to } v = b^p\\]


## Basic Examples

**1)** Given the logarithm \\( log_2 16 \\) what power must you raise `2` to, to get `16`?

We know that \\( p = log_2 16 \\) where \\( p \\) is the power we are searching for, and we can re-write this in *exponential form* as \\( 16 = 2^p \\). It's then clear that \\( p \\) must be equal to `4` because \\( 2^4 = 16 \\).

**2)** What is the *real* value of \\( log_4 16 \\)? This is asking for the same thing as the question above.

\\[ p = log_4 16 \text{, so } 16 = 4^p \text{, so } p = 2 \\\\ \text{ therefore: } log_4 16 = 2\\]

## Logarithmic Multiplication

You can **decompose the multiplication of two inputs to a log function** by *adding* the two individual logs together. The log functions must share the same for this to work.

\\[ log_x(a \times b) = log_x(a) + log_x(b) \\]

You can **write any log as a composition of other logs**.

\\[ ln(20) = ln(10) + ln(2) \\]

\\[ log_2(17) = log_2(8.5) + log_2(8.5) \\]

\\[ log_3(10) = log_3(3) + log_3(3 \frac{1}{3}) \\]

## Logarithmic Division

You can **translate division into logarithms and use subtraction instead**. This has the effect of compressing large numbers into much more computable ranges that only require addition and subtraction to work with.

\\[ log_x(\frac{a}{b}) = log_x(a) - log_x(b) \\]

## Diminishing Returns

Logarithmic curves can be used to **model processes that suffer from diminishing returns**.

Looking at the graph of \\( f(x) = log_2(x) \\) we can see that the graph rises sharply at the beginning and then slowly converges to a single value. So each subsequent step on the \\( x \\) axis leads to smaller increase than the last step.

<iframe src="https://www.desmos.com/calculator/jl4nr89fu1?embed" width="500" height="500" style="border: 1px solid #ccc" frameborder=0></iframe>

You can **stretch and squash a logarithmic graph** by changing the base. A smaller base will result in a graph that climbs over a longer period and the reverse is true for a larger base. 

For example, imagine we have a corn crop that yields ~100kg of corn with 5kg of fertilizer. And each additional kilogram of ferilizer has a logarithmic relationship with yield. We could model this curve and relationship as where \\( x \\) is amount of fertilizer.

\\[ yield = log_{1.4}(x) \times 21 \\]

<iframe src="https://www.desmos.com/calculator/ezggudp5va?embed" width="500" height="500" style="border: 1px solid #ccc" frameborder=0></iframe>

The \\( 1.4 \\) base and scalar of \\( 21 \\) are essentially arbitrary and simply make the graph pass through approximately \\( 100 \\) at \\( x = 5 \\). From this we can that going from \\( 5 \\) to \\( 6 \\) kilograms of fertlizer yields a 12 kilogram improvement in yield, however this drops to an improvement of 9 for 7 killograms. By the time we get to 20kg of fertilizer the rate of improvement has dropped to just 3kg of output per 1kg of extra fertlizer.

## Log with Negative Input

You **cannot take the log of a negative number** (without using imaginary numbers) because whenever you raise a positive real number to a power the result must also be positive. Whatever, positive base you have, raising that base to a power whether that be positive, fractional or negative will always result in a real positive number. The possible cases below *always result in a positive number* and this will remain true for any other positive base.

\\[ 2^3 = 8 \\]

\\[ 2^{\frac{1}{3}} = \sqrt[3]2 \\]

\\[ 2^{-3} = \frac{1}{8} \\]

## Negative Bases

The only way you *could* have a log of a negative number is if you also use a negative base. But this results in weird behavior that is not very useful. Any logarithmic function with a negative base would be undefined for any exponent that is a fraction with an even demoninator because that would been taking the square root of that number. For example \\( -2^{\frac{a}{b}} \\) is that same as \\( \sqrt[b]{-2}^a \\) and if \\( b \\) equals \\( 2 \\) then we would have to take the root of a negative number which is undefined.