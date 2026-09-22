def casefold_string(string):
    return string.casefold()

print(casefold_string("Hello"))

def casefold_string(string1, string2):
    return string1.casefold() == string2.casefold()

print(casefold_string("Hello","hello"))