def make_ends(nums):
  return [nums[0], nums[-1]]


'''
Expected	Run		
make_ends([1, 2, 3]) → [1, 3]	[1, 3]	OK	
make_ends([1, 2, 3, 4]) → [1, 4]	[1, 4]	OK	
make_ends([7, 4, 6, 2]) → [7, 2]	[7, 2]	OK	
make_ends([1, 2, 2, 2, 2, 2, 2, 3]) → [1, 3]	[1, 3]	OK	
make_ends([7, 4]) → [7, 4]	[7, 4]	OK	
make_ends([7]) → [7, 7]	[7, 7]	OK	
make_ends([5, 2, 9]) → [5, 9]	[5, 9]	OK	
make_ends([2, 3, 4, 1]) → [2, 1]	[2, 1]	OK
'''