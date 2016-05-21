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



# or



# or



# or
