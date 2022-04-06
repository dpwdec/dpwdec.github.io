---
title: Narrowing
layout: page
exclude: true
---

When working with **union types** that require a narrowing of the types context to take an action **typescript will automatically infer type narrowing** from conditionals overlaying its compiler type checking narrowing on the javsscript runtime for `if`/`else`.
```ts
const f = (x: number | string) => {
  return x.toUpperCase(); // error because function not on number
}

const f = (x: number | string) => {
  if (typeof(x) == "string") {
    return x.toUpperCase(); // state of x is automatically inferred as string
  } else {
    return x;
  }
}
```

Both **arrays and `null` are `typeof` `"object"`**. Type guarding using `typeof x == "object"` will *not* narrow down types that can be array and `null`.

You can **narrow types based on equality of values**. In the example below, if `x` and `y` are equal they both must be of type `string` which the typescript compiler can infer.
```ts
const f = (x: number | string, y: string) => {
  if (x === y) {
    x.toUpperCase(); // x is inferred to be a string here
  } else {
    // do nothing
  }
}
```

You can **narrow types using the `in` operator**. The `in` operator checks if an object contains a property using a string key. If a specific type is known to have a unique key by the typescript compiler and an object is identified as having that property then its type will be narrowed to that. The `false` branch of this check will *also* narrow the type.
```ts
type Writer = { write: () => null };
type Painter = { paint: () => null };

const do = (job: Writer | Painter) => {
  if ("write" in job) { // narrows type to Writer
    job.write();
  }

  // by implication that type here is now Painter
  job.Paint();
}
```

You can **narrow using `instanceof`** in essentially the same way.

## Type Predicates

You can **create functions that assert on the type of an object** using type predicates. Type predicates take the format `parameteName is T` and are the return of functions. When a that accepts a parameter with wider types and narrows its types using a type predicate, the typescript compiler will understand in functions that use that parameter that is has been narrow. The predicate function should return a boolean that indicates whether the parameter is or is not that type.
```ts
const isWriter = (job: Writer | Painter): job is Writer {
  return (job as Writer).write !== undefined;
}

const job = { write: () => null };
if (isWriter(job)) { // the predicate narrows the types of the branches here
  job.write();
} else {
 job.paint();
}
```

You can even **pass these predicate functions into higher order functions**.
```ts
const isString = (x: string | number): x is string {
    return (x as string).toUpperCase !== undefined;
}

const strumbers: (string | number)[] = [1, "2", 3, 4, "5"];

const strings: string[] = strumbers.filter(isString); // => ["2", "5"]
```

