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

```
In the code a, the combining functionality *and* the printing functionality are combined onto a single line. Even though these are separate responsibilities they appear entwined when presented this way in the body of our method. Furthermore the lack of variables means that the code comments are widely redundant, because even though we makes reference to a `#result` and `#header` these are never referenced in our actual code.

```ruby
# combines result of adding two words and puts them with a message.
def combine_words(word_1, word_2)
  message = "The two words together are "
  result = word_1 + word_2
  puts(message + result)
end
```

If you can extract a method within a class into a separate `private` method which the class delegates responsibility to, there is a good chance that you can extract this method into its own class.


## Code review

Code reviews are usually conducted once a pull request has been made on github as a way of ensuring the quality of code before it is merged into the main project.

To offer feedback on pull request code visit the `pull request` of your repo and select the request you want to review. You can see new additions in the request's code by going to `changed files` tab which displays additions and removals is green and red respectively.

You can leave comments on single or multiple lines by using the `+` symbol next to code lines and "adding a comment". 
> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE5OTgxNzg1NDcsLTU1MjMyODIzNiwtMj
A1NDQ3NTQwNiwxODQ1MzI1MDgzLC0yMDU0NDc1NDA2LC04NTYw
NTExMTddfQ==
-->