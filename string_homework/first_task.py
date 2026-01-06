import string
import keyword
punctuation = string.punctuation.replace("_", " ")
result = True
name = input("Enter variable name:")
if name in keyword.kwlist:
    result = False
elif name[0].isdigit():
    result = False
elif name.count("_") > 1:
    result = False
else:
    for letter in name:
        if letter.isupper() or letter in punctuation:
            result = False
            break
