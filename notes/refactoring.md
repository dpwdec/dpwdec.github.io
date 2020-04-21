---
title: Refactoring
layout: page
exclude: true
---
Code comments that mention elements of your code with an apparent name *should* match the names in code. For example:
```ruby
# combines result of adding two words and puts them with a message.
def combine_words(word_1, word_2)
  puts("The two words together are " + word_1 + word_2)
```
This is a bad example of how to structure your code and comment names because our method comment makes reference to a `#result` and `#header` but these are never referenced in our actual code. A better solution would be:
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
eyJoaXN0b3J5IjpbNTg2NDQzODc2LC01NTIzMjgyMzYsLTIwNT
Q0NzU0MDYsMTg0NTMyNTA4MywtMjA1NDQ3NTQwNiwtODU2MDUx
MTE3XX0=
-->