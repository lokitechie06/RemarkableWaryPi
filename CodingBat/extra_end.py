def extra_end(str):
  return str[-2:]*3

'''
Expected	Run		
extra_end('Hello') → 'lololo'	'lololo'	OK	
extra_end('ab') → 'ababab'	'ababab'	OK	
extra_end('Hi') → 'HiHiHi'	'HiHiHi'	OK	
extra_end('Candy') → 'dydydy'	'dydydy'	OK	
extra_end('Code') → 'dedede'	'dedede'	OK	
other tests OK
'''