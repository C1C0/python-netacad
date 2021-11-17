"""
Exercise 6: 
write a function able to input integer values and to check if they are within a specified range.
The function should:
•	accept three arguments: a prompt, a low acceptable limit, and a high acceptable limit;
•	if the user enters a string that is not an integer value, the function should emit the message Error: wrong input, and ask the user to input the value again;
•	if the user enters a number which falls outside the specified range, the function should emit the message Error: the value is not within permitted range (min..max) and ask the user to input the value again;
•	if the input value is valid, return it as a result.
Test data
Test your code carefully.
This is how the function should react to the user's input:
Enter a number from -10 to 10: 100
Error: the value is not within permitted range (-10..10)
Enter a number from -10 to 10: asd
Error: wrong input
Enter number from -10 to 10: 1
The number is: 1
"""

class OutOfTheRange(Exception):
    pass

def enterNumber(prompt, lowLimit, upLimit) -> None:
    try:
        #get value
        numberInput = int(input(prompt))

        # check for value range
        if(lowLimit > numberInput or numberInput > upLimit):
            raise OutOfTheRange

        print("The number is:", numberInput)

    except ValueError:
        print("Error: wrong input")

    except OutOfTheRange:
        print("Error: the value is not within permitted range ({}..{})".format(lowLimit, upLimit))




enterNumber("Enter a number from -10 to 10:", -10, 10)
