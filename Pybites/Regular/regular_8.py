#!/usr/bin/env python3
# https://codechalleng.es/bites/8/

def rotate(string, n):
    left_1 = string[0:n]
    left_2 = string[n:]
    right_1 = string[0:len(string)+n]
    right_2 = string[len(string)+n:]

    if n > 0:
        return left_2 + left_1
    if n < 0:
        return right_2 + right_1

print(rotate("hello", 2))
print(rotate("hello", -2))
