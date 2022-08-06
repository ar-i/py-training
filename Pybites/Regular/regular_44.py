#!/usr/bin/env python3
# https://codechalleng.es/bites/44/

import string
import secrets


def gen_key(parts: int = 4, chars_per_part: int = 8) -> str:
    alphabet = string.ascii_letters + string.digits
    key = []

    for part in range(parts):
        subpart = ''.join(secrets.choice(alphabet) for i in
                range(chars_per_part))
        key.append(subpart.upper())

    return "-".join(key)

print(gen_key())
