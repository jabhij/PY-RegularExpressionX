"""
[^aeiou]	--  Match anything other than a lowercase vowel
"""

# Importing 're' Module
import re

string = 'When, nothing goes @Right --> \
         Go, @Left <--'

# Matching
match = re.search(r'[^aeiou]', string, re.I)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'
    
# or

# Matching
match = re.search(r'[^o]', string, re.I)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'
    
# or

# Matching
match = re.search(r'[^i]', string, re.I)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'
    
# or

string = 'I\'m into python.'

# Matching
match = re.search(r'[^o]', string, re.I)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'
