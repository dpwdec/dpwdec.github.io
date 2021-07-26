---
layout: page
exclude: true
title: enum
---

You can **define an enum** by defining a set of `const`s that are annotated with the enum type and the `iota` keyword.
```go
package httpverbs

type HttpVerb int

const (
  GET HttpVerb = iota
  POST
  PUT
  DELETE
)
```

You should store your enum inside its own package because otherwise the `const` value will be available at the top level namespace of the file in which its defined.

You can **access the enum variants** on the package namespace *not* on the type.

You can **access the enum type** from the package namespace and use it for data structure storage types.
```go
package main

import("my-project/httpverbs")

func main() {
  // access the a variant of the variant
  x := httpverbs.GET

  // store variants of enum in a data structure
  y := [httpverbs.HttpVerb]{httpverbs.GET, httpverbs.DELETE}
}
```

You can **iterate through all variants of an enum** by adding a "terminating" enum value at the end of the list of enum definition and iterating through to that limit starting from a specific value.
```go
package httpverbs

type HttpVerb int

const (
  GET HttpVerb = iota
  POST
  PUT
  DELETE
  Terminator
)

for verb := HttpVerb(0); verb <
```

The example below iterates through each of the variants of the enum as integer values. This is then used to index a `map` that stores uses the `HttpVerb` type as its key.
```go
package main

import(
  "fmt"
  "my-project/httpverbs"
)

func main() {
  verbs := map[httpverbs.HttpVerb]string {
    httpverbs.GET: "GET",
    httpverbs.POST: "POST",
    httpverbs.PUT: "PUT",
    httpverbs.DELETE: "DELETE",
  }

  for verb := httpsverbs.HttpVerb(0); verb < httpsverbs.Terminator; verb++ {
    fmt.Println("%v\n", verbs[verb])
  }

  // output =>
  // GET
  // POST
  // PUT
  // DELETE
}
```