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
ruby my_app.rb
```
This should be the file in which your different web page routes and defined.

To **stop a Sinatra server** use `CTRL + C` in the command line window where the server is running.

When changing files in your Sinatra project you will need to start and restart the server to see those changes propagated to the web pages displayed online.

### Shotgun
[Shotgun](https://github.com/rtomayko/shotgun) is another ruby gem that can be used to **automatically restart your Sinatra server** after changes are made. To install simply add the `gem Shotgun` line to your `Gemfile`. You can then run the server using the `shotgun` command instead of the `ruby` command so that it is automatically restarted when changes to the code are made.
```
shotgun my_app.rb
```

## Routes
You can **specify different web pages to return** by using an *HTTP Verb* combined with a string representing the page name and a block that display or loads the content for that page.
```ruby
# Basic sinatra route
get '/' do
  'Hello World'
end
```
The example above defines how to respond to a `GET` request from a client to the root URL of the server. In this case it returns the string `Hello world` which is then displayed in plain text by the browser. You can insert HTML as a string, for example `'<h1>Hello World</h1>'`, into the route block, but this is not advised!

## Modular Style

Sinatra's **modular style** allows you to create classes that inherit from `Sinatra::Base` class and contain the app code views for your 

## Views
You can load HTML to display on pages as a dependency by using the `erb` method in the block that loads a page with an argument that represents a `.erb` file. This file should be placed in the `/views` directory of your Sinatra project. This `/views` directory should be at the same directory level as the `my_app.rb` file that runs to start your server.
```ruby
# loads the .erb file views/index.erb
get '/' do
  erb(:index)
end
```
Structuring your application in this way has the benefit of separating out concerns for routing your application and displaying page content as page content is simply kept as a dependency.

You can **submit `.erb` code directly to the Sinatra `erb` function** to be rendered.
```ruby
# render erb code defined by a variable
get '/' do
  code = '<%= [1, 2, 3].sample %>'
  erb(code)
end
```
Views **should be kept free of code concerns**. You should never do more than light `<% if %>` and `<% else %>` statements and light iterators like `<% each %>` in your embedded ruby code. Anything more complex should be extracted out to the main program and encapsulated in an instance variable. You can submit an instance variable by defining it inside the route and then referencing it as embedded ruby. The `my_app.rb` file might be:
```ruby
get '/' do
  # do something complex and programatic here and store it to a varaiable
  @my_variable = "Hello"
  erb(:index)
end
```
The corresponding `.erb` file:
```html
<!-- Render the variable from your routes file -->
<h1><%= @my_variable %></h1>
```
## Params
User queries or request bodies (from a `PUT` statement etc.) will appear inside your routes stored inside a hash called `params`. This `params` hash is typically filled by the HTTP request's body so its scope is localised to the page where the parameters are passed in. If you navigate from one page where you have some parameters loaded to another page without sending those parameters again then the `params` hash will be empty as you load the next page.

You can **access the value in your `params` hash** by using the key in the form of a symbol defined in your user arguments. The key is automatically converted to a symbol.
```ruby
post '/page-with-params' do
  @my_parameter = params[:name]
end
```
> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTgxNzc4MjUzNywtMTM0MTA3OTMwOCwxMT
k5OTI3NTMwLC0xOTgwODIyNDU0LC05OTI0NjA3MTcsNzcxNzIy
MTUxXX0=
-->