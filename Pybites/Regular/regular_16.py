#!/usr/bin/env python3
# https://codechalleng.es/bites/16/

from datetime import datetime, timedelta
from itertools import islice

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    future_100 = PYBITES_BORN + timedelta(days=100)
    yield future_100
    while True:
        future_100 += timedelta(days=100)
        yield future_100
    #print(future_100)
    #print(type(future_100))

gen = gen_special_pybites_dates()
dates = list(islice(gen, 10))
print(dates)

'''
from datetime import datetime
from itertools import islice

from gendates import gen_special_pybites_dates


def test_gen_special_pybites_dates():
    gen = gen_special_pybites_dates()
    dates = list(islice(gen, 10))
    expected = [datetime(2017, 3, 29, 0, 0),
                datetime(2017, 7, 7, 0, 0),
                datetime(2017, 10, 15, 0, 0),
                datetime(2018, 1, 23, 0, 0),
                datetime(2018, 5, 3, 0, 0),
                datetime(2018, 8, 11, 0, 0),
                datetime(2018, 11, 19, 0, 0),
                datetime(2019, 2, 27, 0, 0),
                datetime(2019, 6, 7, 0, 0),
                datetime(2019, 9, 15, 0, 0)]
    assert dates == expected'''
