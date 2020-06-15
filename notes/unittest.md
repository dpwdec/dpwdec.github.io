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

The **basic structure of a single test** follows a pattern of using an *assertion method* on the `self` object with two arguments: the expected output and the actual output.
```py
def test_my_method(self):
  self.assertEqual(assertion, expectation)
```

You can **add multiple assertions into a single test**. These will appear as a single test pass on your test summaries, however if one of the assertions within a single test breaks the test then the resulting error will direct you to the specific assert that failed the test.
```py
def test_my_method(self):
  self.assertEqual(assertion, expectation)
  self.assertEqual(another_assertion, another_expectation)
```

You can **run all test files in you project** (i.e. file beginning with `_test`) by using the `python3 -m unittest` command and not passing in any file arguments.
```py
$ python3 -m unittest
```

You can **run a test** by call `unittest` from Python as the main module and passing in the test file you want to run.
```bash
$ python3 -m unittest test_my_class.py
```

You cannot call testing files directly, such as `python3 test_my_class.py`, however, you can **set up a test file to run through the `unittest` framework automatically when called** use the `__name__ == '__main__'` pattern by appending the code below to the body of your test file. This will conveniently **only run the test that was called** with the `python` run command and won't trigger the `unittest.main` method for ALL tests.
```py
if __name__ == '__main__':
  unittest.name()
```

## Assertions

You can **add failure messages to an assertion** by adding a third string argument to the `assert` method that contains the message to be printed on failure.
```py
def my_test(self):
  self.assertEqual(6, 6, "it should equal 6")
```

## Mocks

You can **start using mock and double objects** by using the python `unittest.mock` extension library. These mocks give you the ability to stub methods on real classes as well as create entire mock / double objects for the purposes of testing and keeping your dependencies separate and testable. They also provide **assertion functions** for testing that a specific method was called. The example `import` statements below show several different ways you *could* `import` mocks into your tests depending on your preferences.
```py
# import top level mock namespace
import unittest.mock
# import mock namespace
from unittest.mock import mock
# import specific frequently used mocking modules
from unittest.mock import Mock
from unittest.mock import MagicMock
```

You can **create a mock object** by instantiating an instance of the `Mock` or class.
```py
def test_my_mock(self):
  my_mock = Mock()
```

You can **test that a method was called on a mock** by appending the name of the method you want to test for to the mock instance and then using the `assert_called_with` method on mock method property. Mock objects **automatically create a mock version of a method if it is called** which means you don't have to explicitly specify that `my_mock` accepts `my_method` and the assertion on its call will still work.
```py
# passes
def test_mock_method_called(self):
  my_mock = Mock()
  my_mock.my_method()
  my_mock.my_method.assert_called_with()
```

You can **test that a mock method was called with a specific set of arguments** by submitting the expected arguments to the `assert_called_with` method.
```py
# passes
def test_mock_method_called_with_args(self):
  my_mock = Mock()
  my_mock.my_method(2, 3)
  my_mock.my_method.assert_called_with(2, 3)
```

You can **set a return value for a mock's method** by 


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4OTkwNjkxMTAsMTcyNjgwNTU3MSwxMD
k1MTk3NDUwLC0zMTcwNTM2NzgsLTcyMjgyMDUzMywtODQ2NjU4
MjUyLC0yMjA3MDEzOTcsNjE3MTQzOTg4LDE5ODQ4MjA5MTMsNz
E4OTk5ODldfQ==
-->