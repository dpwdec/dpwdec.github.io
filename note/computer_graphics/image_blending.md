---
title: Image Blending
layout: page
exclude: true
---

You can **evenly blend *n* number of images** by simply scaling the value of each pixel in each input by \\( \frac{1}{n} \\) and then adding the resulting scaled pixel values to the final image. For example, if you had *four* images that you wanted to evenly blend then an output pixel \\( x \\) for input image pixels \\( p_1, p_2, p_3, p_4 \\) would be
```python
n = 4
blend_ratio = 1 / n
x = (p_1 * blend_ratio) + (p_1 * blend_ratio)
```

https://homepages.inf.ed.ac.uk/rbf/HIPR2/blend.htm

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTE3MzU0Mjk5MF19
-->