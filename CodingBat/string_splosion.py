def string_splosion(str):
  xplosed = ''
  for i in range(len(str)+1):
    xplosed += str[:i]
  return xplosed


'''
Expected	Run		
string_splosion('Code') → 'CCoCodCode'	'CCoCodCode'	OK	
string_splosion('abc') → 'aababc'	'aababc'	OK	
string_splosion('ab') → 'aab'	'aab'	OK	
string_splosion('x') → 'x'	'x'	OK	
string_splosion('fade') → 'ffafadfade'	'ffafadfade'	OK	
string_splosion('There') → 'TThTheTherThere'	'TThTheTherThere'	OK	
string_splosion('Kitten') → 'KKiKitKittKitteKitten'	'KKiKitKittKitteKitten'	OK	
string_splosion('Bye') → 'BByBye'	'BByBye'	OK	
string_splosion('Good') → 'GGoGooGood'	'GGoGooGood'	OK	
string_splosion('Bad') → 'BBaBad'	'BBaBad'	OK
'''