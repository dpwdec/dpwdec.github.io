---
title: Homogenous and Particular Matrix Components
layout: page
exclude: true
---

<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>

You can **state the variable components in a matrix in terms some other variable in the matrix**, where \\( x \\) and \\( y \\) are stated in terms of \\( z \\), for example.

We can transform the matrix below to achieve this.

\\[ \beging{bmatrix} 1 & 2 & -3 & 3 \\\ 2 & -2 & -3 & 0 \end{bmatrix} \\]

Firstly, we want to transform one of the such rows such that we end up with at least one variable zeroed out and a coefficient equal to the solution. We can do this by subtracting twice the first row of the matrix from the second row.

\\[ \beging{bmatrix} 1 & 2 & -3 & 3 \end{bmatrix} \cdot \beging{bmatrix} 2 \end{bmatrix} = \beging{bmatrix} 2 & 4 & -6 & 6 \end{bmatrix} \\]

\\[ \beging{bmatrix} 2 & -2 & -3 & 0 \end{bmatrix} - \beging{bmatrix} 2 & 4 & -6 & 6 \end{bmatrix} =  \beging{bmatrix} 0 & -6 & 3 & -6 \end{bmatrix} \\]

And then dividing the new row so that the \\( y \\) column and the solution equal \\( 1 \\).

\\[ \beging{bmatrix} 0 & -6 & 3 & -6 \end{bmatrix} \div -6 = \beging{bmatrix} 0 & 1 & -\frac{1}{2} & 1 \end{bmatrix} \\]

This new final row is equivalent to

\\[ 0x + 1y - \frac{1}{2}z = 1 \\]

Which can be rearranged to

\\[ y = \frac{1}{2}z + 1 \\]

With \\( y \\) stated in terms of \\( z \\).