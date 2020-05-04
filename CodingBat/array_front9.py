def array_front9(nums):
  
  # array length can be less than 4
  # so 1. figure out the end
  end = len(nums)
  if end > 4:
    end = 4
    
  for i in range(end):
    if nums[i]==9:
      return True
  return False


  '''
  Expected	Run		
array_front9([1, 2, 9, 3, 4]) → True	True	OK	
array_front9([1, 2, 3, 4, 9]) → False	False	OK	
array_front9([1, 2, 3, 4, 5]) → False	False	OK	
array_front9([9, 2, 3]) → True	True	OK	
array_front9([1, 9, 9]) → True	True	OK	
array_front9([1, 2, 3]) → False	False	OK	
array_front9([1, 9]) → True	True	OK	
array_front9([5, 5]) → False	False	OK	
array_front9([2]) → False	False	OK	
array_front9([9]) → True	True	OK	
array_front9([]) → False	False	OK	
array_front9([3, 9, 2, 3, 3]) → True	True	OK	
  '''