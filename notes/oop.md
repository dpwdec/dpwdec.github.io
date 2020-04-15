---
title: OOP
layout: page
exclude: true
---
## Data Abstraction
When creating a class to represent a real world object we can use "data abstraction" to the model that real object more effectively. This means creating classes so that their data is structured in such a way that it *matches* the real world object's structure. 

For example if we have a `Bird` object we can create a generalised blueprint that matches the structure of how information about a bird might be represented.
```ruby
class Bird
  GRAVITY = 9.8
  def initialize(wing_span, weight)
    @wing_span = wing_span
    @weight = weight
    @position = { x: 0, y: 0 }
  end
  
  private
  def fly
    # use flying speed to move the bird and make it fly
  end

  public
  def flying_speed
    # code using gravity, weight and wing span
  end
end
```
Here the `Bird` class represents a bird with a `position`, `wing_span` and `weight`, everything need to calculate the bird's flying speed.
> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE1MTI2OTQ2XX0=
-->