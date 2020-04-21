---
title: Refactoring
layout: page
exclude: true
---
## Basic VMC Refactoring
Basic refactoring follows a pattern of extracting variables, then methods then classes, or VMC. By slowly extricating different pieces of our code we can start to created more cohesive encapsulated programs with well organised modules of functionality.

### Variable Extraction

Code that is all compressed onto one line without the use of variables can confuse the different pieces of functionality that a method might have. 
```ruby
# combines result of adding two words and puts them with a message.
def combine_words(word_1, word_2)
  puts("The two words together are " + word_1 + word_2)
end
```
In the code above, the combining functionality *and* the printing functionality are combined onto a single line. Even though these are separate responsibilities they appear entwined when presented this way in the body of our method. Furthermore the lack of variables means that the code comments are widely redundant, because even though we makes reference to a `#result` and `#header` these are never referenced in our actual code. 
```ruby
# combines result of adding two words and puts them with a message.
def combine_words(word_1, word_2)
  message = "The two words together are "
  result = word_1 + word_2
  puts(message + result)
end
```
We can see in the code above the elements have been refactored into separate variables making the functionality of this method more clear.

### Method Extraction
After clarifying the above examples functionality with variables we can see that this method has more than one responsibility:

1. Adding the words together
2. Outputting the result.

This means that we could refactor the code further to have a method that outputs words rather than doing the combining *and* the printing *inside* the `combine_words` method. In the below example this refactoring has been completed and because the `print_words` method is not used by any code outside of the `combine_words` method it can be safely set as `private`. Note: I've also amended this code to now be wrapped in a class `Words`, however this was intended to be implicit in the above examples.
```ruby
class Words
  def combine_words(word_1, word_2)
    result = word_1 + word_2
    print_words(result)
  end

  private
  def print_words(result)
    message = "The two words together are "
    puts(message + result)
  end
end
```
We now have clear responsibilities based on different methods within this class, each piece of code has a clear responsibility and does exactly what it says it does.

Don't be afraid to extract a line with multiple clauses into multiple methods.
```ruby
def checker
  time < 5 && location == "home"
end
```
The method above has two evaluation clauses inside it that can be refactored into two separated predicate methods.
```ruby
def checker
  time? && home?
end

def time?
  time < 5
end

def home?
  location == "home"
end
```

### Extract Class

If you can extract a method within a class into a separate `private` method which the class delegates responsibility to, there is a good chance that you can extract this method into its own class.

In our example we could probably refactor the `print_words` method into its own class entirely as printing stuff doesn't really have anything to do with managing how words interact.
```ruby
class Words
  def combine_words(word_1, word_2)
    result = word_1 + word_2
    Printer.new.print_words(result)
  end
end

class Printer
  def print_words(result)
    message = "The two words together are "
    puts(message + result)
  end
end
```
Now out code is clearly managed by two separate classes that interact keeping responsibilities entirely separated.

### Other extractions
We can go a little further with the above example. Currently the message in the `Printer` class is always the same, so it can be safely extracted into a constant. Furthermore the `Words` class could implement an instance variable that contains an instance of the `Printer` class so it doesn't need to create a new printer every time the `combine_words` method is called.

```ruby
class Words
  def initialize
    @printer = Printer.new

  def combine_words(word_1, word_2)
    result = word_1 + word_2
    @printer.print_words(result)
  end
end

class Printer
  MESSAGE = "The two words together are "

  def print_words(result)
    puts(MESSAGE+ result)
  end
end
```

## General Refactoring Patterns
### Three instances of repetition
When should you refactor? There is a balance to be struck between refactoring too early by second guessing how your code base will evolve and refactoring too late when there are so many problems with your code that changes become difficult. The rule of thumb is to **refactor when you see three or more instances of code duplication**. You can then be sure that you are seeing a code pattern that will need to dried and extracted.

## Code review

Code reviews are usually conducted once a pull request has been made on github as a way of ensuring the quality of code before it is merged into the main project.

To offer feedback on pull request code visit the `pull request` of your repo and select the request you want to review. You can see new additions in the request's code by going to `changed files` tab which displays additions and removals is green and red respectively.

You can leave comments on single or multiple lines by using the `+` symbol next to code lines and "adding a comment". 
> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzNDUxMTk4NzgsMjEwNDM4MjI4MiwtMT
I3NjYzMDE2MSwxODI4NzMwODY5LDE3NDg4MTg1MDQsMTE1NTEx
OTI3LC01NTIzMjgyMzYsLTIwNTQ0NzU0MDYsMTg0NTMyNTA4My
wtMjA1NDQ3NTQwNiwtODU2MDUxMTE3XX0=
-->