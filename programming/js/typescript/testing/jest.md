---
title: Jest
layout: page
exclude: true
---

## ts-jest

`ts-jest` is a **jest pre-compiler** that can be set in the `preset` field of the `jest.config.js` file to allow you to test typescript files.

To **start using `ts-jest`** you will need to install `jest` and the `@types/jest` packages as dependencies.
```bash
npm i -D jest ts-jest @types/jest
```

You can **initialize your typescript jest testing project** using the `ts-jest config:init` command.
```bash
npx ts-jest config:init
```

This will add `ts-jest` as a `preset` for configuring jest tests in the `jest.config.js` file. *A jest `preset` is another module that contains a `jest-preset` file from which configuration for just can be loaded.*
```js
// jest.config.js
/** @type {import('ts-jest/dist/types').InitialOptionsTsJest} */
module.exports = {
  preset: 'ts-jest',
  testEnvironment: 'node',
};
```

## babel

You can **use babel to facilitate testing** by simply adding a `babel.config.js` file to your project's root folder with the preset env and typescript modules configured.
```js
// babel.config.js
module.exports = {
  presets: [
    ['@babel/preset-env', {targets: {node: 'current'}}],
    '@babel/preset-typescript',
  ],
};
```

You will also need to install dependencies with...
```bash
npm i -D babel-jest @babel/core @babel/preset-env @babel/preset-typescript
```

Now you can simply run the `jest` command to start tests and babel will automatically integrate typescript file. This somewhat more direct and easier than `ts-jest` *however* Babel does *not* type check test code which `ts-jest` does.