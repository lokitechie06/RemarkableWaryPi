"""
Write a function that returns the elements on odd positions (0 based) in a list
"""
def solution(input):
    output = input[1::2]
    return output

assert solution([0,1,2,3,4,5]) == [1,3,5]
assert solution([1,-1,2,-2]) == [-1,-2]

input_list = [0,1,2,3,4,5]
print(solution(input_list))

input_list_2 = [1,-1,2,-2]
print(solution(input_list_2))