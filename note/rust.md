---
title: Rust
layout: page
exclude: true
---

## Variables and Types

### Aliasing
You can **alias a type** or create new types using the `type` keyword. In the example below the `i32` type is aliased under `MyIntType` so that it can be used *as if* referencing that type while adding semantic value.
```rust
type MyIntType = i32;

let x: MyIntType = 10;
```

### Variables
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
`mut` variables can change value but **cannot change type**.
```rust
let mut x = 5;
x = "6" //Error
```
You can **redefine a variable and its type** using the `let` keyword.
```rust
let x = 5;
let x = "6"; // Valid
```
You can **assign datatypes** using a `:` followed by the type attached to the end of a value:
```rust
let x: i32 = 10;
```
Rust also has an integer type called `arch` indicated by the `isize` for signed and `usize` for unsigned. This size is based on the *architecture* of the system you are using. So for a 32 bit system it will be a `i32`.
```rust
// on 64-bit architecture
let x: isize = 97520; // 97520 64-bit integer
```
Floats can be assigned in rust using the `f32` and `f64` types.
```rust
let x: f32 = 5.0;
```
**Integer Overflow** happens when you input a value into an data type that is larger than that data type is meant to hold. For example a `u8` is can hold a maximum value of 255. If you input a value of 256+ you will get an integer overflow error. In Rust if you compile in `debug` mode your program will crash when it encounters a integer overflow error. However if you compile in `release` mode, when your program reaches an integer overflow error it will "wrap" the value. So a value of 256 input into a `u8` will wrap around to be equal to `0`.

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
You can use **shadowing** to assign a variable to using a variable of the same name in some function or computation combined with the `let` keyword.
```rust
let x = 10;
let x = x * 2; // x = 20
```
Shadowed variables can also be assigned from functions.
```rust
let fruit = "pineapple";
let fruit = fruit.chars().count(); // fruit = 9
```
#### Tuples


### Strings
You can return the number of characters in a string using the `.chars().count()` function:
```rust
let my_string = "Akimbo";
let my_string_length = my_string.chars().count();
```

You can **convert a string into a number** by using Rust's string `parse` method. This takes a string input and converts it into a number. There are many types of numbers such as an unsigned or signed 64 bit integer or a signed 32 bit integer, this means you need to specify what type of number you want the parse method to output by adding a `:` and the number type, such as `u32` to the end of the variable name. The `trim` method works like Ruby's `chomp` method and removes any `\n` special characters from the string which would cause an error if you tried to parse them to a number.
```rust
let my_string = "48";
// parse string into a number
let my_number: u32 = my_string.trim().parse()
  .expect("Invalid number")
```
### Format

The `format!` macro works like the `println!` macro but instead of displaying the output to the `stdout` it returns a `String`.
```rust
let world = "world";
format!("Hello {}!", world) // => Hello world!
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

## Structure
Rust projects are made of packages, creates and modules.

- A crate is a binary or library that can be compiled to do something.
- A package is a set of binaries and 1 or 0 libraries.
- A module is an internal code structure for grouping pieces of functionality

### Modules
You can **define a module** by using the `mod` keyword and the name of the module. The code below defines a `struct` called `some_struct` inside a module called `some_module`.
```rust
mod some_module {
  struct some_struct {
    // struct code
  }
}
```

You can **nest modules inside one another** as a way to organise your code.
```rust
mod some_module {
  mod another_module {
    struct some_struct {
      // struct code
    }
  }

  mod third_module {
    // some other code here
  }
}
```

You can **reference the code inside a module** using `relative` or `absolute` paths. The pattern for these references is indicate the module and object names you want to reference separated by `::` double colons.

You can **use absolute module references** by using the `crate` keyword at the beginning of the reference path. In the example below an absolute path is used to reference `some_struct`, this doesn't seem very useful right now because we are referencing this at the top level of our code, *however* if we were several levels deep in another module tree where we wanted to reference `some_struct` this might be very useful.
```rust
mod some_module {
  // ---snip---
}

let instance_of_some_struct = crate::some_module::another_module::some_struct {
  // make a new struct here
}
```

You can **use relative module references** by using the `self` and `super` keywords to referencing module paths for the place in the code where you are currently. In the example below because `some_module` is on the same level as the place where we want to use the code we can just referencing it directly.
```rust
mod some_module {
  // ---snip---
}

let instance_of_some_struct = some_module::another_module::some_struct {
  // make a new struct here
}
```

However, in this example using a relative path we need to make use of the `super` keyword to back out of the `instance_module` to go up a level into the route of the crate and then referencing `some_module` to get the code inside.
```rust
mod some_module {
  // ---snip---
}

