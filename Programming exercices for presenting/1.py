"""
    Exercise 1. Write the missing code for the following function:
    The function should 
    •	accept exactly one argument - a string;
    •	it should return a list of words created from the string, divided in the places where the string contains whitespaces;
    •	if the string is empty, the function should return an empty list;
    •	its name should be mysplit()
    Code:
    def mysplit(strng):
        #
        # put your code here
        #
    print(mysplit("Toj be or not to be, that is the question"))
    print(mysplit("To be or not to be,that is the question"))
    print(mysplit("   "))
    print(mysplit(" abc "))
    print(mysplit(""))
"""

def mysplit(s : str) -> list:
    word = ""
    listOfSeparatedWords = []

    # strip all whitespaces
    s = s.strip()

    # return empty list if empty string
    if len(s) == 0:
        return list()

    # splitting on whitespace
    for letter in s:

        # when whitespace - assigne to list and continue
        if letter == " ":
            listOfSeparatedWords.append(word)
            word = ""
            continue
        
        word += letter

    listOfSeparatedWords.append(word)
    return listOfSeparatedWords



print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
