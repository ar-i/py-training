#!/usr/bin/env python3
# https://codechalleng.es/bites/108/

from collections import namedtuple

BeltStats = namedtuple('BeltStats', 'score ninjas')

ninja_belts = {'yellow': BeltStats(50, 11),
               'orange': BeltStats(100, 7),
               'green': BeltStats(175, 1),
               'blue': BeltStats(250, 5)}


# formula: belt score * belt owners (aka ninjas)
def get_total_points(belts=ninja_belts):
	results = 0
	for key, value in belts.items():
		results += value[0] * value[1]
	return results

print(get_total_points(ninja_belts))
