---
layout: page
title: Ruby
exclude: true
---

## Objects
You can **call an object method by name** by using `send` to push the method to an object as a message instead of calling it directly with the `.` syntax.
```ruby
"hello".send(:upcase)
=> "HELLO"
# this is the same as
"hello".upcase
=> "HELLO"
```
> Why would you want to do this?

This allows you to store methods that you might want to call as a list of symbols that can then be iterated through very cleanly and called on an object. Furthermore if you have an object method that returns a list of methods it responds to as an array of symbols you can easily iterate through that array and call these methods.


> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTExNTk1MjcwNDFdfQ==
-->