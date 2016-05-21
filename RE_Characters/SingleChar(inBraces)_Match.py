"""
[...]	 --  Matches any single character in brackets.
"""

# Importing 're' Module
import re

string = 'When nothing goes @Right -->\
          Go, @Left <--'

# Matching
match = re.search(r'[w]', string, re.I)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'

# or

# Matching
match = re.search(r'[wh]', string, re.I)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'
    
# or

# Matching
match = re.search(r'[when]', string, re.I)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'
    
# or

# Matching
match = re.search(r'[go]', string, re.I)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'
    
# or

# Matching
match = re.search(r'[@]', string, re.I)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'
