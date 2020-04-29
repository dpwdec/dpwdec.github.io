---
title: Sinatra
layout: page
exclude: true
---
Capybara is a ruby framework for remotely controlling a browser by performing actions like visiting websites, clicking links and filling out forms procedurally. This framework can be leveraged in combination with [RSpec](https://dpwdec.github.io/notes/rspec.html) to create a way of testing that your webpages work correctly, for example, checking that links click through correctly and forms display as you intend.

## Start Up
Install the capybara base code by using `gem 'capybara'` inside your `Gemfile` with the `bundle` command. Next run an `rspec --init` command to initialise your `spec` directory and `spec_helper.rb` file. You then need to edit your `spec_helper` file to with some configuration settings to point it towards the correct class / file, as well as `require` the RSpec implementation of capybara.
```ruby
# add this to spec/spec_helper.rb

ENV['RACK_ENV'] = 'test'

# require our Sinatra app file
require File.join(File.dirname(__FILE__), '..', 'app.rb')

require 'capybara'
require 'capybara/rspec'
require 'rspec'

# tell Capybara about our app class
Capybara.app = Battle
```
Capybara feature tests should be placed in the 

> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbNjUzNjQyNzkzXX0=
-->