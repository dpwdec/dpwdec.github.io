---
title: Simultaneous Equations
layout: page
exclude: true
---

<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>

Simultaneous equations act as an entry point for understanding problems in linear algebra.

These equations have multiple unknown values that we want to solve. Solving a linear equation means finding a point at which a system of equations intersect. For example, the two lines below \\( y = 2x - 2 \\) and \\( y = -\frac{1}{2}x + 5 \\) intersect at point \\( (2, 2) \\) meaning that this is where the *solution* for this system of equations is.

<iframe src="https://www.desmos.com/calculator/fnap4cq2mz?embed" width="500" height="500" style="border: 1px solid #ccc" frameborder=0></iframe>

Importantly, it is the *co-efficients* of the unknowns in different equations that describe how the equations behave. For example, in the well known form \\( y = mx \\) the \\( m \\) describes the actual character of the equation. Modifying \\( m \\) modifies the gradient.

To **solve a system of equations with \\( n \\) unknowns requires at least \\( n \\) number of equation**. So to solve a system of three dimensional equations \\( x + y + z = m \\) requires at least three equations.

# Two Unknowns

A system of linear equations with two unknowns (namely \\( x \\) and \\( y \\)) can be stated as

\\[ ax + by = m \\]

\\[ cx + dy = n \\]

With unique co-efficients indicated by \\( a \\), \\( b \\), \\( c \\) and  \\( d \\).

## Parallel Lines

You can **show that a system of two dimensional linear equations has a solution** *if* **the gradient of the two equations is different**. For the system of equations

\\[ ax + by = m \\]

\\[ cx + dy = n \\]

A solution exists if

\\[ ad - bc \neq 0 \\]

If the gradient of the lines is the same it would mean that the lines are **parallel** and would never meet. Therefore there would be no solution.

To show this **convert the standard form of the equations into *y intercept form*** by dividing by the associated co-efficient of \\( y \\) and subtracting the \\( x \\) term.

\\[ \frac{ax + by = m}{b} \\]

\\[ \frac{cx + dy = n}{d} \\]

\\[ \frac{a}{b}x + y = \frac{m}{b} \\]

\\[ \frac{c}{d}x + y = \frac{n}{d} \\]

In standard form as

\\[ y = - \frac{a}{b}x + \frac{m}{b} \\]

\\[ y = - \frac{c}{d}x + \frac{n}{d} \\]

Now that the gradient is isolated as \\( \frac{a}{b}x \\) and \\( \frac{c}{d}x \\) respectively it is clear that if \\( \frac{a}{b} = \frac{c}{d} \\) then the lines are parallel and this system of equations does *not* have a solution.

This can be stated more elegantly by cross multiplying each side of the equation by their denominators to get

\\[ ad = cb \\]

If this case then the lines are parallel. This is just a restating of the above fractional form. This where the rule that *if*

\\[ ad - cb \neq 0 \\]

Then the lines are parallel and the system has no solution.

## Overlayed Lines

A system of equations **has an infinite number of solutions** *if* **the equations of the lines have the same gradient *and* the same \\( y \\) intercept**. In this case the two equations in the system eseentially just express multiples of the same equation.

For the system of equations

\\[ ax + by = m \\]

\\[ cx + dy = n \\]

The system has infinite solutions

*If* \\( ad - cb = 0 \\) *and* \\( dm - bn = 0 \\)

We can build this rule from the above parallel line formula that was already described. For this rule we also take into account the \\( y \\) intercept which is expressed as \\( \frac{m}{b} \\) and \\( \frac{n}{d} \\). Therefore, the lines **share the same intercept if**

\\[ \frac{m}{b} = \frac{n}{d} \\]

Which can be re-written using *cross multiplication* in the subtractive form as

*Lines share a y intercept if* \\( dm - bn = 0 \\)

For example, the two equations below are just multiple forms of the equation \\( y = 2x + 1 \\)

\\[ 2y - 4x = 2 \\]

\\[ 4y - 8x = 4 \\]

If they are converted to \\( y \\) intercept form

\\[ y = \frac{4}{2}x + \frac{2}{2} \\]

\\[ y = \frac{8}{4}x + \frac{4}{4} \\]

It becomes evident that these are the *same* equation because they both share a gradient of \\( 2 \\) and a \\(y \\) intercept of \\( 1 \\). If they are graphed they overlay at each other and have a solution at *every* point.

<iframe src="https://www.desmos.com/calculator/zjntuoyzlf?embed" width="500" height="500" style="border: 1px solid #ccc" frameborder=0></iframe>

<!-- 
TODO: 
- how to solve 2 unknown equations 
- how to solve 3 unknown equations 
-->