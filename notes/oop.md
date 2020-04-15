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
**SRP** means structuring our program so that each individual part of its functionality is encapsulated as a distinct entity (or class) capable of handling that responsibility without outside assistance. Each class should have one thing that is responsible for changing or editing.

### Cohesion


> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE1Njk0MjAxNzIsLTExODM4NDIxNzcsLT
cyNTQ1MDI3NywtMTkzMzg1MTE1OCwtMzcyMjE4MTM2XX0=
-->