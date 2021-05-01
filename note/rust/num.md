---
title: Num
layout: page
exclude: true
---

You can **convert between differently generically defined types** using the `num-traits` crate's `ToPrimitive` and `NumCast` traits. This is only necessary if the generic types in this conversion differ, in the example below the generic `D` only has to be some fo
```rust
use num_traits::cast::NumCast;  
use num_traits::ToPrimitive;  
  
fn cast<D: ToPrimitive, T: NumCast>(x: D) -> T {  
    T::from(x).unwrap()  
}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzNDg4ODM1MjJdfQ==
-->