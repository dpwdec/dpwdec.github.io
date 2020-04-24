---
layout: page
title: Ruby
exclude: true
---
## Strings
You can convert an integer into a string `char` by running the `.chr` method on it.
```ruby
(65).chr
# => 'A'
```
## Booleans
You can assign the output of a boolean operation directly from a bool.
```ruby
my_bool = 10 < 20
# => true
```

## Arrays


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

### Delegators

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

### Gem Files
A gem file set of code that can be extracted into a list of dependencies which your program uses to run. Gem files are written and evaluated as ruby code which allows you to use a range of ruby syntax and methods within them. 

You can **initialize a new `Gemfile`** within a directory by running the `bundle init` command. If you create the `Gemfile` manually it **must be named with a capital "G"**.

The **first thing a gem file needs is a `source`** from which gems will be fetched. This is a method that you "point" at a valid rubygems directory in the method's argument. For almost all projects this will just be `rubygems.org`. It's recommended to **not have more than one `source`** per project.
```ruby
source "https://rubygems.org:"
```
You can **specify the version of ruby** that you want to use in your `Gemfile` with the `ruby` command. You can also optionally specify other parameters like `:engine` and `:path_level` in this command.
```ruby
ruby "2.7.0"
```
You can s**pecify a gem to use in your project** by simply writing the `gem` command with the name of the gem. When this line is read by the `bundle` command it will then go to the `source` you specified and retrieve the gem of that name.
```ruby
gem "my_gem"
```
This can be combined with **defining the version of a gem you want** using basic comparison operators in a second argument with the version you are working on.
```ruby
gem "my_gem", "=1.0" # give me version 1.0 of my gem
gem "my_gem", "!=1.0" # give anything but version 1.0 of my gem
gem "my_gem", ">=1.0" # give me version 1.0 or greater of my gem
gem "my_gem", "<=1.0" # give me version 1.0 or less of my gem
gem "my_gem", ">1.0" # give me a version of my gem greater than 1.0
gem "my_gem", "<1.0" # give me a version of my gem greater than 1.0
```

## Kernel Methods
Kernel methods are a module that is mixed into Ruby's `Object` class and contains methods like `puts`.

You can use the `p()` method to help debug code. This method outputs the equivalent of `object.inspect` to the standard output.
```ruby
[1, 2, 3].each do |num|
  p num
end
# => 1, 2, 3
```

## IRB
You can load classes and ruby file into the irb using the `require` and `require_relative` keywords. I mostly use `require_relative` which initializes a file path that is relative to the directory from which you start the irb. For example, in the following directory if you were running an irb instance from `my_diretory` and wanted to include the `my_class.rb` files contents you would use `require_relative "classes/my_class.rb"`. However, if you executed the irb from within the `classes` directory you could reference the `my_class.rb` file with `require_relative "my_class.rb"`.
```
my_directory
├── classes/
     └── my_class.rb
```

> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTAxNDU0NDk5OCwtMjkyMjE3NDI5LDk1Nz
U4ODA4MywxNDk1ODc0NTEsMTYwOTAyNjQxNiw5NjEwNTc1Njcs
MTI5Nzk3Njc0OSwtODIyNTE4NDcsMTQ4NDk1NzQ1LC0xNTkzMj
M2MDQ5LDIwNjgzNTAzMzQsLTExMjUxMDU5ODUsLTExNTk1Mjcw
NDFdfQ==
-->