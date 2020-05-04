def front_times(str, n):
  if len(str) <= 3:
    return str * n
  else:
    return str[:3]*n


'''
Expected	Run		
front_times('Chocolate', 2) → 'ChoCho'	'ChoCho'	OK	
front_times('Chocolate', 3) → 'ChoChoCho'	'ChoChoCho'	OK	
front_times('Abc', 3) → 'AbcAbcAbc'	'AbcAbcAbc'	OK	
front_times('Ab', 4) → 'AbAbAbAb'	'AbAbAbAb'	OK	
front_times('A', 4) → 'AAAA'	'AAAA'	OK	
front_times('', 4) → ''	''	OK	
front_times('Abc', 0) → ''	''	OK	
'''