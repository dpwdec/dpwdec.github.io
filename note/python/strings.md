---
title: Strings
layout: page
exclude: true
---

You can **remove a character from a python script** using the `strip` function. It seems that you may *have* to use `''` single quotes around the `strip` argument for this to work.
```python
'hello there\n'.strip('\n') # => 'hello there'
```

If you want to **remove trailing characters at the end of a string** use the `rstrip` method. 

You **must use single quotes `''` inside an `f` string** if you want to specify string types inside of it. For example, using the property from a `dict` inside an `f` string. The following would break if `dict_key` was surrounded by `""` double quotes.
```python
my_string = f"Get some value from {my_dict['dict_key']} for this string"
```

You can **replace an N number of occurrences of a substring within a string** by using a third argument slot in the `replace` method to indicate how many instances you want replaced.
```python
x = "There once was a fox from foxton who was in love with a fox."
print(x.replace("fox", "badger", 2))
# => 'There once was a badger from badgerton who was in love with a fox.'
```

You can **substitute dictionary values into strings** by putting the name of keys of properties in the dictionary
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTQ5NTI3NDc4OCw2NTc0NTgzMjJdfQ==
-->