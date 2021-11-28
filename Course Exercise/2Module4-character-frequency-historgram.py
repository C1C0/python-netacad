"""Scenario
A text file contains some text (nothing unusual) but we need to know how often (or how rare) each letter appears in the text. 
Such an analysis may be useful in cryptography, so we want to be able to do that in reference to the Latin alphabet.

Your task is to write a program which:

asks the user for the input file's name;
reads the file (if possible) and counts all the Latin letters (lower- and upper-case letters are treated as equal)
prints a simple histogram in alphabetical order (only non-zero counts should be presented)
Create a test file for the code, and check if your histogram contains valid results.

Assuming that the test file contains just one line filled with:

aBc
samplefile.txt

the expected output should look as follows:

a -> 1
b -> 1
c -> 1
output

Tip: We think that a dictionary is a perfect data collection medium for storing the counts. The letters may be keys while the counters can be values."""

from io import TextIOWrapper


def histogram(file : TextIOWrapper, close:bool = False) -> dict:
    """Goes thorugh each character in TextIOWrapper file object and returns dict histogram

    Args:
        file (TextIOWrapper): text file
        close (bool, optional): Specifies if TextIOWrapper object should be closed. Defaults to False.

    Returns:
        dict: Dictionary of histogram
    """
    histogramCount = dict()
    notCountedChars = ("\n")
    
    # go through each character
    for char in file.read():
        char = char.lower()
        
        if char in notCountedChars or not char.isalpha():
            continue
        
        if char in histogramCount.keys():
            histogramCount[char] += 1
        else:
            histogramCount[char] = 1
        
    # close if specified
    if close: file.close()
    
    return histogramCount

def histogramToString(histogram: dict) -> str:
    """Creates histogram string

    Args:
        histogram (dict):

    Returns:
        str
    """
    output = ""
    
    for key in histogram.keys():
        output += "{key} -> {value}\n".format(key=key, value=histogram[key])

    return output

try:
    fileName = input("Enter the file to analyze: ")
    stream = open('C:\\Users\\kpsko\\Documents\\School\\1sem\\Python\\Course Exercise\\streams\\'+fileName, 'r')
    print(histogramToString(histogram(stream, True)))
except OSError:
    print("File probably doesn't exist")