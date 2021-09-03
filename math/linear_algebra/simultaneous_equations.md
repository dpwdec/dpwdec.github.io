---
title: Simultaneous Equations
layout: page
exclude: true
---

<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>

Simultaneous equations act as an entry point for understanding problems in linear algebra.

These equations have multiple unknown values that we want to solve. Solving a linear equation means finding a point at which a system of equations intersect. GIVE EXAMPLE

Importantly, it is the *co-efficients* of the unknowns in different equations that describe how the equations behave. For example, in the well known form \\( y = mx \\) the \\( m \\) describes the actual character of the equation. Modifying \\( m \\) modifies the gradient.

To **solve a system of equations with \\( n \\) unknowns requires at least \\( n \\) number of equation**. So to solve a system of three dimensional equations \\( x + y + z = m \\) requires at least three equations.

# Two Unknowns

A system of linear equations with two unknowns (namely \\( x \\) and \\( y \\)) can be stated as

\\[ ax + by = m \\]

\\[ cx + dy = n \\]

## Parallel Lines

You can **show that a system of two dimensional linear equations has a solution** *if* **the gradient of the two equations is different**. For the system of equations

\\[ ax + by = m \\]

\\[ cx + dy = n \\]

A solution exists if

\\[ ad - bc \notequal 0 \\]


If the gradient was the same it would mean that the lines are **parallel** and would never meet. Therefore there would be solution.

To show this **convert the standard form of the equations into *y intercept form*** by dividing by the associated co-efficient of \\( y \\) and subtracting the \\( x \\) term.

\\[ \frac{ax + by = m}{b} \\]

\\[ \frac{cx + dy = n}{d} \\]

\\[ \frac{a}{b}x + y = \frac{m}{b} \\]

\\[ \frac{c}{d}x + y = \frac{m}{d} \\]

In standard form as

\\[ y = - \frac{a}{b}x + \frac{m}{b} \\]

\\[ y = - \frac{c}{d}x + \frac{m}{d} \\]

Now that the gradient is isolated as \\( \frac{a}{b}x \\) and \\( \frac{c}{d}x \\) respectively it is clear that if \\( \frac{a}{b} = \frac{c}{d} \\) then the lines are parallel and this system of equations does *not* have a solution.

