---
title: Gaussian Elimination
layout: page
exclude: true
---

<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>

Gaussian elimination is an algorithmic like process of solving a system of linear equations by reducing unknowns in the system until a single unknown has been isolated and then plugging the unknown back into the system.

For a system of \\( n \\) equations with \\( n \\) variables

1. Use algebra to create a system of \\( n - 1 \\) equations with \\( n - 1 \\) variables. *Eliminate one variable from the system*.

2. Repeat step one with the current equations until only 1 variable remains.

3. Plug the known variable back into the original system of equations and solve algebraically.

## Matrix Form Elimination

You can **perform Gaussian elimination using a matrix**.

\\[ \begin{bmatrix} 1 & 2 & 3 & 6 \\\ 
3 & 4 & 1 & 8 \\\ 
2 & -1 & 1 & 2 \\\ \end{bmatrix} \\]

Using the above matrix as an example the general steps for matrix elimination are:

1. Find the **pivot**. This is the first non zero number of the matrix starting from the top left hand corner, in this case the \\( \color{red}{1} \\).

\\[ \begin{bmatrix} \color{red}{1} & 2 & 3 & 6 \\\ 
3 & 4 & 1 & 8 \\\ 
2 & -1 & 1 & 2 \\\ \end{bmatrix} \\]

2. Transform the **pivot row** (the row containing the pivot) so that that **pivot** is equal to \\( 1 \\). For example if the pivot row in the above matrix were \\( \begin{bmatrix} 2 & 4 & 6 & 12 \end{bmatrix} \\) the entire row could be multiplied by \\( \frac{1}{2} \\) so change the pivot of \\( 2 \\) into a \\( 1 \\) and transform the whole row into \\( \begin{bmatrix} 1 & 2 & 3 & 6 \end{bmatrix} \\).

3. For each element in each row *below* the pivot row follow the procedure that each element in the matrix equals

\\[ r_x - r_n \cdot p_x \\]

Where

- \\( r \\) is the current row
- \\( x \\) is the iterated index of an element in a row. So \\(r_1 \\) of row 2 of the example matrix is \\( 3 \\), \\(r_2 \\) of row 2 is \\( 4 \\), \\(r_3 \\) of row 2 is \\( 1 \\) and so on.
- \\( n \\) is the first non zero index of the current row
- \\( p \\) is the pivot row

So the first step for the example matrix would be

\\[ r = 2 \\]
\\[ x = 1 \\]
\\[ n = 1 \\]
\\[ p = 1 \\]

Therefore

\\[ r_x = 3 \\]
\\[ r_n = 3 \\]
\\[ p_x = 1 \\]

So

\\[ r_x - r_n \cdot p_x = 3 - 3 \cdot 1 \\]

Our output matrix will so far look like

\\[ \begin{bmatrix} 1 & 2 & 3 & 6 \\\ 
0 & ? & ? & ? \\\ 
? & ? & ? & ? \\\ \end{bmatrix} \\]

Then repeat for the next element in row 2 at index 2.

\\[ r = 2 \\]
\\[ x = 2 \\]
\\[ n = 1 \\]
\\[ p = 1 \\]
\\[ r_x = 4 \\]
\\[ r_n = 3 \\]
\\[ p_x = 2 \\]

So

\\[ r_x - r_n \cdot p_x = 4 - 3 \cdot 2 \\]

Updating the output matrix to

\\[ \begin{bmatrix} 1 & 2 & 3 & 6 \\\ 
0 & -2 & ? & ? \\\ 
? & ? & ? & ? \\\ \end{bmatrix} \\]

We repeat this procedure (as stated above for every element in all the rows *below* the pivot) until we get

\\[ \begin{bmatrix} 1 & 2 & 3 & 6 \\\ 
0 & -2 & -8 & -10 \\\ 
0 & -5 & -5 & -10 \\\ \end{bmatrix} \\]

If these steps are done correctly it should leave a column of \\( 0 \\)s underneath the pivot.

4. Now repeat steps 1-3 by finding a pivot for a row that has not already been used as a pivot.

In this case row \\( 2 \\) will be multiplied by \\( -frac{1}{2} \\) to get \\( \begin{bmatrix} 0 & 1 & 4 & 5 \end{bmatrix} \\) which is suitable as a pivot row because the first non zero number is now a \\( 1 \\). This gives us the matrix

\\[ \begin{bmatrix} 1 & 2 & 3 & 6 \\\ 
0 & \color{red}{1} & 4 & 5 \\\ 
0 & -5 & -5 & -10 \\\ \end{bmatrix} \\]

Now we can start the subtraction process again, with an \\( x \\) index that starts from the pivot index. Such that

\\[ r = 3 \\]
\\[ x = 2 \\]
\\[ n = 2 \\]
\\[ p = 2 \\]
\\[ r_x = -5 \\]
\\[ r_n = -5 \\]
\\[ p_x = 1 \\]

\\[ r_x - r_n \cdot p_x = -5 - -5 \cdot 1 \\]

Which gives the output matrix 

\\[ \begin{bmatrix} 1 & 2 & 3 & 6 \\\ 
0 & \color{red}{1} & 4 & 5 \\\ 
0 & 0 & ? & ? \\\ \end{bmatrix} \\]

Next we get

\\[ r = 3 \\]
\\[ x = 3 \\]
\\[ n = 2 \\]
\\[ p = 2 \\]
\\[ r_x = -5 \\]
\\[ r_n = -5 \\]
\\[ p_x = 4 \\]

\\[ r_x - r_n \cdot p_x = -5 - -5 \cdot 4 \\]

\\[ \begin{bmatrix} 1 & 2 & 3 & 6 \\\ 
0 & 1 & 4 & 5 \\\ 
0 & 0 & 15 & ? \\\ \end{bmatrix} \\]

With the final output being

\\[ \begin{bmatrix} 1 & 2 & 3 & 6 \\\ 
0 & 1 & 4 & 5 \\\ 
0 & 0 & 15 & 15 \\\ \end{bmatrix} \\]

5. When you reduced a row in the matrix to only *two* values - as in the last row above \\( 15 \\) and \\( 15 \\) the value of the variable with a coeeficient in this show can be computed as the final row is a representation of.

\\[ 0x + 0y + 15z = 15 \\]

Which means that

\\[ z = 15 \\]

This known value can now be substituted back itno the original system of equations and used to solve in the them.

You can **change the order of the coefficients in the matrix to calculate *any* of the other unknowns as well**. For example starting with

\\[ \begin{bmatrix} 3 & 2 & 1 & 6 \\\ 
1 & 4 & 3 & 8 \\\ 
1 & -1 & 2 & 2 \\\ \end{bmatrix} \\]

Essentially switching the \\( x \\) and \\( z \\) position will allow you to compute the value for \\( x \\) using gaussian elimination instead of \\( z \\). Whatever unknown's coefficients are in the pen ultimate column is the unknown the value of which will be computed.