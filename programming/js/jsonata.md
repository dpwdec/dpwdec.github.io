---
title: Jsonata
layout: page
exclude: true
---

## Predicates

You can **select an object using a predicate expression** (some expression that evaluates to true or false using `[]` square brackets.

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
      "age": 20,
      "Addresses": [
        {
		  "Number": 20
        },
        {
          "Number": 25
        }
      ]
    },
    {
      "name": "Mark",
      "age": 10,
      "Addresses": [
        {
		  "Number": 40
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

You can **execute functions within predicate expressions** to filter objects based on conditions. In the example below the `$count` function is used to get the length of the array and then the conditional `>1` is used on the result. This is then evaluated in the `[]` brackets and applied as a predicate to select.
```js
// Query on Data 02
Users[$count(Addresses)>1] =>
{
  "name": "John",
  "age": 20
  "Addresses": [
    {
     "Number": 20
    },
    {
      "Number": 25
    }
  ]
}
```

You can **filter an array based on its contents** by using the `in` in-fix function within a predicate.
```js
// Data 03
[
  {
    "data": [1, 2, 3]
  },
  {
    "data": [4, 5, 6]
  }
]
```

Query for example `Data 03` selects only the object which has a `4` occurring in its `data` property.
```js
*[4 in data] =>
{
  "data": [4, 5, 6]
}
```


## Functions

You can **execute simple functions on object properties** such us combination by using `()` brackets with operators after the property you are selecting with `.` dot syntax. The `&` syntax below is used for concatenating strings, but you can use standard numeric operators for purely numeric data.
```js
// Query on Data 02
Users.(name & " " & age) =>
[
  "John, 20",
  "Mark, 10"
]
```

You can **concatenate the results of two arrays** using the `$append` function. This is useful for combining the results of two queries on a data set.
<!--stackedit_data:
eyJoaXN0b3J5IjpbOTA0NjA4OTgyLDczNjEyMTM4NywtNTY2MT
c5NDkwLDE4Mzg4MTI0ODUsLTIwOTc4OTgzNTEsLTEzNjY3MTI0
OTYsLTY0Njc4ODY0M119
-->