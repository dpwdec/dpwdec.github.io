---
title: Latex
layout: page
exclude: true
---
Latex is a type-setting engine that allows for full controlling of document formatting and content control.

# Preamble
The `preamble` section of a Latex document is any information that comes before the `begin` tag of the document. This section is not rendered to the page and defines meta information about the document such as `class`, sizing or character type.

## Classes

You can **define a document class** by using `documentclass` tag to specify the overall layout and type of your document. This is defined at the head of your document file with the class of document inside `{}` curly brackets.
```latex
\documentclass{article}
```

## Document

The text of your document is placed between the `begin` and `end` tags that mark the body of the document.
```latex
\begin{document}
Some document text
\end{document}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTc5MDQ1NTI1Nyw1Mjg2MDY0MDVdfQ==
-->