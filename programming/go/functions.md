---
layout: page
exclude: true
title: functions
---

You can **assign a function to a variable** inside the body of another function. 
```go
func main() {
  double := func(x int) int {
    return x * 2
  }

  double(2) // => 4
}
```

This also means you can **store functions inside data structures** by type hinting the function structure to be stored.
```go
func main() {
  // create an array that stores functions that take an int and return an int
  funcs := [2]func(x int) int {
    // store first func
    func(x int) int {
      return x * 2
    },
    // store second func
    func(x int) int {
      return x / 2
    },
  }

  funcs[1](10) // => 5
}
```