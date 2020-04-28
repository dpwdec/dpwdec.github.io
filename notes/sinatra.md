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

To **stop a Sinatra server** use `CTRL + C` in the command line window where the server is running.

When changing files in your Sinatra project you will need to start and restart the server to see those changes propagated to the web pages displayed online.

### Shotgun
[Shotgun](https://github.com/rtomayko/shotgun) is another ruby gem that can be used to **automatically restart your Sinatra server** after changes are made. To install simply add the `gem Shotgun` line to your `Gemfile`. You can then

## Routes
You can **specify different web pages to return** by using an *HTTP Verb* combined with a string representing the page name and a block that display or loads the content for that page.
```ruby
# Basic sinatra route
get '/' do
  'Hello World'
end
```
The example above defines how to respond to a `GET` request from a client to the root URL of the server. In this case it returns the string `Hello world` which is then displayed in plain text by the browser. You can insert HTML as a string, for example `'<h1>Hello World</h1>'`, into the route block, but this is not advised!


> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjMzMDgwODQwLDc3MTcyMjE1MV19
-->