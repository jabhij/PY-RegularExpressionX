"""
re{n}	--  Matches exactly n number of occurrences of preceding expression.
(Where n is a natural number)
"""

# Importing 're' Module
import re

string = 'When, nothing goes @Right --> \
         Go, @Left <--'

# Matching
match = re.search(r'\D{3}', string, re.I)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'

# or

# Matching
match = re.search(r'\D{5}', string, re.I)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'


# or

# Matching
match = re.search(r'\D{9}', string, re.I)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'

# or

# Matching
match = re.search(r'\w{2}', string, re.I)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'

# or

# Matching
match = re.search(r'\w{7}', string, re.I)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'

# or

# Matching
match = re.search(r'\S{4}', string, re.I)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'

# or

# Matching
match = re.search(r'\D{15}', string, re.I)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'

# or

# Matching
match = re.search(r'\S{6}', string, re.I)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'
