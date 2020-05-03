def date_fashion(you, date):
  if you >= 8 or date >=8:
    if you <=2 or date <=2 :
      return 0
    return 2
  else:
    if you <=2 or date <=2 :
      return 0
    return 1


# coding bat solution:
def date_fashion(you, date):
  ## Check the <=2 case first, since it takes precedence
  ## over the >=8 case.
  if (you <= 2) or (date <= 2):
    return 0
  elif (you >= 8) or (date >= 8):
    return 2
  else:
    return 1

'''
Test cases:
Expected	Run		
date_fashion(5, 10) → 2	2	OK	
date_fashion(5, 2) → 0	0	OK	
date_fashion(5, 5) → 1	1	OK	
date_fashion(3, 3) → 1	1	OK	
date_fashion(10, 2) → 0	0	OK	
date_fashion(2, 9) → 0	0	OK	
date_fashion(9, 9) → 2	2	OK	
date_fashion(10, 5) → 2	2	OK	
date_fashion(2, 2) → 0	0	OK	
date_fashion(3, 7) → 1	1	OK	
date_fashion(2, 7) → 0	0	OK	
date_fashion(6, 2) → 0	0	OK
'''