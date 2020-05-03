def near_ten(num):
  if num%10 <= 2 or num%10 >=8:
    return True
  else:
    return False


'''
Test cases
Expected	Run		
near_ten(12) → True	True	OK	
near_ten(17) → False	False	OK	
near_ten(19) → True	True	OK	
near_ten(31) → True	True	OK	
near_ten(6) → False	False	OK	
near_ten(10) → True	True	OK	
near_ten(11) → True	True	OK	
near_ten(21) → True	True	OK	
near_ten(22) → True	True	OK	
near_ten(23) → False	False	OK	
near_ten(54) → False	False	OK	
near_ten(155) → False	False	OK	
near_ten(158) → True	True	OK	
near_ten(3) → False	False	OK	
near_ten(1) → True	True	OK
'''