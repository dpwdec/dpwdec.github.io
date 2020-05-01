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
### Storing Data

For more functional data that needs to be stored between page reloads you can **use class variables as a way to persist data** across reloading. For example, if we have a `@game` instance object that we need to persist on many different views we can save this instance to a class variable of the `Game` class and then access it anywhere.
```ruby
class Game
  def self.new_game
    @game = Game.new
  end

  def self.current_game
    @game
  end
end
```
Then in our Sinatra routes this can be accessed directly from the `Game` class or by assigning from the game class to a route specific instance variable.
```ruby
class MyApp < Sinatra::Base
  get '/' do
    Game.new_game
  end
  
  get '/play' do
    @game = Game.current_game
  end
end
```

### Filters
Filters allow you to extract code that is repeated in your controllers into blocks that run before or after each controller. 

To **define a before filter** use the `before` keyword with a block, this block runs before each route is loaded. Variables defined in a before block **are available in the routes before which they run**.
```ruby
class MyApp < Sinatra::Base
  before do
    @my_var = 'Hello'
  end

  get '/' do
    @my_var # => 'Hello'
  end
end
```
To **define an after filter** use the `after` keyword. This code runs after each controller has finished processing. Variables defined in the `before` filter are **available in the after filter**.
```ruby
class MyApp < Sinatra::Base
  before do
    @my_var = 'Hello'
  end

  get '/' do
    @my_var # => 'Hello'
  end

  after do
    puts "Page loaded sucessfully #{@my_var}"
  end
end
```
You can **specify a route that a filter should run on** by submitting that route's URL extension as a `String`. This works for both `before` and `after` filters.

```ruby
# this before method only runs on /page
before '/page' do
  # before code
end
```
You can **also submit `RegEx`** to this argument to text for specific pages. You **must escape the `/` in your route names with `\`** so each regex for a specific route will begin with `\/` inside the double forward slash `RegEx` indicators `/../` to initiate the fact that you are searching for a route.
```ruby
before /\/D\w+/ do
  # matches any pages starting with D that are one word long
end
```
If you want to **set up a filter for multiple we**

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
## Partials
Web partials are a way of DRYing up web interface code by extracting repeated interface elements into a single display file that is invoked on pages. An example of this would be something like a nav bar. Our website might have 100 pages all with the same navbar, so to avoid duplication we have one *partial* file containing the navbar code which we render on each page. Partials are also a great way to insert dependency code like CSS.

To **[render a partial][part] in Sinatra** use the `erb` method with `:layout` set to false. Place your partial file in the Sinatra `views` directory. I also like to name by partial files beginning with an `_` underscore to indicate they are partial views.
```ruby
<!-- renders the _style.erb file in index.erb -->
<%= erb(:_style, :layout => false) %>
```

[part]: https://steve.dynedge.co.uk/2010/04/14/render-rails-style-partials-in-sinatra/

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
[Shotgun](https://github.com/rtomayko/shotgun) is another ruby gem that can be used to **automatically restart your Sinatra server** after changes are made. To install simply add the `gem Shotgun` line to your `Gemfile`. You can then run the server using the `shotgun` command instead of the `ruby` command so that it is automatically restarted when changes to the code are made.
```
shotgun my_app.rb
```
Shotgun has the **same port specification as `rackup`** and also uses your `config.ru` file to start the server when using Sinatra's modular style

```
shotgun -p 4567
```

By default **shotgun does not remember `session` hash data** because it restarts the server every time you load a new page thus erasing the data. To **save session data in shotgun** use the `configure` method on Sinatra's `:development` mode and set the `:session_secret` to be something. This will make the `session` hash persistent across automatic server restarts using Shotgun. It's worth noting the string passed into `:secret_session` can be basically anything, the important thing is that it has an identifier that can be used for session persistence.
```ruby
# Shotgun secret_sessions setting
class MyApp < Sinatra::Base
  configure(:development) { set :session_secret, 'set' }
  enable :sessions

  # ...sinatra web code using sessions here...
end
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTcyNjk5MTIyMCwtMTc0OTU2MDgsLTQ5MT
AzODkyMiwxNDg4NDI5NTIyLDE5MTk0MDEzNTEsLTIzOTI3Mjcw
MSwxMjY4Mzk0MDcyLC0xOTc0ODI4MjcyLDExNzY1MTU4ODQsLT
E1NzM5MjIyOCwtMTg1MjEzMDUwMCwtNTAwNDYzMDIzLC0xMzQx
MDc5MzA4LDExOTk5Mjc1MzAsLTE5ODA4MjI0NTQsLTk5MjQ2MD
cxNyw3NzE3MjIxNTFdfQ==
-->