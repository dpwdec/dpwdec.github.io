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

### Redirect
You can **redirect to a different route** using the `redirect` method within a controller block.
```ruby
# visiting this page
get '/redirect' do
  redirect('/different')
end
# will redirect to this page
get '/different' do
  'Redirected here'
end
```
### Sessions

You can **save information between different pages** so that it is available to all your different controllers by using the `sessions` object. To start using sessions you need to add `enable :sessions` to top of your file or class. Then you can use the `sessions` object just like the `params` hash however it starts off empty and its value will persist in different controllers.
```ruby
class MyApp < Sinatra::Base
  enable :sessions

  get '/' do
    sessions[:my_var] = 'Hello'
  end

  get '/print' do
    # prints 'Hello'
    sessions[:my_var]
  end
end
```

## Modular Style

Sinatra's **modular style** allows you to create classes that inherit from `Sinatra::Base` class and contain the code for your application. You can define multiple different app classes in your root file each one representing a self contained web application, you can switch between these seamlessly within a single ruby process running the server.

To **set up a new modular style app** create a new `Sinatra::Base` class that contains the routes for your app.
```ruby
# app.rb
class MyApp < Sinatra::Base
  # app routes here

  # start the server if ruby file executed directly
  run! if app_file == $0
end
```
You then need to create a `config.ru` file in the root directory of your project which `require`s the file in which your app classes are stored and uses the `run` command to specify a class (which is child of `Sinatra::Base`) to start the application.
```ruby
# config.ru
require './app'
run MyApp
```
The app is then run *from* the `config.ru` file using a command like `rackup` or `shotgun`. These commands will automatically find the `config.ru` file and execute it running the correct class and file.
```
# start with rackup from command line on port 4567
rackup -p 4567
# start with shotgun from command line on port 4567
shotgun -p 4567
```
If you are using `shotgun`, when you change the class specified in `config.ru` the server will dynamically change to run the code from that other class which could be an entirely separate web application.

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
The `params` hash only has elements pushed through from the `name` value of an html element. For example if I have a form field with an `id="my_param"` this will NOT appear in the `params` hash when submitted. The form field MUST have a value `name="my_param"` for that element to appear in the `params` hash.
```html
<form action="/greet" method="post">
  <label for="name">This text won't be submitted</label><br>
  <!-- params[:no_submit] will be empty -->
  <input type="text" id="no_submit"><br>
  <!-- params[:submit] will have the value of this input field -->
  <input type="text" name="submit"><br>
  <input type="submit" value="Submit">
</form>
```
## Rack
You can **specify the port on which you want a server to run with `rack`** by using the `-p` argument followed by the port number.
```
rackup -p 4567
```

## Shotgun
Shotgun is an application gem for running your server and dynamically restarting the server when you make changes to your web code. You can **install Shotgun** by adding `gem 'shotgun'` in your `Gemfile` and running the `bundle` command. Shotgun has the **same port specification as `rackup`** and also uses your `config.ru` file to start the server when using Sinatra's modular style

```
shotgun -p 4567
```

By default **shotgun does not remember `session` hash data** because it restarts the server every time you load a new page thus erasing the data. To **save session data in shotgun** use the `configure` method on Sinatra's `:development` mode and set the `:session_secret` to be something. This will make the `session` hash persistent across automatic server restarts of Ra
> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE0MTI1MzA5MTIsMTE3NjUxNTg4NCwtMT
U3MzkyMjI4LC0xODUyMTMwNTAwLC01MDA0NjMwMjMsLTEzNDEw
NzkzMDgsMTE5OTkyNzUzMCwtMTk4MDgyMjQ1NCwtOTkyNDYwNz
E3LDc3MTcyMjE1MV19
-->