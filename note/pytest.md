---
title: Pytest
layout: page
exclude: true
---

To **create a new test file** that Pytest can find and run, the file name must be in the format `test_*.py` or `*_test.py`.

You can **create a new test case** by defining a function in the format `test_*` and using the pytest `assert` keyword. You **do not need to import Pytest** to do this.
```py
def test_eq():
  assert 1 == 1
```

You can **run Pytest** by using the `pytest` command. This will find all appropriately named pytest test cases.
```bash
$ pytest
```

You can **encapsulate your tests into a class** by placing your test cases inside a `class` named with the format `Test*` and adding `self` as a parameter to the test cases.
```py
class TestClass():
  def test_eq(self):
    assert 1 == 1
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbNzYyOTMzMzcwLDI2Mjg1NzU4MV19
-->