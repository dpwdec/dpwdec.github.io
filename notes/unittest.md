---
title: Unittest
layout: page
exclude: true
---

Unittest is a unit testing framework for python that comes as part of python's standard library. You can start using the `unittest` framework by simplying `import`ing it using `import unittest`.

## Structure
The **test file naming convention** is to use `test_` and the name of the file that is going to tested in the format: `test_NAME_OF_FILE_TO_BE_TESTED`. This is a requirement for writing tests.

You must also **import the code you want to be tested** at the head of your test file.
```py
import unittest
import my_code_to_be_tested
```

To **declare a new set of tests for a particular file** create a new class that inherits from `unitttest.TestCase` class. Your test code will be defined *within* this class.
```py
class TestMyClass(unittest.TestCase):
```

To **define a new test** create a new method the name of which should start with `test_`. This is again a requirement for writing tests, with this naming convention telling the test runner which methods are tests.
```py
def test_my_method(self):
```

## Assertions



<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE1MTA1MjM5MTddfQ==
-->