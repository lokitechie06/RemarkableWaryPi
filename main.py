"""
1. odd_positions_1.py 
Write a function that returns the elements on odd positions (0 based) in a list

2. cumm_sum_list_2.py
Write a function that returns the cumulative sum of elements in a list

"""

"""
Write a function that returns the cumulative sum of elements in a list
"""
def solution(input):
  output = []
  sum = 0
  for x in input:
    sum += x
    output.append(sum)
  return output

assert solution([1,1,1]) == [1,2,3]
assert solution([1,-1,3]) == [1,0,3]

print(solution([1,1,1]))
print(solution([1,-1,3]))