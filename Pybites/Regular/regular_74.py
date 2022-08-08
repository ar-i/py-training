#!/usr/bin/env python3
# https://codechalleng.es/bites/74/

import calendar
import datetime

def weekday_of_birth_date(date):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[calendar.weekday(date.year, date.month, date.day)]
"""Takes a date object and returns the corresponding weekday string"""

