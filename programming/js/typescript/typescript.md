---
title: Typescript
layout: page
exclude: true
---

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
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTk0NzQ1MzYyMSwxMTIwMjE2NTE5XX0=
-->