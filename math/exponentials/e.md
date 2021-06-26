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

## Varying Growth Time

Why is \\( \sqrt e \\) equal to growth over a period of \\( 0.5 \\) units?

It makes sense because if we imagine that raising the equation \\( 1 + \frac{1}{n} \\) to the power of \\( n \\) is essentially *repeated multiplication* it follows that

\\[ (1 + \frac{1}{n})(1 + \frac{1}{n})(1 + \frac{1}{n})(1 + \frac{1}{n})... \\]

is repeated until we reach \\( e \\).

We can therefore imagine that if we split this single period into two equal periods that take half the time of the original period it would mean that 

\\[ half\ period \times half\ period = e \\]

And therefore a \\( half\ period \\) must be equal to \\( \sqrt e \\).

## Varying Growth Rate

If the *rate* at which a process is compounded is varied this same effect can alos be observed. For example, if the *rate* is set to \\( 50% \\), or \\( 0.5 \\). Such that

\\[ \lim_{n \to ∞} (1 + \frac{.5}{n})^n  \\]

After **two** periods of compounding at a rate of \\( .5 \\) we would have reached a total compound of \\( e \\) which means that

\\[ one\ period\ at\ half\ rate \times one\ period\ at\ half\ rate = e \\]

And therefore a \\( one\ period\ at\ half\ rate \\) must be equal to \\( \sqrt e \\).

## Time and Rate

What these ideas about time and rate ultimately reveal is that **time and rate are merged into a single entity** when combined as an exponent with \\( e \\) in the form \\( e^x \\).

Taking from the examples of *time* and *rate* varying above we can represent them as

\\[ e^\frac{1}{2} \\]

This is the same as \\( \sqrt e \\) which can mean the total result after either:

- One \\( half\ period \\) of compounding, or
- Two periods of compounding at \\( half\ rate \\)

Demonstrating that both time and rate are interchangeable and merged when applied to \\( e \\) *because* \\( e \\) represents a neutral one hundred base rate *and* time from which to manipulate.

We can **summarise the relationship between rate and time as**

\\[ growth = e^{rate \times time} \\]

For example, if we have a rate of \\( 5% \\) or \\( 0.05 \\) return over 10 years we would calculate it as

\\[ growth = e^{0.05 \times 10} \\]

\\[ = e^{0.5} \\]

This is the same as a \\( 50% \\) rate for 1 year, or even a \\( 25% \\) rate for 2 years. You can **combine any growth and time period together with \\( e \\) to calculate the growth rate**.