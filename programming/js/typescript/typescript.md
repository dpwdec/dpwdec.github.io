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
