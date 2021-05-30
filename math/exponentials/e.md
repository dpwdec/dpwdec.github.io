---
title: E
layout: page
exclude: true
---

<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>

The constant \\( e \\) or **Euler's number** is an irrational constant that represents the maximum exponential growth of system with a continuous compounding rate of 100%. This can then be taken as a *base rate* for all exponential systems and multiplied or divided to derive other exponential growth rates.

## What is E?

The simplest way to illustrate *what* \\( e \\) is, can be done using interest rates as an example.

If we have a bank account that returns \\( 100% \\) annualised compound interest we can calculate the rate of the money we will get after one year has passed as

\\[ new\ money = current\ money \times (1 + rate) \\]

Where \\( rate \\) is \\( 1 \\), this is a trivial calculation that results in simply multiplying the money at the end of a year by \\( 2 \\) to find the return. So, if we start with \\( 1円 \\) in our account our total money after one year will be \\( 2円 \\).

At the moment, we're only calculating our interest once per year, however, we can *split* the annualised interest rate calculation across the year into two at the six month mark. To do this we would instead receive two compounding interest payments of \\( 50% \\).

So, if we start with \\( 1円 \\) in our account, we can calculat the interest we recieve at the six month mark as

\\[ money = 1 \times (1 + \frac{rate}{2}) \\]

The rate of \\( 100% \\) is simply \\( 1 \\). So,

\\[ money = 1 \times (1 + \frac{1}{2}) \\]

\\[ money = 1.5 \\]

Then, six months later again, at the one year mark we can calculate this again with the current account balance.

\\[ money = 1.5 \times (1 + \frac{1}{2}) \\]

\\[ money = 2.25 \\]

Magic! By the power of compounding twice in one year instead of once we've ended up with \\( .25 \\) more 円 at the end of year.

This process of *splitting* the period into chunks can be generalised as a calculation about the **total return rate**. That is **what to multiply your starting amount by** as

\\[ growth = (1 + \frac{rate}{period})^{period} \\]

So, if you *split* the year at \\( 100% \\) annualised interest into four chunks you would end up with 

\\[ growth = (1 + \frac{1}{4})^4 \\]

Which is the same as

\\[ (1 + \frac{1}{4})(1 + \frac{1}{4})(1 + \frac{1}{4})(1 + \frac{1}{4}) \\]

\\[ = 2.44140625 \\]

Again we've gained a greater growth rate than when we split the year into only two chunks, however the difference this time is smaller. And, indeed, as you split the year into smaller and smaller chunks the amount you gain for each split gets smaller and converges on a single value.

That value is \\( e \\).

## Maximum Growth

Maximum possible growth exponential growth rate can be calculated as

\\[ maximum\ growth = \lim_{n \to ∞} (1 + \frac{1}{n})^n \\]