def array_count9(nums):
  cnt = 0
  for i in nums:
    if i==9:
      cnt+=1
  
  return cnt



'''
Expected	Run		
array_count9([1, 2, 9]) → 1	1	OK	
array_count9([1, 9, 9]) → 2	2	OK	
array_count9([1, 9, 9, 3, 9]) → 3	3	OK	
array_count9([1, 2, 3]) → 0	0	OK	
array_count9([]) → 0	0	OK	
array_count9([4, 2, 4, 3, 1]) → 0	0	OK	
array_count9([9, 2, 4, 3, 1]) → 1	1	OK
'''