---
title: OOP
layout: page
exclude: true
---

### Data Abstraction
When creating a class to represent a real world object we can use **data abstraction** to the model that real object more effectively. This means creating classes so that their data is structured in such a way that it *matches* the real world object's structure. 

For example if we have a `Bird` object we can create a generalised blueprint that matches the structure of how information about a bird might be represented.
```ruby
class Bird
  GRAVITY = 9.8
  def initialize(wing_span, weight)
    @wing_span = wing_span
    @weight = weight
    @position = { x: 0, y: 0 }
  end
  
  public
  def fly
    # use flying speed to move the bird and make it fly
  end

  private
  def flying_speed
    # code using gravity, weight and wing span
  end
end
```
Here the `Bird` class represents a bird with a `position`, `wing_span` and `weight`, everything need to calculate the bird's `flying_speed`. We then include a `fly` to change the bird's position.

### Encapsulation
**Encapsulation** means structuring objects so that only the properties that are required to interact with the object are *exposed* to the rest of the program giving your code a standard interface with which to interact with a class. With encapsulation we hide all of the implementation details from the rest of code keeping it as a contained object.

In the above example `GRAVITY` is a constant that can be accessed for the `Bird` class using `Bird::GRAVITY` but not changed, this is useful if we were perhaps modelling an entire woodland and wanted to get a consistent gravity across the entire model.

The `@position`,`@wing_span` and `@weight` instance variables cannot be accessed from outside the `Bird` class because the rest of program does not need to change these directly. Furthermore the `flying_speed` method is kept private so that only a particular instance of the `Bird` class can calculate its flying speed because the rest of our code doesn't need to interact with this method.

The `fly` method however *is* exposed to the rest of our code so that we have an interface for interacting with our `Bird` instances to make them fly!

Because our code has clearly defined channels for interacting with our `Bird` class it means we can easily change the implementation of the class without effecting the rest of our code. For example if we wanted to completely rewrite the `fly` method to changed how we calculating flying we can do that without in any way changing how the rest of our code outside of the `Bird` class works.

### SRP (Single Responsibility Principle)
**SRP** means structuring our program so that each individual part of its functionality is encapsulated as a distinct entity (or class) capable of handling that responsibility without outside assistance. Each class should have one logical thing that is responsible for.

This also means that if changes are required to your code they should only effect *one* component class in your system. If you find that writing a change into your system is propagating out to multiple classes in then you have probably violated SRP.

The code below describes a class `Body` which has several different methods for things like thinking, moving and looking around. Currently the `Body` class violates SRP because it is responsible for multiple components and behaviours in our system. Furthermore, if we want to make a change to "thinking" or "moving" then both of those changes require use to change the body class, rather than a single component in our system further violating SRP.
```ruby
class Body
  def think
    # has thoughts
  end

  def move
    # moves around
  end

  def look
    # looks around
  end
end
```
Here is another version of the body's functionality refactored to adhere to SRP. In this version the body class has been changed to function simply as a container for the new classes which function as logical units to contain the functionality that was originally in the `Body` class. Now, if we need to make changes to "thinking", "moving" or "seeing" we only need to change one part of our code that is logical separated from the other elements of our program.
```ruby
class Body
   def initialize
     @muscles = Muscles.new
     @brain = Brain.new
     @eyes = Eyes.new
   end
end

class Muscles
  def move
    # move around
  end
end

class Brain
  def think
    # thinks thoughts
  end
end

class Eyes
  def look
    # looks around
  end
end
```
We could go further with this principle. For example, what if we want to distinguish between different parts of movement such as moving the legs to walk, or moving the arms to wave? We don't want to put the code for the walking and waving into the `Muscles` class directly because if we wanted to change our walking or waving code it would mean having more than one reason to change the `Muscles` class, thus violating SRP. Instead we should spin out this functionality into `Legs` and `Arms` classes that are simply managed by inherit from the `Muscles` class. That way if we need to change the way muscles work in general we can refactor the `Muscles` class - a single responsibility - but if we need to change the way our `Body` "walks" or "waves" we can change the `Legs` and `Arms` classes respsectively.
```ruby
class Body
   def initialize
     @muscles = Muscles.new
     @brain = Brain.new
     @eyes = Eyes.new
   end
end

class Muscles
end

class Legs < Muscles
  def walk
    # walks around
  end
end

class Arms < Muscles
  def wave
    # waves at friends
  end
end

class Brain
  def think
    # thinks thoughts
  end
end

class Eyes
  def look
    # looks around
  end
end
```
You can also conceptualise SRP further as being **method specific** if you have a method *within* a class that has more than one responsibility then this also violates SRP and should be refactored into multiple methods.

