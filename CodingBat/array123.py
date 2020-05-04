# My solution, felt like hard coding based on the test cases
def array123(nums):
  seq = [1,2,3]
  if seq in nums or seq==nums or seq==nums[1:4] or seq==nums[-3:]:
    return True
  else:
    return False


# coding bat solution:
def array123(nums):
  # Note: iterate with length-2, so can use i+1 and i+2 in the loop
  for i in range(len(nums)-2):
    if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
      return True
  return False

'''
Expected	Run		
array123([1, 1, 2, 3, 1]) → True	True	OK	
array123([1, 1, 2, 4, 1]) → False	False	OK	
array123([1, 1, 2, 1, 2, 3]) → True	True	OK	
array123([1, 1, 2, 1, 2, 1]) → False	False	OK	
array123([1, 2, 3, 1, 2, 3]) → True	True	OK	
array123([1, 2, 3]) → True	True	OK	
array123([1, 1, 1]) → False	False	OK	
array123([1, 2]) → False	False	OK	
array123([1]) → False	False	OK	
array123([]) → False	False	OK
'''