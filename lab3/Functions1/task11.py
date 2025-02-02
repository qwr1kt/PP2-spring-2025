def is_polyndrome(my_string):
    return my_string == my_string[::-1]

print(is_polyndrome("abba"))
print(is_polyndrome("apple"))
