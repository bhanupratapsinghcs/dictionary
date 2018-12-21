# UNDERSTANDING METHODS IN DIFFLIB LIBRARY

import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches
# SequenceMatcher
# 3 parameters
# 1: junk - word has white spaces or blank lines - our case: None
# 2 & 3: words for comparison
# append ratio() method
value = SequenceMatcher(None, "boook", "book").ratio()
print(value)
# output: 0.8888888888 i.e 89% similarity

# get_close_matches
# 4 parameters
# 1: word for which we want to find close matches
# 2: list of words to match against
# 3: how many matches we need?
# 4: cutoff: ratio
output = get_close_matches("sun", ["moon", "sunny", "soil", "sand"], n=1, cutoff=0.75)
print(output)
# output: first close match
