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




<!--stackedit_data:
eyJoaXN0b3J5IjpbMTAzMzA1NzU4NywtMTY4MjgyODk3NCwtMj
AwOTY0NjA5MywtMTYyMjU5MDI4NywxOTAxMTg3NzQ1LC04OTM0
NzUxMjAsMTQ0NzE4NTEyNiw3MDg3MDM5ODgsMTkwNjkzNTU2Ny
w3NjI5MzMzNzAsMjYyODU3NTgxXX0=
-->