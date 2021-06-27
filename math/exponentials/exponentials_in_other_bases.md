---
title: Exponents in bases other than e
layout: page
exclude: true
---

<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>


You can **relate exponential functions that are in bases other than \\( e \\)** using the **natural lograithm**.

\\[ base^x = e^{x \times ln(base)} \\]

## Example

Consider the function \\( 2^x \\). From the graph below we can see that it passes through \\( 2 \\) at \\( x = 1 \\) then \\( 4 \\) at \\( x = 2 \\) and so on. But how does this relate the base 100% compounding rate of \\( e \\)?

<iframe src="https://www.desmos.com/calculator/xoqytgwgnk?embed" width="500" height="500" style="border: 1px solid #ccc" frameborder=0></iframe>

If we consider \\( e^x \\) we know that at \\( x = 1 \\) the graph will pass through, well, \\( e \\) itself, which is \\( 2.7182~ \\). 

This means that the rate at which the graph \\(2^x \\) is changing is less than that of the graph of \\( e^x \\).

We're kind of asking a new question then: **What \\(rate \times time \\) combination to we need to raise \\( e \\) to get the graph to pass through \\( 2 \\) at \\( x = 1 \\) and \\( 4 \\) at \\( x = 2 \\)?**

**What rate can I pick such that a compounding function with \\( e \\) will overlay exactly the graph of \\( 2^ x \\)?**

The answer is the **natural log** of the base you want \\( e \\) to be in.

For \\( 2 \\) this would be \\( 0.6931~ \\).

Essentially then to have a process that compounds with a base of \\( 2 \\), so that, after \\( 1 \\) period the growth is \\( 2 \\) and after \\( 2 \\) periods \\( 4 \\) etc. would be

\\[ e^{ln(2)} \\]

Which is the same as

\\[ e^{0.6931} \\]

Which is the same as a saying, the rate for this process is just \\( 0.6931 \\).

Below is the same graph of \\( 2^x \\) but this time with the \\( e^{x \times ln(2)} \\) overlayed on top of it.

<iframe src="https://www.desmos.com/calculator/tc5a0h5jpj?embed" width="500" height="500" style="border: 1px solid #ccc" frameborder=0></iframe>