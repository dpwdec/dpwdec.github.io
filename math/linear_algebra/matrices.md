---
title: Matrices
layout: page
exclude: true
---

<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>

You can **represent a system of linear equations as a matrix** by removing the algebraic letters and using only the coefficients.

For example, the system

\\[ x + 2y + 3z = 18 \\]
\\[ 3x + 4y + z = 12 \\]
\\[ 2x - y + z = 6 \\]

can be represented as

\\[ \begin{bmatrix} 1 & 2 & 3 \\\ 
3 & 4 & 1 \\\ 
2 & -1 & 1 \\\ \end{bmatrix} = \begin{bmatrix} 18 \\\ 12 \\\ 6 \end{bmatrix} \\]

The matrix after the \\( = \\) equality is the **right hand side** matrix which is shortened to \\( rhs \\).

Implictly there is also a matrix containing the unknowns by which each coefficient in a row is multipled.

\\[ \begin{bmatrix} 1 & 2 & 3 \\\ 
3 & 4 & 1 \\\ 
2 & -1 & 1 \\\ \end{bmatrix}
\cdot \begin{bmatrix} x \\\ y \\\ z \end{bmatrix}
= \begin{bmatrix} 18 \\\ 12 \\\ 6 \end{bmatrix} \\]

So if we multiply \\( x \\) by the \\( 1 \\), \\( 2 \\) and \\( 3 \\) values in the first row we will get back to the first equation in the system.

\\[ x + 2x + 3z = 18 \\]

You can **represent the entire system including the solution in a single matrix** by removing the implicit \\( = \\) equality sign.

\\[ \begin{bmatrix} 1 & 2 & 3 & 18 \\\ 
3 & 4 & 1 & 12 \\\ 
2 & -1 & 1 & 6 \\\ \end{bmatrix}
\\]

## Matrix operations

You can **multiply or divide every element in a matrix row** to manipulat the coefficients and the solution easily. For example we can turn \\( x + 2x + 3z = 18 \\) into \\( 2x + 4x + 6z = 36 \\) easily by doing

\\[ \begin{bmatrix} 1 & 2 & 3 & 18 \end{bmatrix} \cdot \begin{bmatrix} 2 \end{bmatrix} = \begin{bmatrix} 2 & 4 & 6 & 36 \end{bmatrix} \\]

