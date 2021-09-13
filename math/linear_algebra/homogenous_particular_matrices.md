---
title: Homogenous and Particular Matrix Components
layout: page
exclude: true
---

<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>

All linear systems can be decomposed into a **homogenous** and **particular** solution.

The **homogenous** solution uses the coefficients of the matrix for \\( Ax = 0 \\).

The **particular** solution uses some addition of a constant for \\( Ax = b \\).

## Discussion

You can **state the variable components in a matrix in terms some other variable in the matrix**, where \\( x \\) and \\( y \\) are stated in terms of \\( z \\), for example.

We can transform the matrix below to achieve this.

\\[ \begin{bmatrix} 1 & 2 & -3 & 3 \\\ 2 & -2 & -3 & 0 \end{bmatrix} \\]

Firstly, we want to transform one of the such rows such that we end up with at least one variable zeroed out and a coefficient equal to the solution. We can do this by subtracting twice the first row of the matrix from the second row.

\\[ \begin{bmatrix} 1 & 2 & -3 & 3 \end{bmatrix} \cdot \begin{bmatrix} 2 \end{bmatrix} = \begin{bmatrix} 2 & 4 & -6 & 6 \end{bmatrix} \\]

\\[ \begin{bmatrix} 2 & -2 & -3 & 0 \end{bmatrix} - \begin{bmatrix} 2 & 4 & -6 & 6 \end{bmatrix} =  \begin{bmatrix} 0 & -6 & 3 & -6 \end{bmatrix} \\]

And then dividing the new row so that the \\( y \\) column and the solution equal \\( 1 \\).

\\[ \begin{bmatrix} 0 & -6 & 3 & -6 \end{bmatrix} \div -6 = \begin{bmatrix} 0 & 1 & -\frac{1}{2} & 1 \end{bmatrix} \\]

This new final row is equivalent to

\\[ 0x + 1y - \frac{1}{2}z = 1 \\]

Which can be rearranged to

\\[ y = \frac{1}{2}z + 1 \\]

With \\( y \\) stated in terms of \\( z \\).

This term in \\( y \\) can be substituted *back* into the original equation, reducing it to an expression with just 2 unknowns.

\\[ x + 2(\frac{1}{2}z + 1) -3z = 3 \\]

\\[ x = 2(\frac{1}{2}z + 1) + 3z + 3 \\]

\\[ x = -z - 2 + 3z + 3 \\]

\\[ x = 2z + 1 \\]

By rearranging we have also stated \\( x \\) in terms of \\( z \\). Now the whole system of equations can be expressed in terms of this unknown.

\\[ x = 2z + 1 \\]

\\[ y = \frac{1}{2}z + 1 \\]

\\[ z = z \\]

This can be expressed as the product of two matrices, where one matrix represents the coefficients applied to unknown and the other the added term at the end.

\\[ z \cdot \begin{bmatrix} 2 \\\ \frac{1}{2} \\\ 1 \end{bmatrix} + \begin{bmatrix} 1 \\\ 1 \\\ 0 \end{bmatrix} \\]

The first column \\( \begin{bmatrix} 2 \\\ \frac{1}{2} \\\ 1 \end{bmatrix} \\) is a solution to \\( Ax = 0 \\) case of the equation.

The first column *and* the second column are a solution to the \\( Ax = b \\) case.

These are known as the **homogenous** and **particular** solutions to a system of equations. **Every system of equations can be split into a homogenous and particular solution**.

The unknown \\( z \\) can also take **any real number** i.e. \\( z \in \mathbb{R} \\) as a solution to this system of equations.

For example, if we pick \\( z \\) to be \\( 1 \\) and then plug the values for the homogenous solution back into the equation represented by the first row of the original matrix we get

\\[ 1 \cdot (2 \cdot 1) + 2 \cdot (\frac{1}{2} \cdot 1) - 3 \cdot 1 \\]

\\[ 2 + 1 - 3 = 0 \\]

For whatever value of \\( z \\) that we pick, if we just use this homogenous solution as the values for the unknowns the solution will always be \\( 0 \\). 

*But even in the particular case you can pick any value?*

There is also nothing special about isolating \\( z \\) here. You could isolate \\( x \\) and express the other unknowns in terms of it and then use any \\( x \\) for the homogenous and particular solutions.
