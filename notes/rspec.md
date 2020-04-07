---
layout: page
exclude: true
---

# RSpec

## Mocks

**Test doubles** allow you to define object's that "stand in" for a real object in your system and will give and receive data in a predefined patterns as if they were an actual object. To **create a double** use:
```ruby
dbl = double()
# create a double with an optional name
dbl = double("Name")
```
Doubles are **strict**, only responding to the messages which you say they should respond to. If you try to pass a message to a double that is not expecting you will get an `received unexpected message` error. To **add a messages and return types to a double** submit a list of hashes as part of the doubles constructor: 
```ruby
dbl = double("Name", :method_1 => 3, :method_2 => "hello")
# calling a method on a double
dbl.method_1
=> 3
# using a double's method in an example block
it "passes" do
	expect(dbl.method_2).to eq("hello")
end
```
You can make a double **non-strict** by adding `.as_null_object` to the end of the double creation. For any method its receives that is undefined it will return itself. These non-strict can also be created *with* strict return types as well.
```ruby
# returning itself for all method calls
dbl = double("Name").as_null_object
dbl.a_method => dbl
# returning 2 for a_method and itself for all other method calls
dbl = double("Name", :a_method => 2).as_null_object
dbl.a_method => 2
dbl.b_method => dbl
```
You can add additional methods to a double after creation using the `allow(...)` and `receive(...)` methods. Where `allow` describes the object to receive the method and `receive` describes the name of the method to be received as a symbol. You can convert this syntax into a **method stub** by adding a code block  `{ }`afterwards with the return type.
```ruby
# create a double that accepts no messages
dbl = double("Name")
# make dbl respond to the a_method message
allow(dbl).to receive(:a_method)
# make dbl respond to the a_method message with a pre-defined return
allow(dbl).to receive(:a_method) { 3 }

dbl.a_method => 3
```
You can use **expect with receive** to check if a method is called on an object during an `example` block. Below, the first example fails because `a_method` is never called during the block. In the second instance `a_method` *is* called at least once on the object so it passes. `expect` is separate from `allow` it does not check the object *can* receive a method only that it did.
```ruby
# failing expect / receieve
it "fails" do
	dbl = double("Name")
	expect(dbl).receive(:a_method)
end
=> F
# passing expect / receive
it "passes" do
	dbl = double("Name")
	expect(dbl).receive(:a_method)
	dbl.a_method
end
=> .
```
You can also combined `expect` with a pre-defined output block.
```ruby
# expect a method to be received and specify an output
dbl = double("Name")
expect(dbl).received(:a_mother) { 10 }
```
**Partial test doubles** allow you to temporarily overwrite or extend the functionality of a real object for the purposes of a test. It follows the same syntax pattern as doubles `allow(MyClass).to receive(:my_method) { my_return_value }` and references the class within your system. This can also be combined with any `subject` keyword and instance calls within your tests.
```ruby
class MyClass
	def my_method
		return 5
	end
end

it "returns a redefined value" do
	allow(MyClass).to receive(:my_method) { 0 }
	# where subject is an instance of MyClass
	expect(subject.my_method).to eq(0) => true
end
=> .
```
This also works with `expect` syntax shown above, to temporarily overwrite the output value *and* launch an example test for the method being called on the object

 **Redefinition stops outside of the block** in which it was created. However if you want to **add a double of partial double before every test** you should enclose the `allow(...).to receive(...)` inside a `before { }` block.

This is useful if you want to mock up the response of an object without effecting its functionality. For example, say we have a method in our object `random_number` which just returns a  random number that determines the state of our program in some way. When testing we want to check for all the states that this random number could create without just running our code over and over again to get all the possible states *or* changing the code in random number so that it outputs the numbers that we want for testing purposes. We can simply use **partial test doubles** to temporarily overwrite the output of `random_number` for the purposes of a test. You can see an implementation of this in the `Dice Messenger` kata of my [RSpec Katas][rkata] repo.

[rkata]: https://github.com/dpwdec/rspec-katas "RSpec Katas"

Its also possible to **check for receiving methods after they have been called** using the `have_received(:method)` at the end of an example block as a way to make code that matches the "given-when-then" syntax more effectively. Any double or double partial that can receive a method can have it checked with the `have_received` syntax.
```ruby
# using a double
it "passes" do
	dbl = double("Name", :method => 5)
	dbl.method
	expect(dbl).to have_received(:method)
end

# using a double partial
it "passes" do
	allow(MyClass).to receive(:method)
	MyClass.method
	expect(MyClass).to have_received(:method)
end
``` 

A **spy** is another way of creating a double that can respond to *any* method and work with the `have_received(:method)` in code. The implication here, is that by defining what was expected to be received at the end of the code you don't have to allow methods to run on a double.
```ruby
# using a spy
it "passes" do
	dbl = spy("Name")
	dbl.method
	expect(dbl).to have_received(:method)
end
```
`have_received()`can be **combined with other matchers** to check a range of different outcomes on what is received:
```ruby
# checks if the method was called 
# with arguments 1 and then 2 in that order
expect(my_object).to have_received(:method).with(1).ordered
expect(my_object).to have_received(:method).with(2).ordered
# checks if a method was called at least x number of times
expect(my_object).to have_received(:method).at_least(3).times
```
The **scope** of test doubles is limited to individual examples and will be destroyed and re-created after each test. Trying to create a mock object in a `context` level test will result in a `rspec-mocks outisde of the per-test lifecycle is not supported` error. 

You can put your code for defining test doubles inside a `before(:example) { # set up doubles }` block to keep your spec tests dry.

Its possible to define **temporary scopes** for doubles and use the output values of these with instance variables in your tests. This is done using the `RSpec::Mocks.with_temporary_scope { # set up RSpec block }` namespace code. I imagine that the main advantage of this is to show where derived values in your tests are meant to come from within the structure of your code.
```ruby
before(:context) do
    RSpec::Mocks.with_temporary_scope do
      dbl = double(:foo => 13)
      @result = dbl.foo
    end
  end

  it "passes" do
    expect(@result).to eq(13)
  end
```



> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbNDI3NDA0OTczLC0yMTEwODc2NTE0LDE2MT
M5MTE0MDksNzI4NDMxMTM5LC0xNjE4NDkyNjQ1LC0xMjI3OTI5
NTQxLDg2NDc3NDUxMSwtNzUwNDU5NDU1XX0=
-->