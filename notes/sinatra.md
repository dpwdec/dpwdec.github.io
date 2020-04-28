---
title: Sinatra
layout: page
exclude: true
---
Sinatra is a lightweight web framework for building small web applications in ruby.

## Start up
You can **install Sinatra** by simply including the `gem Sinatra` in your `Gemfile` and running the `bundle` command.

You can **start a Sinatra app running** i.e. listening and functioning as a server by using the `ruby` command in the terminal to run whichever is the main file in your Sinatra project.
```
ruby myapp.rb
```
This should be the file in which your different web page routes and defined.

## Routes
You can **specify different web pages to return** by using an *HTTP Verb* combined with a block that display or loads the content for that page.
```ruby
get '/'
```

> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE2MTEzMzMwNSw3NzE3MjIxNTFdfQ==
-->