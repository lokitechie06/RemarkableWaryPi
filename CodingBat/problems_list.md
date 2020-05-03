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