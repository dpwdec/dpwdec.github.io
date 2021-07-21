---
title: Natural Logarithm
layout: page
exclude: true
---

<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>

The **natural log** is simply tells you **what number to raise \\( e \\) to so that it equals another number**. This is defined as the **inverse** of \\( e^x \\) because it takes *in* a number and tells you the exponent in relation to \\( e \\).

The **natural log** of \\( 2 \\) is \\( 0.6931 \\). So

\\[ e^{0.6931} = 2 \\]

## Notation

The **natural log is usually written as**

\\[ ln(x) \\]

## Time interpretation

The natural log can be **interpreted as the time that it takes to grow by a specific amount**. For example, if you had an investment compounding at \\( 100% \\) and you wanted to know how long it would take for the investment to grow by \\( 12 \\) times, you could compute this by taking the natural log of \\( 12 \\), or \\( ln(12) \\) which is \\( 2.484~ \\). So it would take almost 2.5 years to get a 12 times increase in your original amount.

The **natural log of \\( 1 \\) is always \\( 0 \\)**. As is the case with *all* logarithmic functions, because whenever you have to raise something to power to equal \\( 1 \\) that power *must* be \\( 0 \\). Using the time interpretation of logs, doing \\( ln(1) \\) is like asking "How long will it take to get to 1 times my starting amount?" - well, you're already at that point, so it takes 0 time.

You can **interpret the natural log of fractional numbers** as returning negative time. Or, what the amount would have been in the past if we reversed the compounding from our current amount. 

For example, if we wanted to find how long ago our current amount was *half* of what it is now, we would use \\( ln(0.5) = -0.693 \\). This means we'd have to go *back* in time by 0.693 to get to half the amount that we currently have. This is because we always start from 1 times our amount - the *whole* amount - and then grow or shrink on our timeline from there.

You can **express fractional natural log functions as the negative reciprocal of the compound**. For example, shrinking by \\( 0.5 \\) is the same as shrinking by \\( 50% \\) or \\( \frac{1}{2} \\). The recriprocal of \\( \frac{1}{2} \\) is \\( 2 \\). So

\\[ ln(0.5) = -ln(2) \\]