def in1to10(n, outside_mode):
  if outside_mode:
    if n <= 1 or n >=10:
      return True
    else:
      return False
  else:
    if n in range(1, 11):
      return True
    else:
      return False


'''
Test cases:
Expected	Run		
in1to10(5, False) → True	True	OK	
in1to10(11, False) → False	False	OK	
in1to10(11, True) → True	True	OK	
in1to10(10, False) → True	True	OK	
in1to10(10, True) → True	True	OK	
in1to10(9, False) → True	True	OK	
in1to10(9, True) → False	False	OK	
in1to10(1, False) → True	True	OK	
in1to10(1, True) → True	True	OK	
in1to10(0, False) → False	False	OK	
in1to10(0, True) → True	True	OK	
in1to10(-1, False) → False	False	OK	
in1to10(-1, True) → True	True	OK	
in1to10(99, False) → False	False	OK	
in1to10(-99, True) → True	True	OK
'''