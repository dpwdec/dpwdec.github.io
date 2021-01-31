---
title: Limits
layout: page
exclude: true
---

<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>

A limit describes the process of approaching a point on a graph with a particular value.

There are two types of limits, **right-hand limits** which approach from the right on the number line and **left-hand limits** which approach from the left. It is important to note that it is the \\( x \\) that is moving with respect to \\( x_0 \\) which remains fixed.

The **right-hand limit** is written with a plus above the value which \\( x \\) is approaching.

\\[ \lim_{x \to x_0^+} \\]

For a **right-hand limit** \\( x > x_0 \\) is always true.

The **left-hand limit** is written with a minus above the value which \\( x \\) is approaching.

\\[ \lim_{x \to x_0^-} \\]

For a **right-hand limit** \\( x < x_0 \\) is always true.

The right and left hand limits are **denoated by the letters** \\( R \\) and \\( L \\).

For a discontinuous function like 

\\[
    f(x) =
\begin{cases}
x + 1, &   x > 0 \\\\ -x + 2, & x < 0
\end{cases}
\\]

For a right-hand limit at \\( 0 \\) the limit would approach \\( 1 \\) but the left-hand limit at the same point would approach \\( 2 \\) because of the discontinuousnature of these equations. The **difference of limit from each side is what makes this function discontinuous**.

## Continuity

A function is **continuous** *if*:

\\[ \lim_{x \to x_0}f(x) = f(x_0) \\]

There are **three key requirements to this**. 

1. That limit for \\( L \\) and \\( R \\) (Left and Right limits) exists and that the **left and right limits are equal**.

2. \\( f(x_0) \\) is defined.

3. Both the limit and the function of \\( x_0 \\) are equal the same thing.

Its important to note that even though the function of \\( x \\) and the limit are equal to the same thing they are **not the same thing**, they are different processes of arriving at the same value.
