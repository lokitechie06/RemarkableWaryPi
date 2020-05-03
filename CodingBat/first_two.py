def first_two(str):
  if len(str)>2:
    return str[0:2]
  elif len(str)<=2:
    return str
  else:
    return ''

# coding bat solution
def first_two(str):
  if len(str) >= 2:
    return str[:2]
  else:
    return str

'''
Expected	Run		
first_two('Hello') → 'He'	'He'	OK	
first_two('abcdefg') → 'ab'	'ab'	OK	
first_two('ab') → 'ab'	'ab'	OK	
first_two('a') → 'a'	'a'	OK	
first_two('') → ''	''	OK	
first_two('Kitten') → 'Ki'	'Ki'	OK	
first_two('hi') → 'hi'	'hi'	OK	
first_two('hiya') → 'hi'	'hi'	OK
'''