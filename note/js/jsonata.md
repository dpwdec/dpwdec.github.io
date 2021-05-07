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
      "age": 20
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

You can **maintain select of a higher level object**

You can **select a higher level on a nested match** by nesting `[]` square brackets containing predicates.
```js
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
    }
  ]
}
```

```js
Users[Addresses[Number=20]]
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMzk0MTM2MTQ2LC0xMzY2NzEyNDk2LC02ND
Y3ODg2NDNdfQ==
-->