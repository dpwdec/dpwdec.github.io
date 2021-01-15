---
title: IEEE754
layout: page
exclude: true
---

For **numbers that are both large AND small**, i.e. they have a number of digits in the positive component and also a lot of decimal places such as 10000.00003 the **small decimal amount is pushed off the end of the mantissa** and lost entirely. This is part of the intrinsic inaccuracy of these numbers.
```
     2^9            
0 10001000 11110100000000000000000
``` 
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE3NjAyMzU4NTVdfQ==
-->