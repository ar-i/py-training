#!/usr/bin/env python3
# https://codechalleng.es/bites/46

from typing import Union

def fizzbuzz(num: int) -> Union[str, int]:
    # That's hideous and I am genuinely proud that I came up with that.
    return [num if num % 3 != 0 and num % 5 != 0 else "Fizz Buzz" if num % 3 == 0 and num % 5 == 0 else "Fizz" if num % 3 == 0 else "Buzz"][0]

