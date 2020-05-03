def cigar_party(cigars, is_weekend):
  if is_weekend==True:
    if cigars >= 40:
      return True
  else:
    if cigars >= 40 and cigars <= 60:
      return True
  return False


# coding bat solution
def cigar_party(cigars, is_weekend):
  if is_weekend:
    return (cigars >= 40)
  else:
    return (cigars >= 40 and cigars <= 60)

'''
Test cases:
Expected	Run		
cigar_party(30, False) → False	False	OK	
cigar_party(50, False) → True	True	OK	
cigar_party(70, True) → True	True	OK	
cigar_party(30, True) → False	False	OK	
cigar_party(50, True) → True	True	OK	
cigar_party(60, False) → True	True	OK	
cigar_party(61, False) → False	False	OK	
cigar_party(40, False) → True	True	OK	
cigar_party(39, False) → False	False	OK	
cigar_party(40, True) → True	True	OK	
cigar_party(39, True) → False	False	OK
'''