# List of problems # 

## Warmup-1

1. sleep_in: **sleep_in.py**

''' The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in '''


2. monkey_trouble: **monkey_trouble.py**

''' We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble. '''


3. sum_double: **sum_double.py**

''' Given two int values, return their sum. Unless the two values are the same, then return double their sum. '''


4. diff21: **diff21.py**

''' Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21. '''


5. parrot_trouble: **parrot_trouble.py**

''' We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble. '''


6. makes10: **makes10.py**

''' 
Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10. '''


7. near_hundred: **near_hundred.py**

''' 
Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number. '''


8. pos_neg: **pos_neg.py**

''' 
Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative. '''


9. not_string: **not_string.py**

'''
Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged. '''


10. missing_char: **missing_char.py**

''' Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive). '''


11. front_back: __front_back.py__

''' Given a string, return a new string where the first and last chars have been exchanged. '''


12. front3: __front3.py__

''' Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front. '''


## String-1

13. hello_name: __hello_name.py__

''' Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".'''


14. make_abba: __make_abba.py__

''' Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi". '''


15. make_tags: __make_tags.py__

''' The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. In this example, the "i" tag makes <i> and </i> which surround the word "Yay". Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>". '''


16. make_out_word: __make_out_word.py__

''' Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>". '''


17. extra_end: __extra_end.py__

''' Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2. '''


18. first_two: __first_two.py__

''' Given a string, return the string made of its first two chars, so the String "Hello" yields "He". If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "". '''


19. first_half: __first_half.py__

''' Given a string of even length, return the first half. So the string "WooHoo" yields "Woo". '''


20. without_end: __without_end.py__

''' Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2. '''


21. combo_string: __combo_string.py__

''' Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty (length 0). '''


22. non_start: __non_start.py__

''' Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1. '''


23. left2: __left2.py__

''' Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2. '''


## Logic-1

24. cigar_party: __cigar_party.py__

''' When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise. '''


25. date_fashion: __date_fashion.py__

''' You and your date are trying to get a table at a restaurant. The parameter "you" is the stylishness of your clothes, in the range 0..10, and "date" is the stylishness of your date's clothes. The result getting the table is encoded as an int value with 0=no, 1=maybe, 2=yes. If either of you is very stylish, 8 or more, then the result is 2 (yes). With the exception that if either of you has style of 2 or less, then the result is 0 (no). Otherwise the result is 1 (maybe). '''


26. squirrel_play: __squirrel_play.py__

''' The squirrels in Palo Alto spend most of the day playing. In particular, they play if the temperature is between 60 and 90 (inclusive). Unless it is summer, then the upper limit is 100 instead of 90. Given an int temperature and a boolean is_summer, return True if the squirrels play and False otherwise. '''


27. caught_speeding: __caught_speeding.py__

''' You are driving a little too fast, and a police officer stops you. Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, your speed can be 5 higher in all cases. '''


28. sorta_sum: __sorta_sum.py__

''' Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20. '''


29. alarm_clock: __alarm_clock.py__

'''  Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation, return a string of the form "7:00" indicating when the alarm clock should ring. Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00". Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off". '''


30. love6: __love6.py__

''' The number 6 is a truly great number. Given two int values, a and b, return True if either one is 6. Or if their sum or difference is 6. Note: the function abs(num) computes the absolute value of a number. '''


31. in1to10: __in1to10.py__

''' Given a number n, return True if n is in the range 1..10, inclusive. Unless outside_mode is True, in which case return True if the number is less or equal to 1, or greater or equal to 10. '''


32. near_ten: __near_ten.py__

''' Given a non-negative number "num", return True if num is within 2 of a multiple of 10. Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2. '''


## list-1

33. first_last6: __first_last6.py__

''' Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more. '''


34. same_first_last: __same_first_last.py__

''' Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal. '''


35. make_pi: __make_pi.py__

''' Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}. '''


36. common_end: __common_end.py__

''' Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more. '''


37. sum3: __sum3.py__

''' Given an array of ints length 3, return the sum of all the elements. '''


38. rotate_left3: __rotate_left3.py__

''' Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}. '''


39. reverse3: __reverse3.py__

''' Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}. '''


40. max_end3: __max_end3.py__

''' Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the other elements to be that value. Return the changed array. '''


41. sum2: __sum2.py__

''' Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0. '''


42. middle_way: __middle_way.py__

''' Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements. '''


43. make_ends: __make_ends.py__

''' Given an array of ints, return a new array length 2 containing the first and last elements from the original array. The original array will be length 1 or more. '''


44. has23: __has23.py__

''' Given an int array length 2, return True if it contains a 2 or a 3. '''


## Warmup-2

45. string_times: __string_times.py__

''' Given a string and a non-negative int n, return a larger string that is n copies of the original string. '''


46. front_times: __front_times.py__

''' Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front; '''


47. string_bits: __string_bits.py__

''' Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo". '''


48. string_splosion: __string_splosion.py__

''' Given a non-empty string like "Code" return a string like "CCoCodCode". '''


49. last2: __last2.py__

''' Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring). '''


50. array_count9: __array_count9.py__

''' Given an array of ints, return the number of 9's in the array. '''


51. array_front9: __array_front9.py__

''' Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4. '''


52. array123: __array123.py__

''' Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere. '''


53. string_match: __string_match.py__

''' Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings. '''


## String-2

54. double_char: __double_char.py__

''' Given a string, return a string where for every char in the original, there are two chars. '''


55. count_hi: __count_hi.py__

''' Return the number of times that the string "hi" appears anywhere in the given string. '''