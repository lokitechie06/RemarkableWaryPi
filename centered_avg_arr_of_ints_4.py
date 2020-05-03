"""
From: http://codingbat.com/prob/p126968
Return the "centered" average of an array of ints, which we'll say is 
the mean average of the values, except ignoring the largest and 
smallest values in the array. If there are multiple copies of the 
smallest value, ignore just one copy, and likewise for the largest 
value. Use int division to produce the final average. You may assume 
that the array is length 3 or more.
"""

# how do we get average?
# sum of all elements/ no of elements 
# to get centered average - exclude min and mix of array 
# min - to get the smallest element in the list
# max - to get the largest element in the list
# sum - sum of all elements in the list 
# exclude min(input) and max(output) from sum(output)
# and do len(input)-2 to get true size of input 

def solution(input):
  #smallest = min(input)
  #largest = max(input)
  # remember to do -2 on length of elements as well
  output = (sum(input)-min(input)-max(input))/(len(input)-2)
  return round(output)

print(solution([1, 2, 3, 4, 100]))
print(solution([1, 1, 5, 5, 10, 8, 7]))
print(solution([-10, -4, -2, -4, -2, 0]))

assert solution([1, 2, 3, 4, 100]) == 3
assert solution([1, 1, 5, 5, 10, 8, 7]) == 5
assert solution([-10, -4, -2, -4, -2, 0]) == -3