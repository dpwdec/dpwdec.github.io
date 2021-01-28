---
title: Concerns
layout: page
exclude: true
---

A **concern** is a component of a system grouped by its functionality.

There are **two types of concern**:

1. **Core concerns**: These are primary, specific parts of your system functionality, for example: business logic. *Each of these will be modularised and will execute the core behavior  requirements of your application's spec*.
2. **Crosscutting concerns**: These are secondary system requirements that are applicable at every level of your application, for example: logging, dependency injection, security. *Each module in your system will need to interact with these concerns (all modules will need some logging infrastructure) to some degree regardless of its specific behavior, so these concerns crosscut through your entire application scope*.

![enter image description here](https://i.stack.imgur.com/0xO3n.jpg)
<!--stackedit_data:
eyJoaXN0b3J5IjpbMzc2NTQwNDA5XX0=
-->