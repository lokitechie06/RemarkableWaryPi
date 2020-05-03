def max_end3(nums):
  if nums[0] >= nums[-1]:
    return [nums[0], nums[0], nums[0]]
  else:
    return [nums[-1], nums[-1], nums[-1]]


# coding bat solution:
def max_end3(nums):
  big = max(nums[0], nums[2])
  nums[0] = big
  nums[1] = big
  nums[2] = big
  return nums

'''
Expected	Run		
max_end3([1, 2, 3]) → [3, 3, 3]	[3, 3, 3]	OK	
max_end3([11, 5, 9]) → [11, 11, 11]	[11, 11, 11]	OK	
max_end3([2, 11, 3]) → [3, 3, 3]	[3, 3, 3]	OK	
max_end3([11, 3, 3]) → [11, 11, 11]	[11, 11, 11]	OK	
max_end3([3, 11, 11]) → [11, 11, 11]	[11, 11, 11]	OK	
max_end3([2, 2, 2]) → [2, 2, 2]	[2, 2, 2]	OK	
max_end3([2, 11, 2]) → [2, 2, 2]	[2, 2, 2]	OK	
max_end3([0, 0, 1]) → [1, 1, 1]	[1, 1, 1]	OK
'''