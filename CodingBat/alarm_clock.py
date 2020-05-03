def alarm_clock(day, vacation):
  if vacation==False:
    if day >=1 and day <=5:
      return "7:00"
    elif day==0 or day==6:
      return "10:00"
  else:
    if day >=1 and day <=5:
      return "10:00"
    elif day==0 or day==6:
      return "off"

'''
Test cases:
Expected	Run		
alarm_clock(1, False) → '7:00'	'7:00'	OK	
alarm_clock(5, False) → '7:00'	'7:00'	OK	
alarm_clock(0, False) → '10:00'	'10:00'	OK	
alarm_clock(6, False) → '10:00'	'10:00'	OK	
alarm_clock(0, True) → 'off'	'off'	OK	
alarm_clock(6, True) → 'off'	'off'	OK	
alarm_clock(1, True) → '10:00'	'10:00'	OK	
alarm_clock(3, True) → '10:00'	'10:00'	OK	
alarm_clock(5, True) → '10:00'	'10:00'	OK	
'''