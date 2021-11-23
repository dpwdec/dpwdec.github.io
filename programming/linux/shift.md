---
layout: page
exclude: true
title: Shift
---

The `shift` command moves command line argument input indexing "left" by a specified amount. The default is `1`, so calling `shift` with no argument will shift arguments by `1`.
```bash
shift <AMOUNT_TO_SHIFT>
```

For example, the following bash script with inputs `a b c` would echo `a` then `c` because the `$1` argument would start as `a` then the inputs shifted two positions so that `$1` becomes `c`.
```bash
echo $1
shift 2
echo $1
```