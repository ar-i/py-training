#!/usr/bin/env python3
# https://codechalleng.es/bites/68

def remove_punctuation(input_string):
    forbidden_string = "!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"
    results = "".join([x for x in input_string if x not in forbidden_string])
    return(results)

print(remove_punctuation("Pipi.Papa!Popo*"))
