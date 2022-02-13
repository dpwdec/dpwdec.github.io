---
layout: page
exclude: true
title: Zsh
---

If you want to **update your $PATH or profile on a mac** there's not much point using the `.bashrc` files. Instead use the `.zshrc` file. If this file doesn't exist create it in your `$HOME` / `~` directory. You can add new paths with an `export`.
```bash
#.zshrc
export PATH=$PATH:/path/to/something
```