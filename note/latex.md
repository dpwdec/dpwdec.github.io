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

## Structure

You can **create section headings in your document** using the `section` indicator.
```latex
\section{Introduction}
Some introduction text.
\section{About}
Some about text.
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

### Emphasis

You can **add bold text** with the `textbf` flag.
```latex
\textbf{some text}
```

You can **add underlined text** with the `underline` flag.
```latex
\underline{some text}
```

You can **add italics** with the `textit` flag.
```latex
\textit{some text}
```

You can **add these emphasis indicators contextually** with the `emph` flag. This will italicise regular text and embolden italic text.
```latex
\emph{some text}
```

You can **nest formatting styles**.
```latex
\underline{\textbf{some text}}
```

### Spacing

You can **perform a line break** with `\\` double backslashes. The line break **must follow some text** otherwise it is considered invalid.
```latex
Here is some text
\\
And some more text after a line break
```

You can **make an arbitrary break in text** using the `vskip` command followed by the distance of the break.
```latex
Some text
\vskip 0.2in
More text after the break.
```

You can **remove automatic indents from a line of text** by enclosing it in the `noindent` macro.
```latex
\noindent{Text that would have had an indent.}
```

## Lists

You can **create lists** by using a `begin` and `end` environment with the list environment indicator. You can **create an unordered list** with the `itemsize` indicator. Each element in the list should have the `\item` indicator before it.
```latex
\begin{itemize}
  \item A list item
  \item Another list item
  \item A further list item
\end{itemize}
```

You can **create an ordered list** by using the `enumerate` flag in the same manner as the unordered list flag.
```latex
\begin{enumerate}
  \item A list item
  \item Another list item
  \item A further list item
\end{enumerate}
```

## Tables

You can **add lines breaks to table cells** using the `makecell` package.
```latex
\usepackage{makecell}

\begin{document}

  \begin{center}
    \begin{tabular}{ | c | c | c |}
      \hline
      \thead{A Head} & \thead{A Second \\ Head} & \thead{A Third \\ Head} \\
      \hline
      Some text &  \makecell{Some really \\ longer text}  & Text text text  \\
      \hline
    \end{tabular}
  \end{center}

\end{document} 
```

## Math

You can **insert math into a line of text** by using `$ ... $` two dollars signs, a `\( ... \)` two escape brackets or a `begin{math} ... end{math}` indicator.
```latex
A famous equation was $E=mc^2$ coined by Monsieur Einstein.
```

## TexShop

You can **make the code text BIGGER** by *selecting* the code and then using the `CMD` and `+` keybinding for zooming. This can also be used for **making code text smaller**.

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTMxMjY5MTAyNSwtODY0MjQwNzEyLC0xOD
U0MjYxNTEzLDM0NTk5OTc4MCwxNjg2Njg0Njk1LDE1ODQwMzM3
NDAsMTE5MzE1NjU0NywtMTIzNTg3ODgwNCwtMTcwODkyMjM0OS
w1Mjg2MDY0MDVdfQ==
-->