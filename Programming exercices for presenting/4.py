"""
Exercise 4:
An anagram is a new word formed by rearranging the letters of a word, using all the original letters exactly once. For example, the phrases "rail safety" and "fairy tales" are anagrams, while "I am" and "You are" are not.
Your task is to write a program which:
•	asks the user for two separate texts;
•	checks whether, the entered texts are anagrams and prints the result.
Note:
•	assume that two empty strings are not anagrams;
•	treat upper- and lower-case letters as equal;
•	spaces are not taken into account during the check - treat them as non-existent
Test your code using the data we've provided.
Test data
Sample input:
Listen
Silent

Sample output:
Anagrams
"""

def areAnagram(str1, str2):
    # first check lenght
    n1 = len(str1)
    n2 = len(str2)
    if n1 != n2:
        return

    # we sort them
    str1 = sorted(str1.lower())
    str2 = sorted(str2.lower())

    # We check position of each letter
    for i in range(0, n1):
        if str1[i] != str2[i]:
            return False

    return True


str1 = input("1. string: ")
str2 = input("2. string: ")

if areAnagram(str1, str2):
    print("The two strings are anagram of each other")
else:
    print("The two strings are not anagram of each other") 