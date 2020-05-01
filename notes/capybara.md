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

Capybara will raise a confusing `XPath` error that reads `unable to find xpath "/html"` if you try to test a page which is entirely empty. Be wary of this!

## Helpers
You can **define reusable pieces of code** for your Capybara tests to help keep your test code dry using **helper** methods. These are essentially methods defined in a separate file that can be called in your capybara tests to execu

## Commands

### Finders

`visit('/url-extension')` loads whatever page you want to test.

You can **find an object by its ID value** using the `find_by_id` method. This can then have other actions appended to it.
```ruby
find_by_id('my button').click
```
You can **find a specific option within an element** by using the `find` method combined with the `:xpath` option and an identifier. The query in the `find` should be submitted as an `xpath` identifier.
```ruby
# finds the second option in a drop down menu
find_by_id('my dropdown').find(:xpath, 'option[2]')
```
### Actions

To **click a button** use the `click_button` command. You can also use the `click` command appended to a query that `find`s an element in your HTML document.
```ruby
# clicks 'my button'
click_button('my button')
# find the 'my button' element and click it
find('my button').click
```

You can **fill in a form field** using the `fill_in` command, combined with the field `name`, `id` or `label` and the value to add.
```ruby
# fills in the name field of a form with "John"
fill_in('name', with: 'John')
```
To **select an option from a dropdown** use the `select_option` action. Un-intuitively you cannot use the `click` selector for selecting an option from a drop down.
```ruby
# finds the sencond option of the drop down menu and selects it
find_by_id('my dropdown').find(:xpath, 'option[2]').select_option
``` 
## Matchers
Most capybara matchers for testing page elements work by using the `name`, `id` or `type` values on an HTML element. You should **avoid using the CSS selectors** to test elements on the page.

You can t**est a page has a specific piece of text or content** by using the `have_content(content)` matcher which returns true if a page contains the content submitted in the argument.
```ruby
expect(page).to have_content('Hello world!')
```

You can **check for form content elements** using the `have_field` matcher. This checks based `id` component of the HTML `<form>` field object.
```ruby
expect(page).to have_field('name')
```
You can **test that a link or button goes to a the correct URL** by using the `have_current_path` matcher which test the current URL page extension. In the example below we test a button that takes us to the `/about` page.
```ruby
click_button('some link')
expect(page).to have_current_path('/about')
```
> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTExMTMzMjM1NzEsLTE1MzY4NDIxMDQsLT
Y1NTA3MDE0LDEzNzk5MzU3MDksLTE3ODUwNTM1ODcsMTAwMzE2
MTY5OSwtMTQ2MDE5MTE5MF19
-->