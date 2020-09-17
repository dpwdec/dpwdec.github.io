---
title: Vs Code
layout: page
exclude: true
---
You can **open a folder in VS code from the command line** by using the `code` keyword followed by the `r` flag and then the name of the folder.
```bash
$ code -r MyProject
```

You can **select an entire word or symbol** using the `CMD + D` shortcut. By pressing this keyboard shortcut multiple times you will switch **multi-word editing mode**, this will select each same word after the initial word you selected you can then type to replace them.

You can **configure code formatting settings by language type** by editing vs codes `settings.json` file. [To do this](https://stackoverflow.com/questions/34247939/how-to-set-per-filetype-tab-size):

1. Use the keyboard shortcut `CMD + SHIFT + P`
2. Type into the search box `Preferences: Configure Language Specific Settings`
3. Select the language you want to customise editor settings for. This will open the `settings.json` file with a new entry for that language.
4. Create a new key-value pair (or edit an existing one) inside the language specific entry that indicates what changes you want in the editor.
 
In the below example of the `settings.json` file is edited for python to set the default tab size for that language to `4`.
```json
{
  "editor.tabSize": 2,
  "window.zoomLevel": 1,
  "editor.renderWhitespace": "all",
  "workbench.colorTheme": "Atom One Dark",
  "[python]": {
    "editor.tabSize": 4
  }
}
```

To **open the commands window** `CTRL` + `SHIFT` + `P`.

You can **add the `code` CLI namespace to your machine** by using triggering the `>shell command` in the vs code commands window.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE0MTk1MjAzMzAsMjY0NzYyOTcwLDEzMT
c3OTczOTYsMTM4MjYzMDE0MCwtMTczNzkwMjU3MSwtMTAzODkx
MDIwM119
-->