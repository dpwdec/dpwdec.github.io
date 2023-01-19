---
title: Prometheus
layout: page
exclude: true
---

## Vector Matching

You can **perform logical operations on metrics with differing labels** by using the `ignoring` keyword in your query. By default prometheus does not allow you to perform operations (such as division or subtraction) on metrics with differing labels. So the following query would fail with no data returned because the `my_label` property differs between the two metrics that are being read.
```
# fails
avg_over_time(my_metric{my_label="foo"}[1m]) / avg_over_time(my_metric{my_label="bar"}[1m]) 
```

Instead you need to **add the `ignoring` keyword with the different property before the invocation of the other metric**
```
avg_over_time(my_metric{my_label="foo"}[1m]) / ignoring(my_label) avg_over_time(my_metric{my_label="bar"}[1m]) 

```