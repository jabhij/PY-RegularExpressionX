"""
[^...]	--  Matches any single character not in brackets
(Just opposite of-- [...])
"""

# Importing 're' Module
import re

string = 'When nothing goes @Right -->\
          Go, @Left <--'

# Matching
match = re.search(r'[^w]', string, re.I)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'

# or

# Matching
match = re.search(r'[^wh]', string, re.I)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'

# or

# Matching
match = re.search(r'[^whe]', string, re.I)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'

# or

# Matching
match = re.search(r'[^@Lef]', string, re.I)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'

# or

# Matching
match = re.search(r'[^When]', string, re.I)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'

# or

# Matching
match = re.search(r'[^nothin]', string, re.I)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'
