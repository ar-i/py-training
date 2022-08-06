#!/usr/bin/env python3
# https://codechalleng.es/bites/29/

import string

def get_index_different_char(chars):
    alphanumerical = string.digits + string.ascii_uppercase +\
    string.ascii_lowercase
    numerical = {}
    non_numerical = {}

    for character in chars:
        if str(character) in alphanumerical and len(str(character)) > 0:
            numerical[chars.index(character)] = character
        else:
            non_numerical[chars.index(character)] = character

    print(numerical)
    print(non_numerical)
    if len(numerical) > len(non_numerical):
        return list(non_numerical.keys())[0]
    else:
        return list(numerical.keys())[0]

#chars = ['=', '=', '', '/', '/', 9, ':', ';', '?', '¡']
chars = ['=', '=', '', '/', '/', 9, ...]

print(get_index_different_char(chars))
