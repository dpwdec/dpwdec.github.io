---
layout: page
title: Ruby
exclude: true
---
## Strings
You can convert an integer into a string `char` by running the `.chr` method on it.
```ruby
(65).chr
=> 'A'
```

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

## Other data structures
A **set** is a data storage object  that functions similarly to an array, the main difference being that it is *limited to containing unique elements* or no duplicate elements. You may need to `require 'set'` to use the set object. To create a set:
```ruby
# new set
my_set = Set[1, 3, 4]
# to add a new element
my_set.add(6) # => {1, 3, 4, 6}
# adding a duplicate element changes nothing
my_set.add(4) # => {1, 3, 4, 6}
```
You can **merge sets together**:
```ruby
set_1 = Set[1, 2]
set_2 = Set[3, 4]
set_1.merge(set_2) #=> {1, 2, 3, 4}
```
You can also do return as a boolean whether one set is a **subset** of another set:
```ruby
set_1 = Set[1, 2, 3, 4]
set_2 = Set[3, 4]
set_2.subset?(set_1) # => true
set_1.subset?(set_2) # => false
```
## Gems
Gems are pieces of reusable code that can be installed inside your ruby projects. 

You can **search for a gem from the ruby command line** using:
```
gem search GEM_NAME
```
You can **download a gem without installing it** using the `feth` command and then `unpack` the gem to see its contents which will display the gem's contents as a directory in your project that can be interacted with.
```
gem fetch rails
gem unpack rails
```
You can rebuild an unpacked gem using:
```
gem build GEM_SPEC
```
The basic structure of a gem is:
```
dpwdec/
├── bin/
│   └── dpwdec
├── lib/
│   └── dpwdec.rb
├── test/
│   └── test_dpwdec.rb
├── README
├── Rakefile
└── dpwdec.gemspec
```

 - The **bin** directory contains an executable that is added to the user's `$PATH` when the gem is installed.
 - The **lib** directory contains the code that the gem runs on
 - The **test** directory contains verification tests for the gem
 - The `README` contains documentation information about the code and how to use it.
 - The **rake file** is a `rake` program that performs utility tasks on the gem.
 - The **gemspec** file contains information about the gem such as version, author, homepage etc.

## Kernal Commands

> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTQ5NTI1ODk2LC0xNTkzMjM2MDQ5LDIwNj
gzNTAzMzQsLTExMjUxMDU5ODUsLTExNTk1MjcwNDFdfQ==
-->