---
title: Jsonata
layout: page
exclude: true
---

You can **match an object in an array** by adding `[]` square brackets and using an `=` equals sign with the field you want to select.
```js
// Data 01
{
  "Organisation": "Thunkcorp",
  "Users": [
    {
      "name": "John",
      "age": 20,
      "height": 185
    },
    {
      "name": "Mark",
      "age": 10
    }
  ]
}
```

Query for the example data `Data 01`...
```js
Users[age='10'] =>
{
  "name": "Mark",
  "age": 10
}
```

You can **select a sub property on a matched object**  using the standard `.` dot syntax.
```js
// Query on Data 01
Users[age='10'].name =>
"Mark"
```

You can **select a property based on whether it exists** for data with irregular formatting by using placing the name of a property in the `[]` predicate.
```js
// Query on Data 01
Users[height] =>
{
  "name": "John",
  "age": 20,
  "height": 185
},
```

You can **select a higher level on a nested match** by nesting `[]` square brackets containing predicates.
```js
// Data 02
{
  "Users": [
    {
      "name": "John",
      "age": 20
      "Addresses": [
        {
		  "Number": 20
        }
      ]
    },
    {
      "name": "Mark",
      "age": 10
      "Addresses": [
        {
		  "Number": 40,
        }
      ]
    }
  ]
}
```

Nested query for the example data `Data 02`. Notice that query **returns the entirety of the user object even though the match is made on a lower level property**.
```js
// Query on Data 02
Users[Addresses[Number=20]] =>
{
  "name": "John",
  "age": 20
  "Addresses": [
    {
     "Number": 20
    }
  ]
}
```

You can **execute simple functions on object properties** such us combination by using `()` brackets with operators after the property you are selecting with `.` dot syntax.
```js
// Query on Data 02
Users.(name & " " & age) =>
[
  "John, 20",
  "Mark, 10"
]
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTI2NTYwLDE4Mzg4MTI0ODUsLTIwOTc4OT
gzNTEsLTEzNjY3MTI0OTYsLTY0Njc4ODY0M119
-->