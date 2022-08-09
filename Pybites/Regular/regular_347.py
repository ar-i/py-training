#!/usr/bin/env python3
# https://codechalleng.es/bites/347/

from enum import Enum
from collections import Counter

# On Enums: https://docs.python.org/3.11/howto/enum.html
class Hand(str, Enum):
    RIGHT = "right"
    LEFT = "left"
    BOTH = "both"


LEFT_HAND_CHARS = set("QWERTASDFGZXCVB")
RIGHT_HAND_CHARS = set("YUIOPHJKLNM")


def get_hand_for_word(word: str) -> Hand:
	# I didn't came up with this entirely by myself, the idea was there,
	# but the final implementation was pretty much stolen verbatim from
	# https://stackoverflow.com/questions/20726010/how-to-check-if-a-string-contains-only-characters-from-a-given-set-in-python
	if all(character in LEFT_HAND_CHARS for character in word.replace(" ", "").upper()):
		return Hand.LEFT
	elif all(character in RIGHT_HAND_CHARS for character in word.replace(" ", "").upper()):
		return Hand.RIGHT
	else:
		return Hand.BOTH
