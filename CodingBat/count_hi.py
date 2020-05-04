def count_hi(str):
  cnt = 0
  for i in range(len(str)-1):
    if str[i]=='h' and str[i+1]=='i':
      cnt += 1
  
  return cnt

# coding bat solution:
def count_hi(str):
  sum = 0
  ## Loop to length-1 and access index i and i+1
  ## in the loop.
  for i in range(len(str)-1):
    if str[i:i+2] == 'hi':
      sum = sum + 1
  return sum

'''
Expected	Run		
count_hi('abc hi ho') → 1	1	OK	
count_hi('ABChi hi') → 2	2	OK	
count_hi('hihi') → 2	2	OK	
count_hi('hiHIhi') → 2	2	OK	
count_hi('') → 0	0	OK	
count_hi('h') → 0	0	OK	
count_hi('hi') → 1	1	OK	
count_hi('Hi is no HI on ahI') → 0	0	OK	
count_hi('hiho not HOHIhi') → 2	2	OK	
'''