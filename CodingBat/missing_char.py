def missing_char(str, n):
  newStr = str.replace(str[n],'')
  return newStr

'''
Test cases:
Expected	Run		
missing_char('kitten', 1) → 'ktten'	'ktten'	OK	
missing_char('kitten', 0) → 'itten'	'itten'	OK	
missing_char('kitten', 4) → 'kittn'	'kittn'	OK	
missing_char('Hi', 0) → 'i'	'i'	OK	
missing_char('Hi', 1) → 'H'	'H'	OK	
missing_char('code', 0) → 'ode'	'ode'	OK	
missing_char('code', 1) → 'cde'	'cde'	OK	
missing_char('code', 2) → 'coe'	'coe'	OK	
missing_char('code', 3) → 'cod'	'cod'	OK	
missing_char('chocolate', 8) → 'chocolat'	'chocolat'	OK	
'''