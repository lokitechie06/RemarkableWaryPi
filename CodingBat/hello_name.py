def hello_name(name):
  return 'Hello '+name+'!'


'''
xpected	Run		
hello_name('Bob') → 'Hello Bob!'	'Hello Bob!'	OK	
hello_name('Alice') → 'Hello Alice!'	'Hello Alice!'	OK	
hello_name('X') → 'Hello X!'	'Hello X!'	OK	
hello_name('Dolly') → 'Hello Dolly!'	'Hello Dolly!'	OK	
hello_name('Alpha') → 'Hello Alpha!'	'Hello Alpha!'	OK	
hello_name('Omega') → 'Hello Omega!'	'Hello Omega!'	OK	
hello_name('Goodbye') → 'Hello Goodbye!'	'Hello Goodbye!'	OK	
hello_name('ho ho ho') → 'Hello ho ho ho!'	'Hello ho ho ho!'	OK	
hello_name('xyz!') → 'Hello xyz!!'	'Hello xyz!!'	OK	
hello_name('Hello') → 'Hello Hello!'	'Hello Hello!'	OK	
other tests OK
'''