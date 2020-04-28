---
layout: page
title: Ruby
exclude: true
---
## Strings
You can **convert an integer into a string** `char` by running the `.chr` method on it.
```ruby
(65).chr
# => 'A'
```
You can **split single strings over multiple lines** by using backslash outside of the string new-line separators.
```ruby
multi_line_str = "This is"\
"a string tha"\
"is split over"\
"multiple line"\
"s"
# => "This is a string that is split over multiple lines"
```
## Booleans
You can assign the output of a boolean operation directly from a bool.
```ruby
my_bool = 10 < 20
# => true
```

## Arrays
If you want to **return a single value from an array based on some condition** use the `detect` method. This is different from the `select` method in that it only returns a single result, whereas the latter returns a sub-array of possible results even when there is *only one* possibility.
```ruby
[1, 2, 3].detect { |n| n == 3 }
# => 3
# Select as well for comparison
[1, 2, 3].select { |n| n == 3 }
# => [3]
```

## Hashes
You can have **any arbitrary object as a key** in a hash. This can be useful if you have other information stored in your `key_object` that you want to access while still binding that object temporarily to some information in your hash.
```ruby
key_object = Object.new
my_hash = Hash.new
my_hash[key_object] = 1
```
You can **use the `inject` method with a hash to create a cumulative count of its values**. This works by the block variables coming in the form of an accumulator variable and a hash variable which represents the key-value pair in an array for that iteration through the loop. In the example below on the first iteration through `|count|` will equal `0` and `|hash|` will be an array of `["one", 1]` so to access the value `1` and add it to the `count` we access it with index `[1]` from the `hash` array as it is the second element in that array that represents a single key-value pair of that hash. On the next loop `count` will equal `1` and `hash` will now contain the second key-value pair of the hash as an array, i.e. `["two", 2]`.
```ruby
my_hash = { "one" => 1, "two" => 2, "three => 3" }
my_hash.inject(0) { |count, hash| count + hash[1] }
# => 6
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

## Methods
You can submit to a splat operator via a an array by appending the array with an `*` asterisk. This allows you to assign all the splat arguments as an array without submitting them manually.
```ruby
def my_method(*args)
  args.each do |arg|
    puts arg
  end
end

arguent_array = [1, 2, 3]
my_method(*argument_array)
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
#### Loading gems
You can **specify a gem to use in your project** by simply writing the `gem` command with the name of the gem. When this line is read by the `bundle` command it will then go to the `source` you specified and retrieve the gem of that name.
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
gem "my_gem", "<1.0" # give me a version of my gem less than 1.0
```
There are also a **pessimistic gem version specifier** using the `~>` which works by allowing any gem that matches a specific prefix range of gem versions.
```ruby
gem "my_gem", "~> 2.0" # give me a version of my gem that is in the category 2.0, i.e. won't return any 3.0 version gems
gem "my_gem", "~> 2.5.0" # give me a version of my gem that is in the category 2.5.0 won't return any 2.6.0 version gems
``` 
For example in the second example above gem version `2.5.11` would be valid, as would `2.5.3` but `2.6.0` or `2.4.9` would not be. This seems very unintuitive on the surface but **it is essentially a shortening of writing a compound operator**.
```ruby
gem "my_gem", "~> 2.0"  = gem "my_gem", ">=2.0, <3.0"
gem "my_gem", "~> 2.5.0"  = gem "my_gem", ">=2.5.0, <2.6.0"
```

#### Groups
You can group your ruby gems inside your `Gemfile`. If you don't explicitly give a gem a group then it will go into the `default` group. You can **specify a gem's group** by appending the `group:` argument to the gem's definition.
```ruby
# assigning my_gem in the development group
gem "my_gem", group: :development
```
Groups allow you to **selectively install gems based on groups**. For example running `bundle install --without my_group` will install everything apart from gems in the `my_group` group. You can also **assign multiple gems to a single group** using blocks.
```ruby
group :development do
  gem "my_dev_gem"
  gem "my_db"
end
```
The above code will place the `my_dev_gem` and `my_db` gem in the `:development group`. This can be **expanded to assign multiple groups to gems simultaneously** as well.
```ruby
group :development, :test do
  gem "my_dev_gem"
  gem "my_db"
end
```
In the above example the gems are now placed in *both* the `:development` and `:test` groups. You can specify a group multiple times as well. For example later in the above example you might write `gem "some_other_gem", group: :test` which would then include that newly added gem to just the `test` group while keeping the `my_dev_gem` and `my_db` gem also in that group.

#### Require

The `require` gem modifier is a function designed to work with Rails. When setting up a Rails project there will be `config/application.rb` that will call `Bundler.require` which will load all gems *unless* they have the `require: false` function added to them. The reason you might want to do this is if you have to manually want to set up gem installation including this gives you the option.
```ruby
gem "my_gem", require: false
```
**`Bundler.require` can have the names of different groups added to it and load them**. For example `Bundler.require(:default, Rails.env)` will load all gems in the `default` group and all gems in a group that matches the current `Rails.env`ironment.  You can submit an arbitrary list of groups to `require` such as `Bundler.require(:default, :test, :development)`.



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
You can **`require` multiple classes in the irb** simultaneously by requiring them with the following snippet of code. This finds all files with the `.rb` extension and loads them.
```
Dir["/path/to/directory/*.rb"].each {|file| require file }
```

## Environment Variables
You can **access environment variables** in Ruby using the `ENV` object. This works just like a hash where you submit the name of the environment variable as a string to retrieve its value.
```ruby
my_var = ENV['MY_VAR']
```
You can **get the size of the environment variables list** using the `.size` method.
```ruby
ENV.size
```
You can **return a list of environment variable keys** using the `.keys` method.
```ruby
ENV.keys
```
You can even **iterate through the `ENV` object's entries**.
```ruby
ENV.select  { |key ,value | key.size < 4  }
```

## TCPServer
The `TCPServer` class is a simple class for creating a `TCP/IP` server socket to send a receive information in ruby. You can **start a server** by creating a new instance of the `TCPSserver` class.
```ruby
server = TCPServer.new(2345)
```
You can then contact this server using the `Telnet` command line tool and connecting to your `localhost` and the port number the server is listening at.

You can use `server.accept` to **create an objet that processes information like the command line** on your web server. This allows to use methods like `gets` and `puts` to pass information to the server and perform actions on it, or output information to the client.
> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE3NzcxMTEwMTcsLTU4OTMxODE5MCwxND
czMTgyNTgzLDE0ODkyMTYxOTIsLTE5NTM2MTcxNiwtMzM0MzU5
MzA4LC05ODc0Njc2MjMsLTg3NDc3MTI1NSwtMTk3MjE3MTM2NS
wxMDQ2MTY0NDYsOTkxNjgxMDU0LC0xMjEzOTg4NTQwLC0yOTIy
MTc0MjksOTU3NTg4MDgzLDE0OTU4NzQ1MSwxNjA5MDI2NDE2LD
k2MTA1NzU2NywxMjk3OTc2NzQ5LC04MjI1MTg0NywxNDg0OTU3
NDVdfQ==
-->