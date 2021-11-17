"""
Palindrome is a word which look the same when read forward and backward. For example, "kayak" is a palindrome, while "loyal" is not.
Your task is to write a program which:
•	asks the user for some text;
•	checks whether the entered text is a palindrome, and prints result.
Note:
•	assume that an empty string isn't a palindrome;
•	treat upper- and lower-case letters as equal;
•	spaces are not taken into account during the check - treat them as non-existent;
•	there are more than a few correct solutions - try to find more than one.
Test your code using the data we've provided.
"""

def palindrome(x):
    return x == x[::-1]


o = input("your text")
x = o.replace(" ","").lower()
y = palindrome(x)

if (o == ""):
    print("It's not a palindrome")
elif y:
    print("It's a palindrome")
else:
    print("It's not a palindrome")