### Cohesion
**Cohesion** is similar to both encapsulation and SRP, it simply refers to grouping code in a way that is self contained and executes singular tasks well as opposed to spreading out the functionality of your code base.

### Forwarding and Delegation
**Forwarding** and **delegation** are very similar. They both involve passing messages that are passed to a class down to other objects and using the methods on those objects instead. The main difference is that when you **forward** the class receiving the message is has its own entirely separate context and interface from the class sending the method. Whereas when you **delegate** the receiving class is *wrapped* inside the class calling it, so that the context of code remains consistent with the calling object.

One analogy used is that of receiving an email asking you to donate to a charity. If you **forward** the email you might send it to a friend who would be able to donate that amount. It's not a personally responsibility. However, if you **delegate** the task of donating to your accountant then its still ultimately your responsibility to pay the money to the charity.

But, **what does this actually look like?**

The essential difference is how classes interact. The example below shows how **delegation** works. In this example the `Phone` class delegates the act of displaying things on the screen to the `Screen` class by storing an instance of it in the `@screen` instance variable. It has an essentially private relationship with the screen which it **delegates** responsibilities to. This is delegation because it is never exposed the context of `@screen` is never exposed publicly, it is all mediated through the `display` method in the phone object.
```ruby
class Phone
  def initialize
    @screen = Screen.new
  end

  def display
    @screen.display
  end
end

class Screen
  def display
    # display stuff
  end
end
```
On the other hand **forwarding** is when the interface and context of the object that is handling things is exposed.
```ruby
class Client
  def initialize(server)
    @server = server
  end
end

class Server
  def data
    # return server data
  end
end
```
In the code above the `Client` class takes in a `Server` object when created. This means that `Server` object exists in its own right even before the `Client` is first initialized. Then if our `Client` wants to get `data` it will **forward** that request to the server object. An example in the `irb` might be:
```
server = Server.new
client = Client.new(server)
client.server.data
```
Here we are calling the namespace of the `server` object directly and **forwarding** the request for data onto that object. It's this distinction that is the primary difference between these two methods of object communication. In essence however they are both about extracting functionality and organising code.

### Polymorphism
**Polymorphism** is the method of presenting the same interface on different objects, so that, even though the objects have different functionality the way code interacts with them is kept consistent meaning that we can use only a few lines of code to produce wildly different results simply by calling on different objects with the same interface.
```ruby
class Taster
  def taste(food)
    puts food.flavor
  end
end

class Cabbage
  def flavor
    "Tastes like old socks"
  end
end

class Rice
  def flavor
    "Has the flavor of cardboard"
  end
end

class Almond
  def flavor
    "Like a nut party in my mouth"
  end
end

taster = Taster.new
taster.taste(Cabbage.new) # => "Tastes like old socks"
taster.taste(Rice.new) # => "Has the flavor of cardboard"
taster.taste(Almond.new) # => "Like a nut party in my mouth"
```
In the above example we can see the `Taster` class calls the the functionality on the different types of food in exactly the same way with the line `food.flavor` to produce wildly different outputs. This is because each of the food classes have a **polymorphic** relationship in which they all implement the same method `flavor` but with different outputs. Thus we only need one line of code in the `Taster` class to interact with all of these classes.

