---
title: Typescript
layout: page
exclude: true
---

By default **typescript will update compiled output files even if there are compilation errors**. You can **stop typescript from compiling if there are compilation errors** by using the `--noEmitOnError` flag.
```bash
tsc --noEmitOnError my-app.ts
```

You can **turn off warnings for unused variables** such as `'variable' is declared but its value is never read.` by using the `noUnusedLocals` property in the `tsconfig.json` file.
```json
{
  "compilerOptions": {
	 ...
    "noUnusedLoals": true,
    ...
  }
}
```

## ECMAScript Targets

By default the **typescript compiles down to vanilla javascript compatible with ECMAScript 3**. This removes many newer language features from Javascript.

You can **target new versions of javascript** using the `--target` flag.
```bash
tsc --target es2015 my-app.ts
```

## Strictness

By default **typescript does not enforce strict type checking**.

You can **enable strict type checking** using the `--strict` flag.

The `--strictNullChecks` flag will **ensure that a nullable value can only used if its state is guaranteed**. This is done by making `null` and `undefined` there own types which are not assingable to other properties.

The `--noImplicitAny` flag will **ensure that if the compiler impiles a value is of type `any` it will cause an error**. So you must *explicitly* mark values that take an `any` type.


## Functions

The **types in anonymous functions are inferred** by typescript. The example below demonstrates how typescript tracks the internal type passed to the function.
```ts
let x = [1, 2, 3, 4];

x.forEach(n => n.toUpperCase()) // throws an error because number cannot be converted to upper case
```


## Narrowing

When working with **union types** that require a narrowing of the types context to take an action **typescript will automatically infer type narrowing** from conditionals.
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