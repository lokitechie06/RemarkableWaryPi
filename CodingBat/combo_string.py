def combo_string(a, b):
  if len(a) < len(b):
    return a+b+a
  else:
    return b+a+b


'''
Expected	Run		
combo_string('Hello', 'hi') → 'hiHellohi'	'hiHellohi'	OK	
combo_string('hi', 'Hello') → 'hiHellohi'	'hiHellohi'	OK	
combo_string('aaa', 'b') → 'baaab'	'baaab'	OK	
combo_string('b', 'aaa') → 'baaab'	'baaab'	OK	
combo_string('aaa', '') → 'aaa'	'aaa'	OK	
combo_string('', 'bb') → 'bb'	'bb'	OK	
combo_string('aaa', '1234') → 'aaa1234aaa'	'aaa1234aaa'	OK	
combo_string('aaa', 'bb') → 'bbaaabb'	'bbaaabb'	OK	
combo_string('a', 'bb') → 'abba'	'abba'	OK	
combo_string('bb', 'a') → 'abba'	'abba'	OK	
combo_string('xyz', 'ab') → 'abxyzab'	'abxyzab'	OK
'''