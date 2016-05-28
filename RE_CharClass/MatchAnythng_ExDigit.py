"""
[^0-9]	--  Match anything other than a digit
"""

# Importing 're' Module
import re

string = 'Two 2\'s are 4'

# Matching
match = re.search(r'[^2]', string, re.I)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'

# or

# Matching
match = re.search(r'[^4]', string, re.I)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'