### Inheritance
**Inheritance** is the method of defining multiple objects based on common sets of functionality that would be implemented on those objects. In the last example we created a set of polymorphic classes however its clear that there is a category relationship between all of these objects. They are all food. Which means they can *inherit* from a `Food` class.

```ruby
class Food
  def initialize(type, color)
    @type = type
    @color = color
    @edible = true
  end
  
  def flavor
    "It tastes like something"
  end
end

class Cabbage < Food
  def flavor
    "Tastes like old socks"
  end
end

class Rice < Food
  def flavor
    "Has the flavor of cardboard"
  end
end

class Almond < Food
  def flavor
    "Like a nut party in my mouth"
  end

  def crunch
    puts "Crunchy nuts"
  end
end
```
 We have now created a shared `initialize` method for each of foods that records their type and color as well as a boolean that describes them as edible. Furthermore each food sub class (`Cabbage`, `Rice`, `Almond`) overloads the `flavor` method defined in the `Food` class. This allows us to organise our code and centralise changes to the parent class of these items. For example, if we wanted to change how the `initialize` method on each of these classes *without* them inheriting from `Food` we would need to change three different constructors - not very dry or efficient. By letting our classes inherit the constructor we only have to change one piece of code to update all the subclasses.

### Composition over Inheritance
**Composition** is process of **designing the different parts of your code based on what they do or what they have** *rather than* by what they are. In a traditional inheritance in object oriented programming, we manage classes based on classifying them as objects that *are* something.

| Inheritance | Composition |
| --- | ---
| What something is - a computer is a type of machine | What something does - A computer displays stuff
| | What it has - a computer has a screen component that displasys stuff

Considering the  inheritance and class chart below, imagine that we were asked to make a "robot muder dog" that can `drive`, `murder` and `bark` but not `poop` because it is a robot. We would be in a very bad situation because there is no way we can redefine this inheritance structure to include this functionality without bundling a lot of functionality that we don't want - by creating a common inheritor for everything -  or confusing our types. This is sometimes called the **gorilla and banana problem** because when ask for a banana - i.e. a small piece of added functionality - we instead get a gorilla holding a banana - i.e. implementing that small piece of functionality means we need to include a lot of unnecessary functionality in that class.
```ruby
Animal
| .poop()
|
| Dog
| | .bark()
|
| Cat
| | .meow()

Robot
| .drive()
|
| Cleaner
| | .clean()
|
| Murderer
| | .murder()
```
We can solve the above problem using **composition** by extracting the different pieces of functionality into their own classes. Essentially separating these pieces of functionality in an almost modular fashion.
```ruby
class Drive
  def drive
    "drives recklessly"
  end
end

class Clean
  def clean
    "cleans carefully"
  end
end

class Murder
  def kill
    "kills indiscriminately"
  end
end

class Poop
  def poop
    "poops violently"
  end
end

class Bark
  def bark
    "barks loudly"
  end
end

class Meow
  def meow
    "meows gently"
  end
end
```
Now our original classes and desired features can be created by simply slotting together the different pieces of functionality we have created in a "has a" relationship where the larger class structures contain these smaller functional classes and then use them to do things.
```ruby
class Cat
  def initialize
    @
  end
```
> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE0NjY4MjQ0OTEsMTQ1ODAyNTk2OSwyNT
kwMzY1OTIsMzEyMDMyNzQxLC0xMzc0NjkzOTI2LDQxNDEyNjU2
OSwyMDA3NDU2MTAwLDE5MTMxODQ2NzIsLTIxNzQzMDA1MSwtMT
IwOTU3NjQzNywxMDI3OTAyNDk3LDE0NTgzODg1ODQsLTYyOTAz
NzM5NCwyMjQ4NDU1MDcsMjA4NTY5Njc3NywtMTM4MzI3NTI5NC
wtMjA5OTgxNTcyMSwtMTIzMjY1MjE2NSwtMzI1ODQ2ODM0LDQz
MTM4Mzc4Nl19
-->