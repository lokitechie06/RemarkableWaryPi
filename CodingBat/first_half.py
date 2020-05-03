def first_half(str):
  if len(str)%2==0:
    return str[:len(str)/2]


'''
Expected	Run		
first_half('WooHoo') → 'Woo'	'Woo'	OK	
first_half('HelloThere') → 'Hello'	'Hello'	OK	
first_half('abcdef') → 'abc'	'abc'	OK	
first_half('ab') → 'a'	'a'	OK	
first_half('') → ''	''	OK	
first_half('0123456789') → '01234'	'01234'	OK	
first_half('kitten') → 'kit'	'kit'	OK	
'''