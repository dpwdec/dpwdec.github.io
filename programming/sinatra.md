---
title: Sinatra
layout: page
exclude: true
---
Sinatra is a lightweight web framework for building small web applications in ruby.

## Setup
You can **install Sinatra** by simply including the `gem Sinatra` in your `Gemfile` and running the `bundle` command.

You can **start a Sinatra app running** i.e. listening and functioning as a server by using the `ruby` command in the terminal to run whichever is the main file in your Sinatra project.
```
ruby my_app.rb
```
This should be the file in which your different web page routes and defined.

To **stop a Sinatra server** use `CTRL + C` in the command line window where the server is running.

When changing files in your Sinatra project you will need to start and restart the server to see those changes propagated to the web pages displayed online.

Scripts (i.e. ruby files that contain code directly without methods or classes) that are `require`d inside `app.rb` will be run when your sinatra application start up. Use this functionality to **execute set up code** for your sinatra application.

### Configuration

Sinatra `configuration` blocks run on files `require`d in your main Sinatra file. Usually `app.rb`.  You can submit arguments to these `configuration` blocks in the form of symbols which represent the different environment you are in when running the code. This environment is actually recorded as a symbol of the same name: `:envrionment`.

For example, the `:test` symbol is used for running test code. Which environment you are in depends on the `ENV['RACK_ENV']`. The environment defaults to `:development` if not environment is set.
```ruby
configuration :development do
  # do some development set up
end

configuration :test do
  # do some test set up
end
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

You can **write route titles as `RegEx` expressions** if you want to match a route to a particular class of URL extension in your application by containing the route name inside `/.../` slashes. You also **must escape the opening `/`** with a `\`.
```ruby
# route for webpages that begin with an 'h' followed by some letters
get /\/h\w+/ do
  'This is an H page.'
end
```
You can **return the current page URL extensions** using the `request.path` object, this can be used inside routes *or* filters.
```ruby
get '/mypath' do
  request.path # => '/mypath'
end
```

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
If you want to **set up a filter for [multiple][stackm] web pages** you can use an `if` statement in conjunction with the `request.path` object.
```ruby
# runs before code only on 'mypage' and 'about' page
before do
  if request.path == '/mypage' || request.path == '/about'
    @my_var = 'hello'
  end
end
```
[stackm]: https://stackoverflow.com/questions/7703962/in-sinatra-how-do-you-make-a-before-filter-that-matches-all-routes-except-some

You can also **filter pages negatively** using the `pass` keyword which will essentially break out of the filter if the `request.path` name matches your condition.
```ruby
# runs before code on every page except for '/nobefore'
before do
  pass if request.path == '/nobefore'
  @my_var = 'hello'
end
```

## Restful Routing

### Other HTTP methods

Sinatra and HTML don't directly support HTTP methods apart from `GET` and `POST`. However, Sinatra *does have* route code for managing these routes in `app.rb`, there's just no built in way to direct HTTP requests from pages to these routes. These is a work around using a class called `Rack::MethodOverride` which allows you to submit other HTTP request methods as a hidden `param` from within a submission form using the `_method` key. When your Sinatra application receives this data it will redirect automatically to the appropriate HTTP method route. To use this functionality `use` the `MethodOverride` class inside `app.rb` and edit your HTML forms to include the hidden `_method` field.
```ruby
class MyApp < Sinatra::Base
  use Rack::Override

  get '/user' do
    # show user page
  end

  post '/user' do
    # create user data
  end

  delete '/user' do
    # delete user data
  end
end
```
With the `app.rb` file set up with the appropriate routes. We can now edit our HTML forms to contain the appropriate data fields. Even though official method of this form is still `POST` when your web application receives that request with a `params` key called `_method` the rack part of our Sinatra application will process it as a `DELETE` request and reroute it to the `delete` block.

```html
<form class="" action="/bookmarks" method="post">
  <!-- Line directly below this changes the form functionality -->
  <input type="hidden" name="_method" value="delete">
  <input type="submit" name="delete_button" value="Delete">
</form>
```

This same work around can be used for other HTTP methods like `PUT`, `PATH` etc.

### ID specific pages

You may often be dealing with URLs that are related to a large number of similarly formatted but different resources. For example, posts on a website. A user may make a huge number of posts each with a unique ID and ideally we will have a unique URL for each post that can be viewed. We can **generatively add dynamic routes for different resources** by appending a symbol to your Sinatra route, such as `:id` which is usually used for routing to resource specific pages. For example we might have the url extension `/post/:id` which would display the post with whatever id replaced the `:id` part of the route string. This `:id` replacement **also appears in the `params` hash** so it can accessed and used to get data from a database.

If our user visited `post/263` then our corresponding Sinatra route with the `:id` route would have access to a `params` entry for `:id` that corresponds to `263`. The html for this would be dynamically plug in the corresponding id from a `GET` request to load general data.
```html
<a href="/post/<%= post.id %>"> <%= post.title %> </a>
```

The corresponding Sinatra route would match with this url extension and then load the post from the database before displaying it.

```ruby
class MyApp < Sinatra::Base
  get '/' do
    # route that shows posts and links to posts
  end

  get '/post/:id' do
    @post = load_post_from_database(params[:id])
    # some code for rendering a view that uses the data in @post
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
## Partials

Web partials are a way of DRYing up web interface code by extracting repeated interface elements into a single display file that is invoked on pages. An example of this would be something like a nav bar. Our website might have 100 pages all with the same navbar, so to avoid duplication we have one *partial* file containing the navbar code which we render on each page. Partials are also a great way to insert dependency code like CSS.

