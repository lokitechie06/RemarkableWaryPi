def sorta_sum(a, b):
  tot = a + b
  if tot >= 10 and tot <=19:
    return 20
  else:
    return tot


'''
Test case
Expected	Run		
sorta_sum(3, 4) → 7	7	OK	
sorta_sum(9, 4) → 20	20	OK	
sorta_sum(10, 11) → 21	21	OK	
sorta_sum(12, -3) → 9	9	OK	
sorta_sum(-3, 12) → 9	9	OK	
sorta_sum(4, 5) → 9	9	OK	
sorta_sum(4, 6) → 20	20	OK	
sorta_sum(14, 7) → 21	21	OK	
sorta_sum(14, 6) → 20	20	OK
'''