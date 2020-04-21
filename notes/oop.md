---
title: OOP
layout: page
exclude: true
---
polymorphism
inheritance

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

### Forwarding
**Forwarding** is the method of delegating a task to another class by calling a method on that class from another pi
 
> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTg4MjQ5MjA0OSwtNjI5MDM3Mzk0LDIyND
g0NTUwNywyMDg1Njk2Nzc3LC0xMzgzMjc1Mjk0LC0yMDk5ODE1
NzIxLC0xMjMyNjUyMTY1LC0zMjU4NDY4MzQsNDMxMzgzNzg2LD
E3NDc0NTM0MTAsNzk1NzAxNTk3LC0xNTY5NDIwMTcyLC0xMTgz
ODQyMTc3LC03MjU0NTAyNzcsLTE5MzM4NTExNTgsLTM3MjIxOD
EzNl19
-->