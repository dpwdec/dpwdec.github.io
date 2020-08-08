---
title: Derivatives
layout: page
exclude: true
---
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.11.1/dist/katex.min.css" integrity="sha384-zB1R0rpPzHqg7Kpt0Aljp8JPLqbXI3bhnPWROx27a9N0Ll6ZP/+DiW/UqRcLbRjq" crossorigin="anonymous">  

<!-- The loading of KaTeX is deferred to speed up page rendering -->  
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.11.1/dist/katex.min.js" integrity="sha384-y23I5Q6l+B6vatafAwxRu/0oK/79VlbSz7Q9aiSZUvyWYIYsd+qj+o24G5ZU2zJz" crossorigin="anonymous"></script>  

<!-- To automatically render math in text elements, include the auto-render extension: -->  
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.11.1/dist/contrib/auto-render.min.js" integrity="sha384-kWPLUVMOks5AQFrykwIup5lo0m3iMkkHrD0uJ4H5cjeGihAutqP0yW0J6dpFiVkI" crossorigin="anonymous" onload="renderMathInElement(document.body);"></script>

<style>
    div {
        margin: auto
    }
</style>

A **derivative** allows you to calculate the gradient at points a long a curved graph.

A **derivative** is defined as the **instantaneous rate of change at a point on a graph**. However, this is a confusing, almost meaningless definition. It seems paradoxical for something to have a rate change in a sinlge instant as change is, by definition, something that occurs over time.

A better definition of a derivate might be: **the rate of change between two points that are so close together the effect that the distance between them has on calculation can be ignored**.

This is often rephrased as a difference between two points that **shrinks towards zero**.

## Visual Approach

This calculation is trivial when your graph is just a straight line. The formula for which is:

<p>
$$
\frac{\Delta y}{\Delta x}
$$
</p>

Which is read as **delta x divided by delta y** which simply means *the change in y divided by the change in x*. The graph below shows the funtion:

<p>
$$
y = 2x
$$
</p>

<div id="straight"></div>
<script>
    functionPlot({
  target: "#straight",
  disableZoom: true,
  grid: true,
  data: [{ fn: "2x" }]
})
</script>

<div></div>

You can calculate the gradient of this line by taking two points along that line and then dividing the difference between them. For example, if you have the coordinates `(1, 2), (2, 4)` the calculation for the gradient would be:

<p>
$$
\frac{4 - 2}{2 - 1} = \frac{2}{1} = 2
$$
</p>

So the rate of change of graph above is `2`. This function is a straight line so its rate of the change is constant, no matter what two points you use to run the calculation above you will get the same result.

But how would you calculate the gradient of a curved graph? The next graph shows the function:

<p>
$$
y = x^2
$$
</p>

It's not clear how we can solve the problem of finding the gradient or rate of change of this graph because it is constantly changing. At `x = 0` the rate of change will be completely different from `x = 10`.

<div id="xsquared"></div>

<script>
    functionPlot({
  target: '#xsquared',
  yAxis: {domain: [-1, 9]},
  disableZoom: true,
  data: [{
    fn: 'x^2',
  }]
})
</script>

We can however approximate the rate of change in a local area of the graph by drawing a straight line between two points on the graph and calculating the gradient for that straight line with the simple *change in x over change in y* formula above. The graph below shows a zoomed in section of the `y = x^2` curve with a line that intersects two points on the curve. Calculating the gradient of this line can approximate the rate of change at that point.

<div id="average"></div>
<script>
functionPlot({
  target: "#average",
  yAxis: { domain: [-0.6, 1] },
  xAxis: { domain: [-2, 2] },
  data: [
    { fn: "x^2" },
    {
      fn: "x/2"
    }
  ]
});
</script>

To get a more accurate rate of change for a specific point on the graph we could **shrink the distance between the two intersection points** until the distance is almost unnoticeable.

<div id="small"></div>
<script>
functionPlot({
  target: "#small",
  disableZoom: true,
  yAxis: { domain: [-0.6, 1] },
  xAxis: { domain: [-2, 2] },
  data: [
    { fn: "x^2" },
    {
      fn: "x/5  0.2"
    }
  ]
});
</script>

At this point the line we are calculating begins to look like a **tangent** to a point on the curve where we want to know the rate of change, and in fact, this is exactly what the derivate of a point is! 

However, there's a problem. With this method of testing smaller and smaller real points on the graph we can only ever reach an approximation of the gradient at any specific point but we would like a pure, beautiful and general way to describe the gradient at an arbitrary point on the graph.

## Algebraic Approach

You can **derive this intuition about the derivative** algebraically from the *change in x over change in y* formula by thinking about in terms of this very small difference between two points, a difference which shrinks towards (but never actually reaches) zero. The name for this is often `dx`. For a function:


<p>
$$
y = f(x)
$$
</p>

This means that:

<p>
$$
\frac{dx}{dy} = \frac{f(x + dx) - f(x)}{dx}
$$
</p>

Because we need to calculate the two positions of `y` at both `x` and `x` plus that very small difference `dx`. The difference between these two `y`s is `dy`.

Let's use this with the example the graph above for the function:
<p>
$$
f(x) = x^2
$$
</p>

This means that we subsitute the function for `x^2`.
<p>
$$
\frac{(x + dx)^2 - x^2}{dx} \\[5pt]

=

\frac{x^2 + 2xdx + dx^2 - x^2}{dx} \\[5pt]

=

\frac{2xdx + dx^2}{dx}
$$
</p>

We then cancel the `dx` in the demoninator with each of the clauses in the numerator to get:

<p>
$$
2x + dx
$$
</p>

And, **this is the most important part about the intuition here** because `dx` is so small as to be almost, or shrinking towards, zero, it can be ignored. We can just remove it from the equation! 🤯  

So the derivative of the graph `f(x) = x^2` is just `2x`. At point `x = 2` the slope of the graph is `4` at point `x = 5` the slope of the graph is `10`. 

This derivative basically just represents a line that is **perfectly tangent to a point on the graph**. The graph below demonstrates this interactively by dynamically calculating the derivative line for a point on the graph.

<div id="derivative"></div>

<script>
functionPlot({
  target: '#derivative',
  disableZoom: true,
  yAxis: {domain: [-1, 9]},
  data: [{
    fn: 'x^2',
    derivative: {
      fn: '2 * x',
      updateOnMouseMove: true
    }
  }]
})
</script>

## Derivative Rules

The **derivative is often abbreviated** to a tick mark `'`. For example the derivative of the function `f` would be written as `f'`.

### Power Rule

The **power rule** states that you can **calculate the derivative for function with a power in it** by placing the power as a multipler in from of the algebraic term of the function and substracting 1 from the power.

<p>
$$
(x^n)' = nx^n-1
$$
</p>

Examples:

<p>
$$
(x^3)' = 3x^2 \\[5pt]
(5x^4)' = 20x^3
$$
</p>

This **also works for fractional and negative powers**:

<p>
$$
(\frac{1}{x})' = (x^-1)' = -x^-2 = \frac{1}{x^2} \\[5pt]
$$
</p>

### Sum and Difference Rules

The **sum rule** states that the derviate is **composable** from the individual derivates of the function terms. The same **difference rules** applies for the difference between function terms.

<p>
$$
(f + g)' = f' + g' \\[5pt]
(f - g)' = f' - g'
$$
</p>

Examples:

<p>
$$
(x^2 + x^3)' = 2x + 3x^2 \\[5pt]
(x^5 - x^6)' = 5x^4 + 6x^5
$$
</p>
<!--stackedit_data:
eyJoaXN0b3J5IjpbMzA4MTAxNDMzXX0=
-->