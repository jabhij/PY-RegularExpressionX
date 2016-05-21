"""
exp*	 --  Matches 0 or more occurrences of preceding expressions
"""

# Importing 're' Module
import re

string = 'She sells seashells by the seashore.'

# Matching
match = re.search(r's*', string, re.I)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'
    
# or

# Matching
match = re.search(r'se*', string, re.I)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'
    
    
# or

# Matching
match = re.search(r'sel*', string, re.I)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'
    
# or

# Matching
match = re.search(r'she*', string, re.I)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'
    
# or

# Matching
match = re.search(r'b*', string, re.I)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'
    
# or

# Matching
match = re.search(r'sea*', string, re.I)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'

# or

# Matching
match = re.search(r'th*', string, re.I)
if match:
    print 'Match:', match.group()
else:
    print 'Try Something Else!'
