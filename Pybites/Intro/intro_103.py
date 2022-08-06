#!/usr/bin/env python3
# https://codechalleng.es/bites/103/

GAME_STATS = dict(sara=0, bob=1, tim=5, julian=3, jim=1)

def print_game_stats(games_won):
	for player, wins in games_won.items():
		if wins == 1:
			print(f"{player} has won {wins} game")
		else:
			print(f"{player} has won {wins} games")

print_game_stats(GAME_STATS)
