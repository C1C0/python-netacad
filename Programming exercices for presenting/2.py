"""
Exercise 2: 
The original Caesar cipher shifts each character by one: a becomes b, z becomes a, and so on. Let's make it a bit harder, and allow the shifted value to come from the range 1..25 inclusive. Moreover, let the code preserve the letters' case (lower-case letters will remain lower-case) and all non-alphabetical characters should remain untouched.
Your task is to write a program which:
•	asks the user for one line of text to encrypt;
•	asks the user for a shift value (an integer number from the range 1..25 - note: you should force the user to enter a valid shift value (don't give up and don't let bad data fool you!)
•	prints out the encoded text.
Test your code using the data we've provided.
Test data
Sample input:  
abcxyzABCxyz 123
2
Sample output:
cdezabCDEzab 123

"""

def shift(s: str, shift: int) -> str:
    newS = ""

    bottomLimit, upperLimit = 'a', 'z'
    bottomLimitCode, upperLimitCode = ord(bottomLimit), ord(upperLimit)

    # go through every char in string
    for letter in s:
        letterCode = ord(letter)

        # evaluate another letter, if this one is out of range
        if bottomLimitCode > letterCode or letterCode > upperLimitCode:
            newS += letter
            continue
        
        newCode = ord(letter) + shift
        
        # start from bottom limit if we pass upper limit
        if(newCode > upperLimitCode):
            newS += chr(newCode - 1 - upperLimitCode + bottomLimitCode)
        else:
            newS += chr(newCode)

    return newS

# user input
userString = input()

print(shift(userString, 1))