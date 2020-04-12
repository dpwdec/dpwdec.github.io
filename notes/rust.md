---
title: Rust
layout: page
exclude: true
---
## Variables and Types
Variables in Rust are **immutable** by default and cannot be changed after they are assigned. The Rust team argues that immutable variables are more in general more stable and easier to debug especially in the case of multiple sections of your code accessing of changing a single mutable variable.
```rust
let x = 4
// next line will cause an error
x = 5 // --> NOT VALID
```
You can define **mutable** variables by using the `mut` keyword before a variable is first assigned.
```rust
let mut x = 5
// now you change the variable
x = 6
```
You can **assign datatypes** using a `:` followed by the type attached to the end of a value:
```rust
let x: i32 = 10;
```
Large numbers can be assigned using `_` number syntax:
```rust
let number = 100_000; // one hundred thousand
```
You can **create a constant** with the `const` keyword. Constants are valid for the entire run time of the program. Constants are *always* immutable and cannot be used with the `mut` keyword. Constants **must be defined with a type indicator**, like `i32`. The rust naming convention for constants is to use all upper with `_` underscores.
```rust
const MY_CONSTANT: u32 = 100;
```
Rust constants can *never* be changed. They can also never be assigned using functions that require computation at run time, such as a function or if statement where there could be multiple possible outcomes for the constant, even when the function is entirely static.
```rust
const A_CONSTANT = 3 + 4; // Valid
const ANOTHER_CONSTANT = my_function(3); // Error
```


You can **convert a string into a number** by using Rust's string `parse` method. This takes a string input and converts it into a number. There are many types of numbers such as an unsigned or signed 64 bit integer or a signed 32 bit integer, this means you need to specify what type of number you want the parse method to output by adding a `:` and the number type, such as `u32` to the end of the variable name. The `trim` method works like Ruby's `chomp` method and removes any `\n` special characters from the string which would cause an error if you tried to parse them to a number.
```rust
let my_string = "48";
// parse string into a number
let my_number: u32 = my_string.trim().parse()
  .expect("Invalid number")
```
## Control Flow
## Pattern Matching
The `match` keyword can be used to match the output of a particular set of enums and execute code based on the result. In the example below `a_num` run a comparison method on `b_num` which returns an enum with three possible outputs - Less, Greater and Equal. The `match` block then executes code based on each possible return type from the enum.
```rust
use std::cmp::Ordering;
// initialize numbers
let a_num = 10;
let b_num = 15;
// check matches
match a_num.cmp(&b_num) {
  Ordering::Less => println!("Smaller")
  Ordering::Greater=> println!("Larger")
  Ordering::Equal => println!("Same")
}
```
In the example above, the `a_num.cmp` method takes a pointer to `b_num` as indicated by the `&` ampersand, and compares itself to that value.
## Cargo
You can **add a new code library** (also known as a "crate") to rust by adding to the `[dependencies]` section of the `cargo.toml` file. To add a new a crate simply input the crate's name and the version that you want to use. The actual installed version may differ from the version specified as this number only ensures that a version compatible with the specified version number will be installed.
```toml
[dependencies]
crate_name = "0.5.5"
```
Use `cargo build` to update and download any dependencies to your project. You can use `cargo update` to update your installed dependencies, this will also ignore your `cargo.lock` file.

## Rand
The `rand` crate allows you generate random numbers at run time for your program. The random number generator works by creating a `thread_rng` object that is localised to our execution thread and seeded by the operating system.
```rust
use rand::Rng;
// generate a new random number
let random_number = rand::thread_rng.gen_range(1, 101)
```
The `gen_range()` function is inclusive at its bottom end and exclusive at its top end. In the above example it will produce a number between 1 and 100.
> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE3ODA1MzgzNDcsLTE2MzgyMzI2NzcsMj
AzODg0NDg2OSw2MTcyMjAzNDcsLTg1ODA4ODI0MywtMTYwODgy
NTI2M119
-->