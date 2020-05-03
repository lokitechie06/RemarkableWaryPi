# My solution:
def front_back(str):
  newStr=''
  if len(str)<=1:
    newStr = str
  else:
    firstChar = str[0]
    lastChar = str[-1]
    newStr = lastChar+str[1:len(str)-1]+firstChar
  return newStr


# Coding bat solution - 
def front_back(str):
  if len(str) <= 1:
    return str
  
  mid = str[1:len(str)-1]  # can be written as str[1:-1]
  
  # last + mid + first
  return str[len(str)-1] + mid + str[0]

'''
Test cases
Expected	Run		
front_back('code') → 'eodc'	'eodc'	OK	
front_back('a') → 'a'	'a'	OK	
front_back('ab') → 'ba'	'ba'	OK	
front_back('abc') → 'cba'	'cba'	OK	
front_back('') → ''	''	OK	
front_back('Chocolate') → 'ehocolatC'	'ehocolatC'	OK	
front_back('aavJ') → 'Java'	'Java'	OK	
front_back('hello') → 'oellh'	'oellh'	OK
'''