mod instance_module {
  let instance_of_some_struct = super::some_module::another_module::some_struct {
  // make a new struct here
  }
}
```

### Use
The `use` keyword can be used to **import entire module name spaces**. The examples above with explicit module referencing are very long and if you need to use the thing you are referencing more than once it becomes laborious to type out the entire path reference every time. The `use` keyword adds the module code name-spaced under its lowest level specifier at the scope where it is used. In the example below `use` is used inside `third_module` to bring `another_module` into its name-space so it can re-used again and again without referencing the entire path to the module again.
```rust
mod some_module {
  mod another_module {
    struct some_struct {
      // struct code
    }
  }

  mod third_module {
    use super::some_module::another_module;
    let struct_instance = another_module::some_struct {
      // struct code here
    }
  }
}
```

The `use` keyword **only refers to the module scope in which it is defined**, it **does not extend to inner scopes**. The example below **does not work**, even though the code defines a `use` of `some_struct` at the top level that contains `another_module` the `use` does not extend inside the module and needs to be defined as a name-space *within* that specific module where it is used.
<pre class="error">
  mod some_module {
    struct some_struct {
      // struct code
    }
  }

  use self::some_module::some_struct;

  mod another_module {
    fn use_some_struct() -> some_struct { // -> some_struct will be undefined
      return some_struct {
        // struct code
      }
    }
  }
</pre>

This would be the correct structure to use `some_struct` inside `another_module` in which we have moved the `use` *inside* `another_module`.
```rust
mod some_module {
  struct some_struct {
    // struct code
  }

  fn some_function() -> i32 {
    // function code
  }
}

mod another_module {
  use super::some_module;
  fn use_some_struct() -> some_module::some_struct { 
    return some_module::some_struct {
      // struct code
    }
  }
}
```

It is **idiomatic in rust when importing functions to keep name-spaces at the parent level of the module you want to use**.  For example, if we wanted to use `some_function` in the code above we would import it name-spaced to its parent module `some_module`.
```rust
use some_module;

let x = some_module::some_function();
```


On the other hand **when importing structs, enums and other objects it's idiomatic to use the full path and directly reference what you want to `use`**. This holds true **unless the name of two things in scope would clash**. For example if we wanted to use `some_struct` from the example above the way it has been imported in `another_module` would *NOT* be idiomatic. Instead it would be better to simply `use` the `some_module` module and then name-space everything from there.
```rust
use some_module::some_struct;

fn use_some_struct() -> some_struct {
  return some_struct {
    // struct code
  }
}
```

You can **use the `as` keyword to `use` a module's content with a new name**. This allows you to rename name-space clashes and bring in code in any style you see fit.
```rust
use some_module::some_struct as my_struct;

let my_struct_instance = my_struct {
  // struct code
};
```

### Nested Paths
If you want to **bring multiple modules into scope from the same parent module** you can cut down on the number of `use` statements you write by nesting name-spaces inside `{}` curly braces separated by `,` commas. The code below will import `some_other_module` *and* `some_struct` from the `some_module` name-space.
```rust
use some_module::{some_other_module, some_struct};
```

You can also **specify the module itself to be imported in nested paths** using the `self` keyword. The code below will import the code directly in `some_module` as well as `some_struct`.
```rust
use some_module::{self, some_struct};
```

### Glob
You can **bring all public modules from a name-space into scope** by using the `*` asterisk or glob after the name-space path.
```rust
use some_module::*;
```

### External Files
You can **import a module from the another directory** by referencing it with `crate` keyword where **each file is treated as if it were a module**.
```
src
├── eggs
|	├── mod.rs
|   └── ham.rs
├── main.rs
└── spam.rs
```

For example, if we wanted to import the `Jam` struct from the `spam` file module we could use the import statement below.
```rust
// main.rs
use crate::spam::jam;
```
To **import a module from a sub-directory**, the sub-directory must have the file names exposed in a `mod.rs` file. For example, the `mod.rs` file for the `eggs` directory might look like this:
```rust
// eggs/mod.rs
mod ham;
```
And the equivalent import code would reference this structure via the `crate`.
```rust
// main.rs
use crate::eggs::ham;
```

## Traits

Traits are used to define shared behaviour on generics by specifying that some set of generic objects in our system have a shared set things they can do. They are similar to `interfaces` in other languages. 

### Defining traits

You can **define a new trait** by using the `trait` keyword followed by the name of the trait. The trait then describes a set of method signatures (name, input and return types) followed by a `;` semi-colon to show that the method is not yet implemented. Any structures that `implement` the trait must have a valid implementation of the methods defined by that trait.
```rust
pub trait Foo {
  fn Bar(&self) -> String;
  fn Baz(&self, fac: i32) -> i32;
}
```

You can **implement a trait on a struct** by using the `impl` keyword followed by the name of the trait with `for` keyword and the name of struct implementing the trait.
```rust
pub struct Eggs {
  name: String
  age: i32
}

impl Foo for Eggs {
  fn Bar(&self) -> String {
    format!("My name is: {}", self.name)
  }

