def make_tags(tag, word):
  return '<'+tag+'>'+word+'</'+tag+'>'

'''
Expected	Run		
make_tags('i', 'Yay') → '<i>Yay</i>'	'<i>Yay</i>'	OK	
make_tags('i', 'Hello') → '<i>Hello</i>'	'<i>Hello</i>'	OK	
make_tags('cite', 'Yay') → '<cite>Yay</cite>'	'<cite>Yay</cite>'	OK	
make_tags('address', 'here') → '<address>here</address>'	'<address>here</address>'	OK	
make_tags('body', 'Heart') → '<body>Heart</body>'	'<body>Heart</body>'	OK	
make_tags('i', 'i') → '<i>i</i>'	'<i>i</i>'	OK	
make_tags('i', '') → '<i></i>'	'<i></i>'	OK	
other tests OK
'''