---
title: Test
layout: page
exclude: true
---

You can **run tests from a test project** by using the `test` command.
```bash
dotnet test
```

You can **show console output** from the code being tested by using the `logger` flag set to `console`.
```bash
dotnet watch test --logger:"console;verbosity=detailed"
```