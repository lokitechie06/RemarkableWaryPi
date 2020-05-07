"""
1. odd_positions_1.py 
Write a function that returns the elements on odd positions (0 based) in a list

2. cumm_sum_list_2.py
Write a function that returns the cumulative sum of elements in a list

3. output_list_digits_3.py
Write a function that takes a number and returns a list of its digits

4. centered_avg_arr_of_ints_4.py
From: http://codingbat.com/prob/p126968
Return the "centered" average of an array of ints, which we'll say is 
the mean average of the values, except ignoring the largest and 
smallest values in the array. If there are multiple copies of the 
smallest value, ignore just one copy, and likewise for the largest 
value. Use int division to produce the final average. You may assume 
that the array is length 3 or more.


"""

def odd_positions(input):
  output = input[1::2]
  return output

assert odd_positions([0,1,2,3,4,5,6]) == [1,3,5]
assert odd_positions([0,-1,2,-2])==[-1,-2]

print(odd_positions([0,1,2,3,4,5,6]))
print(odd_positions([0,-1,2,-2]))



def cumm_sum_list(input):
  output = []
  sum = 0
  for i in input:
    sum += i
    output.append(sum)
  return output


assert cumm_sum_list([1,1,1]) == [1,2,3]
assert cumm_sum_list([1,-1,3]) == [1,0,3]

print(cumm_sum_list([1,1,1]))
print(cumm_sum_list([1,-1,3]))



def output_list_digits(input):
  output = []
  inputStr = str(input)
  for ch in inputStr:
    output.append(int(ch))
  return output

assert output_list_digits(100) == [1,0,0]
assert output_list_digits(400) == [4,0,0]

print(output_list_digits(100))
print(output_list_digits(400))



def centered_avg_arr_of_ints(input):
  return round((sum(input)-max(input)-min(input))/(len(input)-2));


assert centered_avg_arr_of_ints([1, 2, 3, 4, 100]) == 3
assert centered_avg_arr_of_ints([1, 1, 5, 5, 10, 8, 7]) == 5
assert centered_avg_arr_of_ints([-10, -4, -2, -4, -2, 0]) == -3



print(centered_avg_arr_of_ints([1, 2, 3, 4, 100]))
print(centered_avg_arr_of_ints([1, 1, 5, 5, 10, 8, 7]))
print(centered_avg_arr_of_ints([-10, -4, -2, -4, -2, 0]))