#!/usr/bin/env python3
# https://codechalleng.es/bites/55

from collections import namedtuple

import feedparser

# cached version to have predictable results for testing
FEED_URL = "https://bites-data.s3.us-east-2.amazonaws.com/steam_gaming.xml"

Game = namedtuple('Game', 'title link')


def get_games():
    games = []
    feed_data = feedparser.parse(FEED_URL)

    for game in feed_data.entries:

        games.append(Game(game['title'], game['link']))

    return games
