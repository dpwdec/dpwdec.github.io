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

You can **create the equivalent of `before_each` method** in your unit test suite that runs before each test by using the `setUp` method. This is run before each test method.
```py
def setUp(self):
  # do set up here
```

You can **keep your test code organised into blocks of similar functionality** by creating a single test class for a specific set of tests with a single `setUp` method and then inheriting a number of different test classes from that class to organise your test code. In the example below we define a `TestClass` that inherits from the `unittest.TestCase` class and then when we want to organise a specific and more localised test we subclass it with the `SomeSpecificTest` class.
```py
class TestClass(TestCase):

  def setUp(self):
    # general class set up

class SomeSpecificTest(TestClas):

  def test_something_specific(self):
    # do a specific test
```

## Running tests

You can **run all test files in you project** (i.e. file beginning with `_test`) by using the `python3 -m unittest` command and not passing in any file arguments.
```py
$ python3 -m unittest
```

You can **run a single test** by calling `unittest` from Python as the main module and passing in the test file you want to run.
```bash
$ python3 -m unittest test_my_class.py
```

You can **run tests in a specific directory** by using the `discover` command the passing in the directory name.
```bash
$ python3 -m unittest discover my_test_folder
```

You cannot call testing files directly, such as `python3 test_my_class.py`, however, you can **set up a test file to run through the `unittest` framework automatically when called** use the `__name__ == '__main__'` pattern by appending the code below to the body of your test file. This will conveniently **only run the test that was called** with the `python` run command and won't trigger the `unittest.main` method for ALL tests.
```py
if __name__ == '__main__':
  unittest.name()
```


## Assertions

You can **add failure messages to an assertion** by adding a third string argument to the `assert` method that contains the message to be printed on failure.
```py
def test_equal(self):
  self.assertEqual(6, 6, "it should equal 6")
```

You can **test if an object is an instance of class** by using the `assertIsInstance` method.
```py
def test_is_instance(self):
  self.asssertIsInstance("Hello", str)
```

You can **test if a class has a method or attribute** by using the `hasattr` method in conjunction with an `assertTrue` method.
```py
def test_has_attribute(self):
  self.assertTrue(hasattr(self.object, "some_attribute_name"))
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

### Mock Objects

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

You can **set a return value for a mock's method** by setting the `return_value` property of a mock's method property. When that mock property is called as a method it will return whatever was set as its return.
```py
# passes
def test_mock_method_called_with_return(self):
  my_mock = Mock()
  my_mock.my_method.return_value = 35
  self.assertEqual(my_mock.my_method(), 35)
```

### Mock Stubs

You can **stub a real object's methods** by assigning the object's method property to an instance of `Mock`.
```py
# passes
def test_stub_method(self):
  real_instance = RealClass()
  real_instance.real_method = Mock()
  real_instance.real_method()
  real_instance.real_method.assert_called_with()
```

You can **stub the return value of a real object's method** by assigning the `return_value` method property of the object that you are mocking.
```py
# passes
def test_stub_method(self):
  real_instance = RealClass()
  real_instance.real_method = Mock()
  real_instance.real_method.return_value = 35
  self.assertEqual(real_instance.real_method(), 35)
```

# Coverage

You can **track python test coverage** using the `coverage.py` module. You can **install `coverage.py`** using `pip install` or `pipenv install`.
```bash
$ pip install coverage
$ pipenv install coverage
```

## Tracking coverage

The basic flow of `coverage.py` is to

1. Run your python tests using `coverage` and collect data on test coverage
2. Report the test coverage data

Unlike other test coverage frameworks these are divided into separate command line steps to execute. (The following examples show usage using `pipenv`, however they are quite similar to the standard CLI usage in the `coverage.py` docs. To **run tests with coverage data gathering** use the `run` command with `coverage`. This will create a `.coverage` file in your repo that you should probably add to your `.gitignore`.
```bash
$ pipenv run coverage run -m unittest
```

To **report the coverage data** using the `report` function which will print a nice table showing test coverage
```bash
$ pipenv run coverage report -m
```

If you want to **run both the coverage data gathering and reporting together** you can combine both commands into a bash `.sh` script file.
```bash
#!/bin/bash
pipenv run coverage run -m unittest
pipenv run coverage report -m
```

## Configuration

You can **configure your coverage settings** by creating a `.coveragerc` file.

### Excluding

You can **omit a directory from being include in your coverage report** by adding it to the `omit` list under the `[run]` section of your `.coveragerc` file. An omission needs to be placed on a new line after the `omit` flag and indented by at least one tab. The `*` asterisk indicates a match all. In the example below we `omit` anything within the `.local` directory.
```
# .coveragerc
[run]
omit =
  */.local/*
```

You can **omit a file by a naming pattern from being include in your coverage report** by adding to the `omit` list with the file name matched using the `*` asterisk character. The `omit` below ignores any `__init__.py` files.
```
# .coveragerc
[run]
omit =
  *__init__* 
```

You can **have multiple omit lines** by simply carriage returning the different `omit` entries.
```
# .coveragerc
[run]
omit =
  */.local/*
  *__init__* 
```

## Coveralls

Coveralls is a service for creating coverage badges for your repos. There is a wrapper for coveralls for python that interfaces directly with Travis CI and the `coverage.py` module. To **install coveralls** simply run a `pip` command on the `python-coveralls` package.
```bash
$ pipenv install python-coveralls
```

Coveralls **currently ONLY WORKS with `coverage.py` versions less than `5.0`**. You must set up your `pipfile` to only install `coverage="<5.0"` with semantic versioning if you want coveralls to work.

After installing `python-coveralls` and adding it to your `pipfile`. The only thing you need to do is add the `coveralls` command your `.travis.yml` file in the `after_success` script section so that it sends coverage data once completed.
```yml
# .travis.yml
language: python
python:
- "3.7"
- 
install:
- pip install pipenv
- pipenv install

script:
- pipenv run coverage run -m unittest

after_success:
- coveralls
```





<!--stackedit_data:
eyJoaXN0b3J5IjpbLTYzODUyNjYyNiwtNDM4OTkyNzQ1LC0xNz
A1ODI4Mzg4LC0xOTcwNDczMjAxLDQzMTIyMzE0MCwtMTk0Nzc3
OTkwOSw5MTg2MjIyNDYsMTcyNjgwNTU3MSwxMDk1MTk3NDUwLC
0zMTcwNTM2NzgsLTcyMjgyMDUzMywtODQ2NjU4MjUyLC0yMjA3
MDEzOTcsNjE3MTQzOTg4LDE5ODQ4MjA5MTMsNzE4OTk5ODldfQ
==
-->