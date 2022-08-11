#!/usr/bin/env python3

import pickle

hackers = {"neut": 1, "geohot": 100, "neo": 1000}

serialized = pickle.dumps(hackers)
hackers_v2 = pickle.loads(serialized)

with open("hackers.pickle", "wb") as handle:
    pickle.dump(hackers, handle)

with open("hackers.pickle", "rb") as handle:
    hackers_v3 = pickle.load(handle)

print(hackers_v3)
