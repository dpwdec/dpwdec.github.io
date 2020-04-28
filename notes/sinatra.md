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
eyJoaXN0b3J5IjpbLTE2MjMxMjY2NTMsNzcxNzIyMTUxXX0=
-->