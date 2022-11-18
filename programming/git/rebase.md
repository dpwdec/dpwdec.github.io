---
title: Rebase
layout: page
exclude: true
---

You can **rewrite the message of a commit before it has been pushed** by using the `rebase` command.

First start an interactive `rebase` with the `-i` flag. If you are trying to rewrite the commit you just did then this all you need. If you want to **rewrite a commit that is several commits in the past** then use the `HEAD~n` where `n` is the number of the commits you want to go back. There's no need to get this number perfectly right just as long as you go far enough back to see the commit with the message you want to change.

```
git rebase -i HEAD~4
```

This will output a list of commits in your terminal and bring you into a vim style editor.
```
pick 57uh431 Some commit message
pick 6gffh12 Another commit message
pick po8bn33 More commit message
pick ojr5yuf The commit message

# Rebase ...
```

Navigate to the line of commit you want to rewrite in the terminal and press `i` to insert and change the text to the right of the commit hash, then change the action `pick` to `reword`. In this case we will `More commit message` to `A CHANGED commit message`.
```
pick 57uh431 Some commit message
pick 6gffh12 Another commit message
reword po8bn33 A CHANGED commit message
pick ojr5yuf The commit message

# Rebase ...
```

Press `escape` and then `:wq` to save, the rebase will run the commit will be rewritten.