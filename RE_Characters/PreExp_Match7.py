"""
re{ n, m}	 -- Matches at least n and at most m occurrences of preceding expression.
"""

"""
I would recoomend you guys to go through RE_Patterns,
It'll halp in grasping these concepts.
"""

# Importing 're' Module
import re

string = 'When, nothing goes @Right --> \
         Go, @Left <--'

# Matching
match = re.search(r'\D{1,8}', string, re.I)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'

# or

# Matching
match = re.search(r'\S{1,8}', string, re.I)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'


# or

# Matching
match = re.search(r'\w{1,8}', string, re.I)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'

# or

# Matching
match = re.search(r'\D{4,6}', string, re.I)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'

# or

# Matching
match = re.search(r'\S{4,6}', string, re.I)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'

# or

# Matching
match = re.search(r'\w{4,6}', string, re.I)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'

