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
Tests that use capybara should be placed in the `spec/features` directory. These tests are then run automatically when you use the `rspec` command to trigger all your tests.

## Structure
The basic structure of capybara tests is similar to RSpec core with slightly different adjectives. In Capybara we run a `feature` block instead of a `describe` block to indicate which broad feature we are testing and we run a `scenario` block instead of an `it` block. You can then do set up using basic capybara and the vanilla RSpec `expect` adjective with capybara commands.
```ruby
feature 'Tests web page content' do
  scenario 'It has correct text' do
    visit('/')
    expect(page).to have_content 'Hello world!'
  end
end
```
The `page` variable is the equivalent of `subject` in capybara and points to the content on whatever page the test is currently running.
## Commands
- `visit('/url-extension')` loads whatever page you want to test.

## Matchers
Most capybara matchers for testing page elements work by using the `name`, `id` or `type` values on an HTML element. You should **avoid using the CSS selectors** to test elements on the page.

You can test a page has a specific piece of text or content by using the `have_content(content)` matcher which returns true if a page contains the content submitted in the argument.
```ruby
expect(page).to have_content('Hello world!')
```

You can **check for form content elements** using the `have_field` matcher. This checks based `id` component of the HTML `<form>` field object.
```ruby
expect(page).to have_field('name')
```
> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbNjQwODE4MDA2LDEzNzk5MzU3MDksLTE3OD
UwNTM1ODcsMTAwMzE2MTY5OSwtMTQ2MDE5MTE5MF19
-->