  fn Baz(&self, fac: i32) -> i32 {
    fac * self.age
  }
}
```

You can **import traits to implement from anywhere in your project.** But you can **only implement a new trait for a struct in the file in which that struct is defined**. This limits to altering source code for structs directly so you can't add trait implementations for libraries and external resources without modifying those resources directly.

You can **provide a default implementation** for a trait.
```rust
pub trait Foo {
  fn bar(&self) -> String {
    format!("This is a default implementation")
  }
}
```

When structs **implement a trait with a default implementation** they can simply leave the `impl` blank to indicate that they want to use the default implementation **or they can override the default** by redefining the trait's method.
```rust
impl Foo for eggs { } // default implementation
```

You can also **call other methods defined in the same trait from default trait method implementations**. In this case the struct that implements `Foo` would then need to create an implementation of `baz` which would then be called by the default implementation of `bar`.
```rust
pub trait Foo {
  fn bar(&self) -> String {
    format!("Hello there...{}", self.baz())
  }

  fn baz(&self) -> String;
}
```

### Simple Trait Arguments

You can **create functions that take generic objects that implement a specific trait** as its argument. The example below defines a `use_foo` function that accepts a *reference* to any object that implements the `Foo` trait as indicated by the `impl` keyword in the argument field. This function can then use the trait in its code.
```rust
fn use_foo(foo: &impl Foo) {
  println!("{}", foo.bar());
}
```

You can **define multiple trait bounds** by enclosing trait specifications in `()` soft braces with a `+` plus concatenating them. In the example below arguments to `use_foo` must implement the `Foo` and `Qux` trait.
```rust
fn use_foo(foo: &(impl Foo + Qux)) {
  println!("{}", foo.bar());
}
```

### Trait Bound Syntax

You can also **create functions that take generic objects that implement a specific trait** by defining abstract types (such as `T`) which implement a trait. This allows for complex use cases such as differing type inputs and multiple trait specifications. Below is the code from the previous example re-written using **trait bound syntax** with a generic type `T`.
```rust
fn use_foo<T: Foo>(foo: T) {
  println!("{}", foo.bar());
}
```

You can **use trait bound syntax to pass in multiple objects that implement a trait** without having to define the `impl` for each argument.
```rust
fn use_foo<T: Foo>(foo1: T, foo2: T) {
  println!("{}", foo1.bar());
  println!("{}", foo2.bar());
}
```

You can **define MULTIPLE trait implementation parameters for arguments** by adding a `+` operator between trait names in the type definition. In the example below arguments to `use_foo` must implement the `Foo` and `Qux` trait.
```rust
fn use_foo<T: Foo + Qux>(foo: T) {
  // code using Foo and Qux trait methods
}
```

You can **define multiple trait argument types** by comma separating them.
```rust
fn use_foo<T: Foo + Qux, U: Qux + Debug>(foo: T) {
  // code using Foo and Qux trait methods
}
```

### Where syntax

Functions with many trait types and bounds can become difficult to read. You can **use the `where` syntax to define the trait bounding of arguments INSIDE the function that uses them**.
```rust
fn use_foo<T, U>(eggs: T, spam: U) {
  where T: Foo + Qux + Clone,
        U: Qux + Debug
  // code that uses trait objects and methods
}
```
## Panic

You can **manually trigger a program to panic** by using the `panic!` macro. This macro can take a `str` argument which describes the stack trace error.
```rust
panic!("Your program failed horribly!");
```

## Testing

You can **run cargo tests with `println!` statements showing** by using the `nocapture` flag.
```bash
$ cargo test -- --nocapture
```

## Rand
The `rand` crate allows you generate random numbers at run time for your program. The random number generator works by creating a `thread_rng` object that is localised to our execution thread and seeded by the operating system.
```rust
use rand::Rng;
// generate a new random number
let random_number = rand::thread_rng.gen_range(1, 101)
```
The `gen_range()` function is inclusive at its bottom end and exclusive at its top end. In the above example it will produce a number between 1 and 100.

`drain` `skip_while`

`life times`
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEyMDk3NjU3OTAsLTcxODEzNjM2MCwtMT
c5NDU5Njc2LDIwODg0OTIzNzcsMjA2MTUwNjE1MCwtMTA2OTU2
ODg5NiwxOTM2MzExNzA4LDQxMTY1MTAsLTY5OTgxNDg3Myw5OT
U2ODQ5MzMsLTE2NzA5MzkyMTMsLTE3NDE0OTE4MzAsODcwMDM5
OTI1LDM4MzM0NDcxMSwtMzUyNTc4MzUxLC0xOTUxMjEzODQ0LC
0xNzEyOTYxMjcxLDEwMTA5Mzc4NzksMjQ1OTEwNjM1LC0xMDEy
ODI2NjkwXX0=
-->