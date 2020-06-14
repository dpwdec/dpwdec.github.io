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

To **declare a new set of tests for a particular **

<!--stackedit_data:
eyJoaXN0b3J5IjpbODUyMjQzMzYxXX0=
-->