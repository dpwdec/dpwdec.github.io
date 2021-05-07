---
title: Jsonata
layout: page
exclude: true
---

You can **match an object in an array** by adding `[]` square brackets and using an `=` equals sign with the field you want to select.
```js
// Da
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

```js
Users[age='10'] =>
{
  "name": "Mark",
  "age": 10
}
```

You can **select a sub property on a matched object**  using the standard `.` dot syntax.
```js
Users[age='10'].name =>
"Mark"
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE0NTI0MjIyOTcsLTY0Njc4ODY0M119
-->