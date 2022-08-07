#!/usr/bin/env python3
# https://codechalleng.es/bites/4/

import os
from collections import Counter
import urllib.request
import xml.etree.ElementTree as ET
#import re

# NOTES
# Things I have tried so far:
# * regex - despite working in regex-testers,
# (?<=<category>).*(?=<\/category>), does not work.
# * using ET - same issue, no matter what method I call on the string, I get
# either nothing or the entire string, not single tags

tmp = os.getenv("TMP", "/tmp")
tempfile = os.path.join(tmp, 'feed')

# Temporarily disabled because the file already exists on my disk, I don't want
# to re-fetch it every single time I run the script.
#urllib.request.urlretrieve(
#    'https://bites-data.s3.us-east-2.amazonaws.com/feed',
#    tempfile
#)

with open(tempfile) as f:
    content = f.read().lower()

def get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""
    pass