The primary way to do this in Sinatra is **using the `layout.erb`** file. This is a file is placed in the `views` folder and contains the `<%= yield %>` tags to render page specific content. It is run on every single page in your application and whatever the content is for that page will be inserted where the `yield` is called.
```html
<!doctype html>
<html>
  <%= yield %>
</html>
```

You can also render page specific partials by calling them with the**[render a partial][part] functionality in Sinatra** which use the `erb` method with `:layout` set to false. Place your partial file in the Sinatra `views` directory. I also like to name by partial files beginning with an `_` underscore to indicate they are partial views.
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
## CSS
To **link to CSS stylesheets** within your Sinatra project you should place stylesheets in the `public` directory and then ideally in a `stylesheets` sub-directory. The ultimate path to your stylesheet will then be `public/stylesheets/my_style.css`. To access these sheets simply link to them inside a `link` element placed in the `head` of document.
```html
<head>
  <link rel="stylesheet" type="text/css" href="/stylesheets/my_style.css">
</head>
```

## Serving Ajax Requests with JSON

When you want to return a response as `JSON` that you know will be used by Javascript in an Ajax cycle using ruby's built in `to_json` in isolation is not enough. This is because the `response` object that the Ajax request receives will actually be a string representing the object so the client side Javascript will need to call `JSON.parse` on the data returned from Sinatra route before being able to use the data like an object.
```ruby
# app.rb
require 'json'

get '/' do
  x = 5;
  { x: x }.to_json
end
```
The server side Javascript might make the request as follows. The `get` callback will need to use the `JSON.parse` function to coerce the `data` from the server into a usable object.
```js
$.get('/', function(data, status) {
  console.log(data) // => { "x":"5" }
  console.log(data.x) // => undefined
  data = JSON.parse(data);
  console.log(data) // => { x: 5 }
  console.log(data.x) // => 5
}
```
However, by using the `content_type` tag in ruby you can directly pass a `JSON` object out to Javascript requests.
```ruby
# app.rb
require 'json'

get '/' do
  x = 5;
  content_type :json
  { x: x }.to_json
end
```
Then the corresponding Javascript can simply load the `data` object from its callback function and access it directly.
```js
$.get('/', function(data, status) {
  console.log(data) // => { x: 5 }
  console.log(data.x) // => 5
}
```
## Rack
Rack is a minimal interface that facilitates the communication of web servers and ruby applications. When a request is sent to a web application it first goes to a server where the application is running, which has its own framework and conventions. This request is then passed to the application and then returned as a response which goes through the same process in reverse. 
![enter image description here](https://miro.medium.com/max/1134/0*GN3ldsyRjwXwqdHO.png)
The problem with this, is that if we want to change the server architecture *or* the type of app that is running the entire basis of our code would have be altered causing a lot of problems. 

`Rack` acts as a layer between the server and the application that they both agree to communicate with. Then, if the server needs to change or a different framework needs to be used for the web application, as long as they both speak rack there don't need to be any big changes to how the application works for these improvements and changes to be carried out.
![enter image description here](https://miro.medium.com/max/1400/0*d-jA4FIoJ9cuZA9p.png)
You can **specify the port on which you want a server to run with `rack`** by using the `-p` argument followed by the port number.
```
rackup -p 4567
```
You can create your own `rack` compliant classes by given them a `call` method that returns an array containing three elements:

- a status code
- a hash containing header information
- a body (inside an array)

And takes in an `env` variable as an argument.
```ruby
class MyClass
  def call(env)
    [200, {'content-type' => 'text/plain'}. ['This is my class.']]
  end
end
```
This class will now work effectively with `rack` and can interface with any web server that also runs rack to output `'This is my class'` text to a web page or server request.

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

## Sinatra-Flash

[Sinatra-Flash](https://github.com/SFEley/sinatra-flash) is a library that **allows you to use flash messages inside your sinatra** application. These messages appear once and when the page is refreshed disappear. This useful for displaying information that doesn't need to be persistently dispalyed, things like error messages and log in confirmation.

To setup `sinatra-flash` add it as a gem to your gemfile. Then `require 'sinatra/flash'` in your main Sinatra, `enable :sessions` and `register` the `Sinatra::Flash` namespace.

This allows you to use the `flash` which you can fill with values of your choosing and then display in your applications `.erb` files. These **flash messages persist through `redirect`s**. So, if you assign a flash messages value inside a `post` route for example, and then `redirect` to a `GET` page the value of the `flash` has will still be available for viewing.

Here is the `app.rb` for a flash implementation:
```ruby
# app.rb
require 'sinatra'
require 'sinatra/flash'

class MyApp < Sinatra::Base
  enable :sessions
  register Sinatra::Flash

  get '/notice' do
	# print the flash notice
    erb(:notice)
  end

  post '/notice' do
    # set flash notice and redirect
    flash[:notice] = 'This is a notice.'
    redirect('/notice')
  end
end
```
And the corresponding `.erb` file:
```html
<!-- notice.erb -->
<h1> <%= flash[:notice] %> </h1>
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTQ1ODU1ODUxOCwxODYzMzcwOTgxLDIxND
A1NzM0ODAsLTE0NDEwNzM1OTMsLTgyMTgwMTg1NCwtMjA5OTM2
NCw4MDQzMzI5OTQsNTI1MjAzOTU3LDM5ODQ1ODkxNSwtMTgyMj
I5NDY3MCwtMTg4MzkxMjU5MSw4NzkzMDU1MTcsLTExNDg5NTIy
NDksLTE4MTc0MTEzNTEsLTE3NzczMjY1ODIsLTE3NDk1NjA4LC
00OTEwMzg5MjIsMTQ4ODQyOTUyMiwxOTE5NDAxMzUxLC0yMzky
NzI3MDFdfQ==
-->