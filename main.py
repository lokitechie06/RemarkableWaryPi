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

def first_two(str):
  if len(str)>2:
    return str[0:2]
  elif len(str)<=2:
    return str
  else:
    return ''

print(first_two('Hello'))
print(first_two('ab'))
print(first_two(''))