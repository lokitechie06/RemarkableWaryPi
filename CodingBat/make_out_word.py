def make_out_word(out, word):
  return out[0:2]+word+out[2:5]

'''
Expected	Run		
make_out_word('<<>>', 'Yay') → '<<Yay>>'	'<<Yay>>'	OK	
make_out_word('<<>>', 'WooHoo') → '<<WooHoo>>'	'<<WooHoo>>'	OK	
make_out_word('[[]]', 'word') → '[[word]]'	'[[word]]'	OK	
make_out_word('HHoo', 'Hello') → 'HHHellooo'	'HHHellooo'	OK	
make_out_word('abyz', 'YAY') → 'abYAYyz'	'abYAYyz'	OK	
other tests OK
'''