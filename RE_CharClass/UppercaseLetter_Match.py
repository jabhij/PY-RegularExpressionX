"""
[A-Z]	 --  Match any uppercase ASCII letter
"""

# Importing 're' Module
import re

string = 'When, nothing goes @Right --> \
          Go, @Left <--'

# Matching
match = re.search(r'[W]', string)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'

# or

# Matching
match = re.search(r'[R]', string)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'


# or

# Matching
match = re.search(r'[L]', string)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'

# or

# Matching
match = re.search(r'[e]', string)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'

# or

# Matching
match = re.search(r'[g]', string)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'

# or

# Matching
match = re.search(r'[S]', string)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'
