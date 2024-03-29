---
title: Vs Code
layout: page
exclude: true
---

## Code

You can **install the VS code command line tool** by using `CMD + SHIFT + P` and using the `shell command` installation feature.
```
>shell command: Install 'code' command in PATH
```

You can **open a folder in VS code from the command line** by using the `code` keyword followed by the `r` flag and then the name of the folder.
```bash
$ code -r MyProject
```

You can **select an entire word or symbol** using the `CMD + D` shortcut. By pressing this keyboard shortcut multiple times you will switch **multi-word editing mode**, this will select each same word after the initial word you selected you can then type to replace them.

## Settings

All the **non-default settings for vs code are controlled using a `settings.json` file**. To open this file use `CMD + SHIFT + P` to open the vs code command window and then use the `Preferences: Open Settings (JSON)` command.
```
>Preferences: Open Settings (JSON)
```

You can **change the size of the vs code terminal text** by using the `terminal.integrated.fontSize` property. You will need to **restart the terminal** to see an effect.
```json
{
  "terminal.integrated.fontSize": 14
}
```

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

## Search

You can **search your entire project** using the global search function by pressing `CMD` + `SHIFT` + `F`.

You can **narrow your search to a particular directory** by clicking the `...` three dots on the search window and in the `files to include` section putting in a relative path from the root directory with `.` period, current directory indicator. The query below would only search in the `src` directory which is a directory contained in the root.
```
./src
```

## Error Highlighting

Often you will need to add a `.vscode` file to your to **enable error handling**.

## Git

You can **create a new branch of your current project** by opening the vscode command window and using the `git checkout` command and then selecting a `new branch` and adding the name of the branch.
```
>Git Checkout
```

## Tab

You can **toggle tab to move focus** instead of inserting tabs by pressing `CTRL + SHIFT + M` on Mac and `CTRL + M` on Windows.

## Error Highlighting

If your **dotnet code is missing error highlighting in editor** you probably need to restart Omnisharp. Do this with `CTRL + SHIFT + P` and then `>Restart Omnisharp`.