---
title: RSpec
layout: page
exclude: true
---

1. [Workflow](#workflow)
	1.1. [Scope](#scope)
	1.2. [Committing](#committing)
 2. [core](#core)
	 2.1. [subject scope](#subject-scope)
	 2.2. [shared context](#shared-context)
 3. [expectations](#expectations)
	 3.1. [collection matchers](#collection-matchers)
 4. [mocks](#mocks)
     4.1. [instance doubles](#instance-double)
3. [command line interface](#cli)

## Workflow

RSpec is a **domain specific language** that works as a testing framework which allows you to `expect` particular outputs from your code before you ever actually run it. This workflow means that you can you can manually generate error messages that inform you about the expected functionality of your code before you ever write a single line or "real" code.

Testing code in this way allows you to:
1. Ensure that your code works as intended before it is shipped.
2. Test sections of your code in isolation.
3. Communicate to other developers how your code should function.
4. Refactor your code cleanly.

The basic workflow in RSpec is to follow a **Red - Green - Refactor** coding loop. These steps are:
1. Write a test that will fail (because there isn't any code to pass it yet).
2. Write the code to pass the test.
3. Refactor the passing code maintaining its passing status.

This workflow ensures that you build your code with the intended functionality *and* when you refactor it you don't accidentally break it. If you make refactoring changes to your code *after* you have a passing test you can ensure that as long as your tests still pass after the refactor your code still works in the same way, despite its form or method being altered.

### Scope

You do not need to test `private` methods in RSpec. When testing we only want to confirm that our interface facing behaviour of our program is working correctly. Are we getting the correct inputs and outputs. A private method would only influence the internal parts of a class so it can be safely ignored as long our tests that measure the external outputs of our class are working as intended.

### Committing

You should `commit` when:
1. Your tests pass after writing a new piece of code.
2. Your tests pass after refactoring your code.

## Core
If you **do not define a top level `describe` value** for your tests then `subject` will default to a `String` that matches the top level name of your tests.

### Let
The `let` assigning function **goes out of scope when you move into a new `describe` block**. If you have nested `describe` blocks for classes, functions etc. then `let` name definitions will only persist within the describe block they were defined.
```ruby
describe MyClass do
  let(:my_variable) { 10 }

  it "returns the value of my variable" do
    puts my_variable
    # => 10
  end

  describe "#something else" do
    it "tries to return the value of my variable but errors" do
      puts my_variable
      # => No Name Error
    end
  end
end
```
The above example shows how `my_variable` goes out of scope when a new `describe` block is initialised. 

### Subject Scope
You should not use the `subject` keyword *inside* a `before` block. This is because `subject` is re initialised for each example.  In the below example we initialize `subject.message` in `before` but when we test the code with `expect` it returns nil, because `subject` was reinitialised as an empty object when the example was triggered.
```ruby
# FAILS
before do
  subject = described_class.new
  subject.message = "pops"
end
it "responds with pops to cocoa" do
  expect(subject.cocoa).to eq("pops")
end
# => Expected "pops" but got "nil"
```
This also means that you can't use `described_class` subject's with constructors that require arguments because when RSpec initializes the subject inside an example it will not submit the requisite arguments.
```ruby
# FAILS
before { subject = described_class.new("pops") }
it "responds with pops to cocoa" do
  expect(subject.cocoa).to eq("pops")
end
# => subject expected 1 argument but received 0
```
You **can use any sort of instance variables** from within a `before` block as well any **that refer to `described_class`**.
```ruby
# PASSES
before { @my_subject = desribed_class.new("pops") }
it "responds with pops to cocoa" do
  expect(@my_subject.cocoa).to eq("pops")
end
```
You **cannot use regular variables from within a `before`** block.
```ruby
# FAILS
before { my_subject = desribed_class.new("pops") }
it "responds with pops to cocoa" do
  expect(my_subject.cocoa).to eq("pops")
end
# => unitialized variable "my_subject"
```
If you want to **define the subject *before* each example** without the use of a custom instance variable (HINT: you *should* want to do this) then you must use a `subject { ... }` block at the `context` level.
```ruby
# Both example PASS because the subject block is run on each example
subject { described_class.new("pops")
it "returns a string to cocoa" do
  expect(subject.cocoa).to be_a_kind_of(String)
end
it "responds with pops to cocoa" do
  expect(my_subject.cocoa).to eq("pops")
end
```
After initializing `subject` using a `subject { ... }` block you **can alter the contents of subject from within `before`**. This actually an enforced feature as editing `subject` outside of an `it` literal can only be done from within a boock. See the example after this next one for that!
```ruby
# set up the subject object with a block
subject { subject.described_class.new("pops") }
# make changes and do further set up before each example
before { subject.messsage = "cops" }
it "responds with cops to cocoa" do
  expect(subject.cocoa).to eq("cops")
end
```
You can also just  **define (and alter) subject locally to an `it` block**:
```ruby
it "returns with pops to cocoa" do
  subject = described_class("pops")
  expect(my_subject.cocoa).to eq("pops")
end
```

---

You can **add a class description and a block description to a describe block** by submitting multiple comma separated arguments to the describe.
```ruby
describe MyClass, '#my_method' do
  # ... testing code
end
``` 
You can **create single like `it` blocks** using one-liner syntax combined with the `is_expected` keyword. When testing a method output with `is_expected` set the output of an object to the subject.
```ruby
# object one liner
subject { [1, 2, 3] }
it { is_expected.to not be_empty }
# method output one liner
subject { "Hello".upcase }
it { is_expected.to eq("HELLO") }
```
---
### Structure
Use `describe` blocks with a `#` or `.` appended to their beginning for each method that you are testing.
```ruby
describe ".include?" do
describe "#include?" do
```
Nest `context` within descriptions to indicate different paths and states that a method might encounter and `it` blocks to describe the expected output in clear terms. *Keep descriptions short!* [Better Specs][bs] suggests a description length capped at 40 characters.

[bs]: http://www.betterspecs.org/#short
```ruby
describe ".include?" do
  context "It contains element 3" do
    it "returns true" do
      expect(subject.include?).to be true
    end
  end
  context "It does not contain 4" do
    it "return false" do
      expect(subject.include?).to be false
    end
  end
```
Keep all `it` assertions separated unless the performance speed loss from separating them due to complex set at dependencies would several impact the functioning of your test suite.

Often you should prefer `let` over `before`, this is because "let is lazy" and so only runs when the object is needed.

Use [Mocks](#mocks) sparingly, while they will increase the speed of your tests they make tests less usable and reliable in general.

Avoid using the imperative form "should" when describing test outcomes. Instead use the third person prescriptive form "does".
```ruby
it "should not change" do # --> BAD
it "does not change" do # --> GOOD
```
---
### Shared Context
A **shared context** allows you to define re-usable context code for your examples. You can define a shared context inside a `shared_context` block that is separate from your main `describe` code. Shared context blocks **must be placed at the beginning** of your RSpec test file. You can **define instance variables, methods and** `let` **statements** inside a shared context. Instance variables must initialized inside a shared context must be contained in a `before` block.
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
---
### Pending Tests
You can define pending tests in your spec files by using the `pending` keyword in plac
## Expectations
A basic way to **test argument input values** is by expecting the output of the correct input to *not* raise an error.
```ruby
# testing that method accepts 2 integers as input
expect { subject.method(2, 10) }.to_not raise_error
```
You can **create a test for the number of arguments that a method should accept** by using the `respond_to` syntax.
```ruby
it { is_expected.to respond_to(:dock).with(1).argument }
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

#### Instance double
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
An `instance_double` **must be created inside an `it` example block**.

The class that the `instance_double` verifies with can be submitted as the literal class name *or* as a string. They can be **used interchangeably**.
```ruby
# both of these are valid constructors for a MyClass verifying double
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
# Even though MyClass impements my_method
# it wasn't explicitly allowed on this double
# so it fails
it "fails because method was not allowed" do
  my_class = instace_double(MyClass)
  my_class.my_method
  # => received unexpected message
end
```
`instance_double` will also **check the arity (number of input arguments) for a method** on a verifying double.
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
    my_checker.check(5)
  end
  # => .
  it "fails with wrong number of arguments" do
    my_checker = instance_double(Checker)
    allow(my_checker).to receive(:check) { "checked!" }
    my_checker.check(5, 10)
  end
  # => ArgumentError
end
```
`instance_double` will also **check for required keyword arguments** when called.
```ruby
class Bar
  # required argument is baz
  def foo(baz:)
    puts "output: #{baz}"
  end
end

describe Checker do
  it "passes with required arguments" do
    bar= instance_double(Bar)
    allow(bar).to receive(:foo) { "Barred!" }
    bar.foo(baz: 7)
  end
  # => .
  it "fails with no required argument" do
    bar= instance_double(Bar)
    allow(bar).to receive(:foo) { "Barred!" }
    bar.foo(7)
  end
  # => Missing required keyword arguments: baz
end
```
You can **use `instance_double` the `expect(...)` and `receive(...)` matchers** to confirm that doubles being called by other objects are being interacted with correctly. When doing this methods **do not** need to be `allowed` because they are just having their calls checked.
```ruby
class Mint
  def minty!
    # ..
  end
end

describe Mint do
  it "passes with a real method" do
    mint = instance_double("Mint")
    expect(mint).to receive(:minty!)
    mint.minty!
  end
  # => .
  it "fails with an unknown method" do
    mint = instance_double("Mint")
    expect(mint).to receive(:basket!)
    mint.basket!
  end
  # => does not implement method
end
```
`instance_double` can be **combined with `expect(...)`, `receive(...)`, `have_received(..)` and `with` methods** to create matchers for methods called on verifying doubles. The code below passes a verifying double of the `Notifier` class to a new instance of `Caller` with an `expect` block the `create` method to be called on the double.
```ruby
class Caller
  def initialize(notifier)
    @notifier = notifier
  end

  def notify!
    puts @notifier.create("re-call", 12)
  end

  def reiterate!
    puts @notifier.profile("input", 20)
  end
end

class Notifier
  def create(name, times)
    # ...
  end
end

describe Caller do
  it "passes by calling create on notifier" do
    note = instance_double("Notifier")

    expect(note).to receive(:create).with("re-call", 12) { "re-called 12" }
    
    caller = Caller.new(note)
    caller.notify!
  end
  # => .
  it "fails by calling profile on notifier" do
    note = instance_double("Notifier")

    expect(note).to receive(:profile).with("input", 20) { "input 20" }
    
    caller = Caller.new(note)
    caller.reiterate!
  end
  # => Instance does not implement profile
end
```
Had an `instance_double` not been used in the above code the second example would have actually passed because (even though that situation would have had no relation to the actual functioning of our code) because a normal double would not check for any verification with the original object and would have only verified that the double received a message.

### Private Instance Variables

Sometimes you will want to set the value of private instance variables of a class for the purpose of running tests. Consider the following classes.
```ruby
class MyClass
  def initialize
    @my_object = MyObject.new
  end

  def get_report
    @my_object.report
  end
end

class MyObject
  def report
    return "Reporting!"
  end
end
```
`MyClass` contains a private instance variable `@my_object` which is an instance of `MyObject`. We do not want this variable to be publicly available to the rest of our program during normal functioning but we *do* want to interact with it during testing to influence the behaviour of `MyClass`. For example, **what if we wanted to created a mock of `@my_object`** inside `MyClass`? This wouldn't be possible because that variable is private, but we still need to assign it as an RSpec mock to check some functionality. To do this we can use the `instance_variable_set` method. This allows to assign a private instance variable on an object as long as you know its names. The first argument specifies the name of the instance variable as a symbol and the second argument is the value that you want that variable to be assigned to.
```ruby
describe MyClass do
  it 'has a mock object' do
    dbl = instance_double(MyObject, :report => "No Report!")
    subject.instance_variable_set(:@my_object, dbl)
    expect(subject.get_report).to eq('No report!')
  end
end
```
This works as intended with the `subject`'s private instance variable being replaced by our mock object that returns a different value when the `report` function is called.

## CLI
You can run a specific RSpec tests by specifying a line number from the tests that falls within a block. For example if you had a test block which started on line 9, you could run *only* that test by using.
```
rspec ./spec/myclass_spec.rb:9
```
> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbNzQ2MjEzNTE5LC02NjkzOTYxODUsMjY1Nj
QxNDU3LC04ODY3NDQ0OTksMTcxNjgyMDQyNCwtOTQ2MTYyOTcx
LDE2NzUyMDgwNDQsLTE5MzM3ODgwMjksLTk0MDU4NTEwNSwtMT
E2ODYyMjEyMCw1NTY2NTQ1MCwxMTA1NTE0NTMxLDE0MTUxNjc5
MDQsLTYxNzIyMTI1OSwtMTk3Nzc1MzM1MCwzODA3NDkxNjEsLT
I2MDUzNzA0MiwxNzM1NDIwMjEzLDE3Njc3MDU3MCwtMTk5MzI0
ODE0OV19
-->