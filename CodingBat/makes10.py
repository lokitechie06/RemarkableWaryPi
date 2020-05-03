def makes10(a, b):
  if a==10 or b==10 or a+b==10:
    return True
  else:
    return False

'''
Test cases
Expected	Run		
makes10(9, 10) → True	True	OK	
makes10(9, 9) → False	False	OK	
makes10(1, 9) → True	True	OK	
makes10(10, 1) → True	True	OK	
makes10(10, 10) → True	True	OK	
makes10(8, 2) → True	True	OK	
makes10(8, 3) → False	False	OK	
makes10(10, 42) → True	True	OK	
makes10(12, -2) → True	True	OK
'''