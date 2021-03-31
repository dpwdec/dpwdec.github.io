---
title: Image Blending
layout: page
exclude: true
---

You can **evenly blend *n* number of images** by simply scaling the value of each pixel in each input by \\( \frac{1}{n} \\) and then adding the resulting scaled pixel values to the final image. For example, if you had *four* images that you wanted to evenly blend then an output pixel \\( x \\) for input image pixels \\( p_1, p_2, p_3, p_4 \\) would be
```python
n = 4
blend_ratio = 1 / n
x = (p_1 * blend_ratio) + (p_2 * blend_ratio) + (p_3 * blend_ratio) + (p_4 * blend_ratio)
```

However, in an actually implementation you *may have to apply the blend to each channel of each pixel (rgb etc.) and then add to each corresponding channel in the output pixel*. For example

```python
n = 4
blend_ratio = 1 / n
x_red_channel = (p_1.red_channel * blend_ratio) + (p_2.red_channel  * blend_ratio) + (p_3.red_channel  * blend_ratio) + (p_4.red_channel * blend_ratio)

x_green_channel = (p_1.x_green_channel * blend_ratio) + (p_2.x_green_channel  * blend_ratio) + (p_3.x_green_channel  * blend_ratio) + (p_4.x_green_channel * blend_ratio)

x_blue_channel = (p_1.x_blue_channel * blend_ratio) + (p_2.x_blue_channel  * blend_ratio) + (p_3.x_blue_channel  * blend_ratio) + (p_4.x_blue_channel * blend_ratio)

x = make_pixel_from_channels(x_red_channel, x_green_channel, x_blue_channel)

```

More information [here](https://homepages.inf.ed.ac.uk/rbf/HIPR2/blend.htm)

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTExODE2NTM3NF19
-->