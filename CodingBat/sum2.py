def sum2(nums):
  if len(nums) > 2:
    return sum(nums[0:2])
  elif len(nums) <= 2:
    return sum(nums)
  elif len(nums)==0:
    return 0



'''
Expected	Run		
sum2([1, 2, 3]) → 3	3	OK	
sum2([1, 1]) → 2	2	OK	
sum2([1, 1, 1, 1]) → 2	2	OK	
sum2([1, 2]) → 3	3	OK	
sum2([1]) → 1	1	OK	
sum2([]) → 0	0	OK	
sum2([4, 5, 6]) → 9	9	OK	
sum2([4]) → 4	4	OK	
'''