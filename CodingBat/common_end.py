def common_end(a, b):
  return a[0]==b[0] or a[-1]==b[-1]


'''
Expected	Run		
common_end([1, 2, 3], [7, 3]) → True	True	OK	
common_end([1, 2, 3], [7, 3, 2]) → False	False	OK	
common_end([1, 2, 3], [1, 3]) → True	True	OK	
common_end([1, 2, 3], [1]) → True	True	OK	
common_end([1, 2, 3], [2]) → False	False	OK
'''