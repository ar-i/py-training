#!/usr/bin/env python3
# https://codechalleng.es/bites/318/

import base64
import csv
from typing import List  # will remove with 3.9

def get_credit_cards(data: bytes) -> List[str]:
	credit_cards = []
	decoded_data = base64.b64decode(data).decode("ASCII").split("\n")
	# Remove that empty string that's in there for some reason.
	cleaned_data = [x for x in decoded_data if x]
	for dataset in cleaned_data:
		credit_cards.append(dataset.split(",")[2])
	# Not exactly elegant: Remove the heading
	credit_cards.pop(0)
	return credit_cards

"""Decode the base64 encoded data which gives you a csv
of "first_name,last_name,credit_card", from which you have
to extract the credit card numbers.
"""

