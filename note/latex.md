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

You can **define the font size of your document** by submitting it as an argument to the class. The default font size in `10pt`.
```latex
\documentclass[12pt]{article}
```

You can **define the paper size that your document uses** by submitting it as argument to the class with a paper size specifier. Common specifiers are `letterpaper`, `a4paper` or `legalpaper`.
```latex
\documentclass[a4paper]{article}
```

You can **pass multiple arguments into the class specifier** by comma separating them.
```latex
\documentclass[12pt, legalpaper]{article}
```

## Encoding

You can **set the document type encoding** from the `\usepackage` command with an argument of the encoding type and `inputenc` specifier.
```latex
\usepackage[utf8]{inputenc}
```

## Document Titles

You can **set the title of your document in the preamble** using the `title` property.
```latex
\title{My Document}
```

You can **set the author of your document in the preamble** using the `author` property.
```latex
\author{Dec}
```

You can **set the date of your document in the premable** using the `date` property.
```latex
\date{12 July 2020}
```

Importantly, none of these will appear by default in the actual document, if you want to render this information to display in the document with a title you will need to use the `maketitle` command inside the `begin` tags of the document. This will print the formatted information defined in the premable to the document.
```latex
\begin{document}
\maketitle
\end{document}
```

# Body

The text of your document is placed between the `begin` and `end` tags that mark the body of the document.
```latex
\begin{document}
Some document text
\end{document}
```

## Comments

You can **add comments to your document** by using the `%` percent sign indicator.
```latex
\begin{document}

This text will be rendered.

% This next will NOT be rendered.
\end{document}
```

## Formatting


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEyMzU4Nzg4MDQsLTE3MDg5MjIzNDksNT
I4NjA2NDA1XX0=
-->