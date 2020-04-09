---
title: RSpec
layout: page
exclude: true
---
## Core
A **shared context** allows you to define re-usable context code for your examples. You can define a shared context inside a `shared_context` block that is separate from your main `describe` code. You can **define instance variables, methods and** `let` **statements** inside a shared context. Instance variables must initialized inside a shared context must be contained in a `before` block.
```ruby
# defining a shared context
shared_context 'context name' do
  before { @some_var = 10 }
  let(:another_var) { 20 }
  def shared_method
    return "This is a shared method."
  end
end
```
You can **invoke a shared context** by placing it inside a `context` block with the `include_context` method and the name of the context. Objects and methods define in the shared context can then be called from your example testing code as if they had been defined inside that context's scope.
```ruby
# call a context
context "my shared context" do
  include_context 'context name'
  # testing a shared context instance variable
  it "should return 10 for some_var" do
    expect(@some_var).to eq(10)
  end
  # testing a shared context let variable
  it "should return 20 for another_var" do
	  expect(another_var).to eq(20)
  end
  # testing a shared context method
  it "should return 'This is a shared method'" do
    expect(shared_method).to eq("This is a shared method.")
  end
end
```
You **cannot:** 

 - Use the `subject` keyword inside the `before` block of a shared context.
 - Define variables outside of a `before` block. 
 - Define non-instance variables unless through a `let` method.
 
```ruby
# INVALID object initialization:
shared_context "non functional context" do
  # subject will not be initialized with input
  # when called in an example
  before do
    subject = described_class.new(:input)
    subject = MyClass.new(:input)
    # non instance variables are not valid unless
    # defined using let
    my_var = MyClass.new(:input)
  end
  # initialization of a variable outside a before 
  # block will result in a Nil return type when called
  my_var = MyClass.new(:input)
  @my_var = MyClass.new(:input)
end
```
It is however **valid to use** the `described_class` syntax within a shared context - the class instantiated will be taken implicitly from the `describe` block which your `include_context` statement appears in. You can also **initialize subject from a shared context** using a `let` block.
```ruby
# VALID object initialization
shared_context "my context" do
  before
    @class_instance = MyClass(:input)
    @described_instance = described_class.new(:input)
  end
  let(:class_instance) { MyClass(:input) }
  # initialize subject as instance of described class
  # with shared contextual settings
  let(:subject) { described_class.new(:input) }
end
```
It is possible to define variables outside of a `before` or `let` block within a shared context block providing you only intend to use those variables within the scope of the shared context code.
```ruby
# variable defined and used within shared context scope
shared_context 'context name' do
  input_var = 10
  let(:my_object) { MyClass.new(input_var) }
end
```
## Expectations
A basic way to **test argument input values** is by expecting the output of the correct input to *not* raise an error.
```ruby
# testing that method accepts 2 integers as input
expect { subject.method(2, 10) }.to_not raise_error
```
### Include matchers
You can **check the contents** of a hash's key-value pair by using the `include` matcher with any arbitrary *and* literal hash input as its argument.
```ruby
my_hash = { "a" => 2, :b => 3 }
it "contains kv pair 'a':2 and kv pair b:3" do
  expect(my_hash).to include("a" => 2)
  expect(my_hash).to include(:b => 3)
  # testing for multiple key-value pairs
  expect(my_hash).to include("a" => 2, :b => 3)
end
```

