def string_bits(str):
  yeilded = ''
  for i in range(0, len(str), 2):
     yeilded += str[i]
  return yeilded


'''
Expected	Run		
string_bits('Hello') → 'Hlo'	'Hlo'	OK	
string_bits('Hi') → 'H'	'H'	OK	
string_bits('Heeololeo') → 'Hello'	'Hello'	OK	
string_bits('HiHiHi') → 'HHH'	'HHH'	OK	
string_bits('') → ''	''	OK	
string_bits('Greetings') → 'Getns'	'Getns'	OK	
string_bits('Chocoate') → 'Coot'	'Coot'	OK	
string_bits('pi') → 'p'	'p'	OK	
string_bits('Hello Kitten') → 'HloKte'	'HloKte'	OK	
string_bits('hxaxpxpxy') → 'happy'	'happy'	O
'''