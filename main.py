"""
1. odd_positions_1.py 
Write a function that returns the elements on odd positions (0 based) in a list

2. cumm_sum_list_2.py
Write a function that returns the cumulative sum of elements in a list

3. output_list_digits_3.py
Write a function that takes a number and returns a list of its digits
"""

"""
Write a function that takes a number and returns a list of its digits
"""
def solution(input):
  output = []
  # convert to string 
  inputStr = str(input)
  for x in inputStr:
    # convert back to integer
    output.append(int(x))
  return output

assert solution(123) == [1,2,3]
assert solution(400) == [4,0,0]


print(solution(123))
print(solution(400))