### Collection matchers:
Collection matchers have been [removed][colremove] from RSpec expectations. To do collection matching you should now use the [`rspec-collection_matchers`][rscm] gem to run collection matching expectations. To **install collection matching gem** use:
```
gem install rspec-collection_matchers
```
Collection matchers allow you to check size and structure of collections without referencing their collection attributes (such as `.length`) directly. You must `require` collection matchers to use the collection matching code.
```ruby
require 'rspec/collection_matchers'
it "matches the number of items in a collection" do
  expect([1, 2, 3]).to have_exactly(3).items
end
```
[colremove]: [https://stackoverflow.com/questions/24111204/rspec-to-haven-items-undefined-method](https://stackoverflow.com/questions/24111204/rspec-to-haven-items-undefined-method)
[rscm]: [https://github.com/rspec/rspec-collection_matchers](https://github.com/rspec/rspec-collection_matchers)
## Mocks
### Basics
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
You can use **expect with receive** to check if a method is called on an object during an `example` block. Below, the first example fails because `a_method` is never called during the block. In the second instance `a_method` *is* called at least once on the object so it passes. `expect` is separate from `allow` it does not check the object *can* receive a method only that it did. The method **must be called after the receive** statement for this to work.
```ruby
# failing expect / receieve
it "fails" do
  dbl = double("Name")
  expect(dbl).to receive(:a_method)
end
=> F
# passing expect / receive
it "passes" do
  dbl = double("Name")
  expect(dbl).to receive(:a_method)
  dbl.a_method
end
=> .
```
You can also combined `expect` with a pre-defined output block.
```ruby
# expect a method to be received and specify an output
dbl = double("Name")
expect(dbl).to receive(:a_method) { 10 }
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
# => .
```
This also works with `expect` syntax shown above, to temporarily overwrite the output value *and* launch an example test for the method being called on the object

You can **use the `with` matcher appended to receive to check if a method receives a particular set of arguments.**
```ruby
it "passes by receiving a method with argument 1" do
  dbl = double
  expect(dbl).to receive(:a_method).with(1)
  dbl.a_method(1)
end
# => .
it "fails by receiving a method with arugme '1'" do
  dbl = double
  expect(dbl).to receive(:a_method).with(1)
  dbl.a_method("1")
end
# => F
```
`with` can be **used with regular expressions** to match a range of different potential input arguments. In the example below it is also placed in a `before` block so that it can be run before 
```ruby
describe "method argument matching" do
  let(:dbl) { double }
  before { expect(dbl).to receive(:a_method).with(/ab/)
  it "passes absolute" do
    dbl.a_method("absolute")
  end
  it "passes abdominals" do
    dbl.a_method("abdominals")
  end
  it "fails acting" do
    dbl.a_method("acting")
  end
end
```
The `anything` keyword can be used **to match `with` to any potential argument input**.
```ruby
describe "matching with anything" do
  let(:dbl) { double }
  before { expect(dbl).to receive(:a_method).with(anything)
  it "passes nil" do
    dbl.a_method(nil)
  end
  it "passes string" do
    dbl.a_method("hello")
  end
  it "passes int" do
    dbl.a_method(10)
  end
end
```
These `with` queries **can be combined arbitrarily for testing multiple arguments**.
```ruby
expect(dbl).to receive(:a_method).with(1, anything, /abs/)
```
 **Redefinition from a double stops outside of the block** in which it was created. However if you want to **add a double of partial double before every test** you should enclose the `allow(...).to receive(...)` inside a `before { }` block.

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
### Verifying doubles
Double verification allows you to **ensure that your double's methods and attributes match a real object**.

An `instance_double` represents an instance of a real class and can **verify that it really does receive a specified method**. Attempting to add a method to a verifying double that does not exist on the class that double is attempting to mock will result in an error. Apart from this functionality **verifying doubles work in the same way as regular doubles**.
```ruby
class MyClass
  def my_method
    return "hello"
  end
end

describe MyClass, '#my_method' do
  # verifies that my_method exists
  it "creates a working verified double" do
    my_class = instance_double(MyClass, :my_method => "Goodbye")
    my_class.my_method
  # => "Goodbye"
  end
  it "creates a failing verified double" do
    # errors when you try to add a method that 
    # doesn't exist on the original class
    my_class = instance_double(MyClass, :another_method => "Hello")
    # => the MyClass class does not implement the instance method another_method
  end
end
```
An `instance_double` must be created inside an `it` example block.

The class that the `instance_double` verifies with can be submitted as the literal class name *or* as a string. They can be **used interchangeably**.
```ruby
# both of these are valid constructors for a
# MyClass verifying double
my_class = instance_double(MyClass)
my_class = instance_double("MyClass")
```
`instance_double` can also be used with the `allow(...)` and `receive(...)` syntax.
```ruby
my_class = instance_double("MyClass")
# working method stubbing with verification
allow(my_class).to receive(:my_method) { "Goodbye" }
# failing method stubbing with verification
allow(my_class).to receive(:another_method) { "Bye!" }
# => the MyClass class does not implement the instance method another_method
```
`instance_double` like normal doubles **do not automatically allow methods from the class it is verifying**. These methods *must* be added using `allow` even if they exist on the verified class.
```ruby
it "passes because method is allowed" do
  my_class = instance_double(MyClass)
  allow(my_class).to receive(:my_method) { "Goodbye" }
  my_class.my_method
end
# Even though MyClass impement my_method
# it wasn't explicitly allowed on this double
# so it fails
it "fails because method was not allowed" do
  my_class = instace_double(MyClass)
  my_class.my_method
  # => received unexpected message
end
```
`instance_double` will also check the arity (number of input arguments) for a method on a verifying double.
```ruby
class Checker
  def check(n)
    puts "checked #{n}"
  end
end

describe Checker do
  it "passes with correct number of arguments" do
    my_checker = instance_double(Checker)
    allow(my_checker).to receive(:check) { "checked!" }
    my_checker(5)
  end
  it "fails with wrong number of arguments" do
    my_checker = instance_double(Checker)
    allow(my_checker).to receive(:check) { "checked!" }
    my_checker(5)
  end
end
```
> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE0MTc3MTE0ODcsMTgzNzMzMzA2OCw0Nj
A1Njk5MywtMTIwNTA5NTk5MSwtMTEzNzU4NzY4NywtMTM2MzY0
Nzg5NiwtMjA4NjE0ODk3MywxNTY0NTc2MzMwLDg1NTU4Nzc4Ny
w1MDEzODc4MDQsLTgwNTYzMjM0NiwxODUyNTU3NDMsMTIwMDY0
NTc3OCw2NTg1NzA3MzYsLTM3NjY1MTcyLDQ5MjcyOTcyNiwxNj
UyNTQxMjY0LDEyMTY0Nzc0OTksMzQ1Nzg5NDg5LC0yMTc1MDg1
MjldfQ==
-->