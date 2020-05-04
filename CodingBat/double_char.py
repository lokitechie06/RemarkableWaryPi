def double_char(str):
  newstr = ''
  for ch in str:
    newstr += 2 * ch
    
  return newstr


# coding bat solution:
def double_char(str):
  result = ""
  for i in range(len(str)):
    result += str[i] + str[i]
  return result

'''
Expected	Run		
double_char('The') → 'TThhee'	'TThhee'	OK	
double_char('AAbb') → 'AAAAbbbb'	'AAAAbbbb'	OK	
double_char('Hi-There') → 'HHii--TThheerree'	'HHii--TThheerree'	OK	
double_char('Word!') → 'WWoorrdd!!'	'WWoorrdd!!'	OK	
double_char('!!') → '!!!!'	'!!!!'	OK	
double_char('') → ''	''	OK	
double_char('a') → 'aa'	'aa'	OK	
double_char('.') → '..'	'..'	OK	
double_char('aa') → 'aaaa'	'aaaa'	OK
'''