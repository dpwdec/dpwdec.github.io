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

A **pytest fixture** is a way to encapsulate set up behaviour for test cases in module way. To **define a new fixture** use the `@pytest.fixture` decorator and make the return value the result that will be used by your test.
```py
import pytest

@pytest.fixture
def create_msg():
  return "This is a message"
```

You can **call a fixture in a test** by adding it as an argument that **matches the name of the fixture** to the test function, this will **pass the result of the test fixture into the test function** to be used.
```py
def test_msg(create_msg):
  assert create_msg == "This is a message"
```

You can **integrate set up with tear down functionality inside a fixture** by using a `yield` inside the fixture with the argument to the yield being the object that you want to be pass to your test. However, doing `assert`ions inside a fixture is not recommended.
```py
@pytest.fixture():
def db():
  db_connection = create_database()
  yield db_connection # send the db connection object to the test
  db_connection.close() # runs after the test has finished and closes the connection
```

You can **share the objects create in fixtures across multiple scopes** by using the `scope` flag as an argument in the fixture definition. By default a fixture is re-created every time each test function runs, this may not be feasible if the fixture does some computationally expensive set up. The `scope="module` will initialise the fixture *once* for an entire module allowing all tests to interact with it and persist its state.
```py
@pytest.fixture(scope="module")
def db_connection():
  db = create_db_connection()
  return db
```

There are **multiple possible scopes for fixtures** which can be at the level of the:
- `function` (the default)
- `class`
- `module`
- `package`
- `session` (the entire session of running your tests)

You can **require a fixture for every test function within a scope WITHOUT explicitly referencing it** by setting the `autouse` argument to `True`. This will make the fixture run by default for each test even if the test doesn't explicitly invoke that feature.
```py
@pytest.fixture(autouse=True)
def some_essential_setup():
  # do essential set up here
```

### conftest

You can **make fixtures available in multiple locations WITHOUT importing** by defining them in `conftest.py` file in your project directory. When `pytest` runs it will automatically check the `conftest.py` file for a matching fixture.
```py
# conftest.py
import pytest

@pytest.fixture
def create_msg():
  return "This is a message" 
```

## Mocking

To start using Pytest's mocking functionality you must install the `pytest-mock` module.
```bash
pip3 install pytest-mock
```

**Mocking can be accomplished in Pytest using the `mocker` fixture**. This is passed into test functions that need to use mocking as an argument. **It does not need to be imported as a dependency for the tests**.
```py
def some_test(mocker):
  # use mocker here to mock things
```

The **`pytest-mock` module is simply a wrapper around standard `mock` library** that allows it work as a fixture. Everything that you can do with python's `unittest.mock` library you can do with pytest's `mocker` fixture.
```py
def mock_functionality(mocker):
  # create a mock class
  my_mock = mocker.Mock()
```

You can **mock methods and function returns** using the `patch` method on `mocker`. This takes the name of the method that is being mocked as a string, and a named argument `return_value` set equal to mocked return. In the example below the `expensive_user` function calls the `expensive_function` when it returns, which is computationally intensive. To mock this function, which also inside the `expf` file, it is referenced with `expf.expensive_function`. The `patch` method is **function scoped**, if you mock a value differently in different test functions these will not conflict.
```py
from expf import expensive_user

def some_test(mocker):
  mocker.patch("expf.expensive_function", return_value=True)
  assert expensive_user() == True
```

If you want to **patch a method or function imported from a different file** to the function that you are testing, you should still reference it *as if* it were defined in the file which you are testing.




<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEwMDAyMDM1ODIsOTYyNDUyODMxLDU4Mz
UwMjQ5Myw0NzU0MDE0MTMsLTE1OTg5MTM1MDEsMjA4MDY0MzAy
NSwxMDMzMDU3NTg3LC0xNjgyODI4OTc0LC0yMDA5NjQ2MDkzLC
0xNjIyNTkwMjg3LDE5MDExODc3NDUsLTg5MzQ3NTEyMCwxNDQ3
MTg1MTI2LDcwODcwMzk4OCwxOTA2OTM1NTY3LDc2MjkzMzM3MC
wyNjI4NTc1ODFdfQ==
-->