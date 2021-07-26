---
title: Product Rule
layout: page
exclude: true
---

<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>

The **logarithmic product rule** states that

\\[ log_x(a \times b) = log_x(a) + log_x(b) \\]

You can **decompose the multiplication of two inputs to a log function** by *adding* the two individual logs together. The log functions must share the same for this to work.

You can **write any log as a composition of other logs**.

\\[ ln(20) = ln(10) + ln(2) \\]

\\[ log_2(17) = log_2(8.5) + log_2(8.5) \\]

\\[ log_3(10) = log_3(3) + log_3(3 \frac{1}{3}) \\]

## Time Interpretation

We can use the **time interpretation of logarithms** to clarify why this is the case.

You can **interpret the multiplication of log inputs** as growing for a set amount of time and then growing again. For example, if we want to calculate the time to grow by a factor of \\( 16 \\) we can just use \\( ln(16) \\) but we can also break this down into \\( ln(4) + ln(4) \\). What this means intuitively is that we grow four times for some period and then we grow *another* four times resulting in a total \\( \times 16 \\) growth over two equal time periods.