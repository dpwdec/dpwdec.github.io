---
title: Num
layout: page
exclude: true
---

You can **convert between differently generically defined types** using the `num-traits` crate's `ToPrimitive` and `NumCast` traits. This is only necessary if the generic types in this conversion differ, in the example below the generic `D` only has to be some form of primitive or something can be converted `ToPrimitive` and represented in that way. The type it is being turned into `T` must support the `NumCast` trait which enables casting `from` arbitrary values. This conversion will fail with a `None` if the conversion cannot take place.
```rust
use num_traits::cast::NumCast;  
use num_traits::ToPrimitive;  
  
fn cast<D: ToPrimitive, T: NumCast>(x: D) -> T {  
    T::from(x).unwrap()  
}
```

There are also a **range of predefined conversion methods** in the `Num` crate that allow you to convert between mismatched types to a specific type *in* a generic case such as `to_u32` or `to_i64`.
```rust
use num_traits::ToPrimitive; 

fn cast<T: ToPrimitive>(x: T) -> u32 {  
    x.to_u32().unwrap()  
}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIxNDMzMDA2OTMsLTEzMzQzOTU3NjgsMT
MzNjAwNjI4OV19
-->