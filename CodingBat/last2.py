def last2(str):
  
  if len(str) < 2:
    return 0
  
  # get the end substring
  end2 = str[-2:]
  count = 0
  
  for i in range(len(str)-2):
    sub = str[i:i+2]
    if sub == end2:
      count += 1
  
  return count



'''
Expected	Run		
last2('hixxhi') → 1	1	OK	
last2('xaxxaxaxx') → 1	1	OK	
last2('axxxaaxx') → 2	2	OK	
last2('xxaxxaxxaxx') → 3	3	OK	
last2('xaxaxaxx') → 0	0	OK	
last2('xxxx') → 2	2	OK	
last2('13121312') → 1	1	OK	
last2('11212') → 1	1	OK	
last2('13121311') → 0	0	OK	
last2('1717171') → 2	2	OK	
last2('hi') → 0	0	OK	
last2('h') → 0	0	OK	
last2('') → 0	0	OK	
'''