---
layout: page
exclude: true
title: fmt
---

You can **interpolate into a print output** by using the `Printf` function from `fmt` package using `%v` to substitute variables. You will need to add a `\n` character if you want new line printing.
```go
x := "Natasha"
fmt.Printf("%v! Hello there!\n", x) // => Natasha! Hello there!
```

