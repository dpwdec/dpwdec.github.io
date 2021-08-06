---
title: Natural Logarithm
layout: page
exclude: true
---

<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>

The **natural log** is simply tells you **what number to raise \\( e \\) to so that it equals another number**. This is defined as the **inverse** of \\( e^x \\) because it takes *in* a number and tells you the exponent in relation to \\( e \\).

The **natural log** of \\( 2 \\) is \\( 0.6931 \\). So

\\[ e^{0.6931} = 2 \\]

You can **write a number is terms of \\( e \\)** by raising e to the natural log of that number. Such as \\( e^{ln2} = 2 \\), which just says that "raise \\( e \\) to what you need to raise \\( e \\) by to get 2."

\\[ e^{ln64} = 64 \\]
\\[ e^{ln2.334} = 2.334 \\]
\\[ e^{ln\pi} = \pi \\]

## Notation

The **natural log is usually written as**

\\[ ln(x) \\]

# Time interpretation

The natural log can be **interpreted as the time that it takes to grow by a specific amount**. For example, if you had an investment compounding at \\( 100% \\) and you wanted to know how long it would take for the investment to grow by \\( 12 \\) times, you could compute this by taking the natural log of \\( 12 \\), or \\( ln(12) \\) which is \\( 2.484~ \\). So it would take almost 2.5 years to get a 12 times increase in your original amount.

The **natural log of \\( 1 \\) is always \\( 0 \\)**. As is the case with *all* logarithmic functions, because whenever you have to raise something to power to equal \\( 1 \\) that power *must* be \\( 0 \\). Using the time interpretation of logs, doing \\( ln(1) \\) is like asking "How long will it take to get to 1 times my starting amount?" - well, you're already at that point, so it takes 0 time.

You can **interpret the natural log of fractional numbers** as returning negative time. Or, what the amount would have been in the past if we reversed the compounding from our current amount. 

For example, if we wanted to find how long ago our current amount was *half* of what it is now, we would use \\( ln(0.5) = -0.693 \\). This means we'd have to go *back* in time by 0.693 units to get to half the amount that we currently have. This is because we always start from 1 times our amount - the *whole* amount - and then grow or shrink on our timeline from there.

You can **express fractional natural log functions as the negative reciprocal of the compound**. For example, shrinking by \\( 0.5 \\) is the same as shrinking by \\( 50% \\) or \\( \frac{1}{2} \\). The recriprocal of \\( \frac{1}{2} \\) is \\( 2 \\). So

\\[ ln(0.5) = -ln(2) \\]

This time interpretation **does not allow for negative logarithms** because if ask the question "How long would it take for me to get to a negative amount?" In the form, \\( ln(-3) \\), for example, this would be `undefined`, because there is no way you can grow to get a negative amount.

You can **interpret the multiplication of log inputs** as growing for a set amount of time and then growing again. For example, if we want to calculate the time to grow by a factor of \\( 16 \\) we can just use \\( ln(16) \\) but we can also break this down into \\( ln(4) + ln(4) \\). What this means intuitively is that we grow four times for some period and then we grow *another* four times resulting in a total \\( \times 16 \\) growth over two equal time periods.

You can **interpret the division of log inputs** as growing for a set of amount of time and then *shrinking* back in to another amount. The example below is the same as growing the amount for a period until it gets to \\( 2 \\) times its original size and then shrinking until the amount \\( 3 \\) times smaller than that. This makes sense because fractional exponents give you amounts in the past.

\\[ ln(\frac{2}{3}) = ln(2) - ln(3) \\]

## Other Bases

We can **apply the time interpretation to other rates** by reintroducing the idea that \\( rate \\) and \\( time \\) are linked in the exponent of \\( e \\).

For example, \\( ln(10) \\) tells us how long it would take to grow by \\( 10 \\) times at \\( 100% \\) growth rate. So

\\[ ln(10) = 2.3 \\]

Which means that

\\[ e^{2.3} = 10 \\]

Because we know that growth and rate are linked this means that

\\[ e^{1 \cdot 2.3} = 10 \\]

Where \\( 1 \\) in the exponent represents a growth rate of \\( 100% \\).

So, if instead we wanted a growth rate of \\( 2% \\) we could rewrite the exponent as \\( rate \cdot \ time \\) which should equal \\( 2.3 \\).

\\[ 0.02 \cdot \ time = 2.3 \\]

\\[ \frac{2.3}{0.02} = 115 \\]

So it would take 115 years to grow by \\( 10 \\) times at a rate of \\( 2% \\).