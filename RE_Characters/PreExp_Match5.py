"""
re{ n,}	 --  Matches n or more occurrences of preceding expression.
"""

# Importing 're' Module
import re

string = 'When, nothing goes @Right --> \
         Go, @Left <--'

# Matching
match = re.search(r'\D{3,}', string, re.I)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'

# or

# Matching
match = re.search(r'\D{5,}', string, re.I)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'


# or

# Matching
match = re.search(r'\D{1,}', string, re.I)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'

# or

# Matching
match = re.search(r'\w{2,}', string, re.I)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'

# or

# Matching
match = re.search(r'\w{6,}', string, re.I)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'

# or

# Matching
match = re.search(r'\S{4,}', string, re.I)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'

# or

# Matching
match = re.search(r'\S{5,}', string, re.I)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'

# or

# Matching
match = re.search(r'\S{6,}', string, re.I)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'
