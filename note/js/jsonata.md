---
title: Jsonata
layout: page
exclude: true
---

You can **match an object in an array** by adding `[]` square brackets and using an `=` equals sign with the field you want to select.
```js
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

---

Users[age='10'] =>

{
  "name": "Mark",
  "age": 10
}
```

You can **select a sub property on a matched object** 
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTY0NDgxNTU4NSwtNjQ2Nzg4NjQzXX0=
-->