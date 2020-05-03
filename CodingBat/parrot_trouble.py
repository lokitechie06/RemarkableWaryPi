def parrot_trouble(talking, hour):
  if talking==True and (hour < 7 or hour > 20):
    return True
  else:
    return False

'''
Test cases
Expected	Run		
parrot_trouble(True, 6) → True	True	OK	
parrot_trouble(True, 7) → False	False	OK	
parrot_trouble(False, 6) → False	False	OK	
parrot_trouble(True, 21) → True	True	OK	
parrot_trouble(False, 21) → False	False	OK	
parrot_trouble(False, 20) → False	False	OK	
parrot_trouble(True, 23) → True	True	OK	
parrot_trouble(False, 23) → False	False	OK	
parrot_trouble(True, 20) → False	False	OK	
parrot_trouble(False, 12) → False	False	OK	
'''