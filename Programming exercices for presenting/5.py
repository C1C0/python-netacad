"""
Exercise 5:
Your task is to write a program which:
•	asks the user her/his birthday (in the format YYYYMMDD, or YYYYDDMM, or MMDDYYYY - actually, the order of the digits doesn't matter)
•	outputs the Digit of Life for the date.
Where the Digit of Life is a digit evaluated using somebody's birthday. It's simple - you just need to sum all the digits of the date. If the result contains more than one digit, you have to repeat the addition until you get exactly one digit. For example:
•	1 January 2017 = 2017 01 01
•	2 + 0 + 1 + 7 + 0 + 1 + 0 + 1 = 12
•	1 + 2 = 3
3 is the digit we searched for and found.

Test your code using the data we've provided.
Test data
Sample input:
19991229
Sample output:
6
"""


r = 0
y = int(input("text"))
x = [int(a) for a in str(y)]
for q in range(0,len(x)):
    r = r + x[q]
o = [int(a) for a in str(r)]
p = o[0] + o[1]
print(p)