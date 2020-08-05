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

You can **encapsulate your tests into a class** by placing your test cases inside a `class` named with the format `Test*` and adding `self` as a parameter to the test cases. It's important to note that each test case within a test class represents its own instance of that class when `pytest` runs.
```py
class TestClass():
  def test_eq(self):
    assert 1 == 1
```

## Fixtures

A **pytest fixture** is a way to encapsulate set up behaviour for test cases in module way. To **define a new fixture** use the `@pytest.fixture` decorator and make the return value the o
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTExMDg1ODE2NCwxOTA2OTM1NTY3LDc2Mj
kzMzM3MCwyNjI4NTc1ODFdfQ==
-->