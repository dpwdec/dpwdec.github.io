---
title: Type Hints
layout: page
exclude: true
---

You can **add type hints to for the inputs and outs of functions and classes**. To **define an input type** use a `:` colon followed by the type. To **define an output type** use an `->` followed by the type.
```py
def greeting(name: str) -> str:
  return f"Hello {name}"
```

You can **add type hints for the inputs of collections** by importing their typed versions from the `typing` module. The `scores` function below has a type hint indicating it returns a `Dict` with `str` type keys and `int` type values.
```py
from typing import Dict

def scores() -> Dict[str, int]:
  return {
    "Jason": 20,
	"Gertrude": 19,
	"Mildred": 331
  }
```

You can **alias types to names** by simply assigning them with `=` equals. In the example below, the `int` type is aliased to `Vertex` and a list of "`Vertex`es" is aliased as a `Vector`.
```py
from typing import List

Vertex = int
Vector = List[Vertex]
```

You can **type hint a function** with the `callable` type from the `typing` library.
```py
from typing import callable

def higher_order_function(func: callable) -> callable:
  # construct another function using func
```

## list

The `list` type is included as part of the default set of python type hints.
```python
def joiner(words: list) -> str:
  return ' '.join(words)
```

However, **this list type CANNOT contain types**, you cannot specify for readers that the `list` being passed into `joiner` the function above should contain `str` types. The code below will not work.
```python
# does not work
def joiner(words: list[str]) -> str:
  return ' '.join(words)
```

To **specify internal list types** you need to `import` the `List` type from the `typing` library.
```python
from typing 
def joiner(words: List[str]) -> str:
  return ' '.join(words)
```


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTgzNDA4MTI2NywtNTY0MjQ3MjldfQ==
-->