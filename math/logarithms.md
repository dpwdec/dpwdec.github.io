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

## Natural Logarithms and E

A **natural logarithm** asks what the special exponential constant \\( e \\) needs to be raised by to equal the natural logs result. For example, \\( ln2 \\) is the same as \\( log_e 2 \\).

You can **write a number is terms of \\( e \\)** by raising e to the natural log of that number. Such as \\( e^{ln2} = 2 \\), which just says that "raise \\( e \\) to what you need to raise \\( e \\) by to get 2."

\\[ e^{ln64} = 64 \\]
\\[ e^{ln2.334} = 2.334 \\]
\\[ e^{ln\pi} = \pi \\]

## Division Using Logarithms

You can **translate division into logarithms and use subtraction instead**. This has the effect of compressing large numbers into much more computable ranges that only require addition and subtraction to work with. 

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEyMzM2MTEyMTMsLTIxNjA0NjI3NV19
-->