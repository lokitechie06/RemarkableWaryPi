def without_end(str):
  return str[1:len(str)-1]


'''
Expected	Run		
without_end('Hello') → 'ell'	'ell'	OK	
without_end('java') → 'av'	'av'	OK	
without_end('coding') → 'odin'	'odin'	OK	
without_end('code') → 'od'	'od'	OK	
without_end('ab') → ''	''	OK	
without_end('Chocolate!') → 'hocolate'	'hocolate'	OK	
without_end('kitten') → 'itte'	'itte'	OK	
without_end('woohoo') → 'ooho'	'ooho'	OK
'''