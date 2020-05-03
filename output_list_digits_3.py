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