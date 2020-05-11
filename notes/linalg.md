---
title: Linear Algebra
layout: page
exclude: true
---


<script src="https://cdn.jsdelivr.net/npm/chart.js@2.8.0"></script>


<canvas id="myChart"></canvas>

<script>
var ctx = document.getElementById('myChart').getContext('2d');
var chart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'line',

    // The data for our dataset
    data: {
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
        datasets: [{
            label: 'My First dataset',
            backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(255, 99, 132)',
            data: [0, 10, 5, 2, 20, 30, 45]
        }]
    },

    // Configuration options go here
    options: {}
});
</script>

<p>
$$
\Gamma(z) = \int_0^\infty t^{z-1}e^{-t}dt\,
$$
</p>

<p>
$$
\begin{vmatrix}
   0 & 1 \\
   1 & 0
\end{vmatrix}
\centerdot
\begin{vmatrix}
   0 & 1 \\
   1 & 0
\end{vmatrix}
$$
</p>

<h1>
$$
\begin{vmatrix}
   3 & 2 & 5 \\
   1 & 0 & 9 \\
   6 & 8 & 4
\end{vmatrix}
$$
</h1>
