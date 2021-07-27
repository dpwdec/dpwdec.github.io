---
title: gspread
layout: page
exclude: true
---

You can **get the "next empty row" in your spreadsheet** to insert new data into by getting the `len` of the `get_all_values` function result and adding `1` to it. *This only ever returns the last row of your data and doesn't do anything fancy to fill in actual empty rows*.