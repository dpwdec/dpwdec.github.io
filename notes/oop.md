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
  end

  def flying_speed
    # code using gravity, weight and wing span
  end

  def fly
    # use flying speed to move the bird and make it fly
  end
end
```

> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTQ2OTcyNTYxOV19
-->