"""
.	--  Matches any single character. 
(Using m option allows it to match newline as well.)
"""

# Importing 're' Module
import re

string = 'When nothing goes @Right -->\
          Go, @Left <--'

# Matching
match = re.search(r'.<--', string, re.I)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'
    
# or

# Matching
match = re.search(r'.@Right', string, re.I)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'

# or

# Matching
match = re.search(r'.noth', string, re.I)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'

# or

# Matching
match = re.search(r'.go', string, re.I)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'

# or

# Matching
match = re.search(r'.@', string, re.I)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'
