"""Prerequisites
4.3.1.15

Objectives
improve the student's skills in operating with files (reading/writing)
using lambdas to change the sort order.
Scenario
The previous code needs to be improved. It's okay, but it has to be better.

Your task is to make some amendments, which generate the following results:

the output histogram will be sorted based on the characters' frequency (the bigger counter should be presented first)
the histogram should be sent to a file with the same name as the input one, but with the suffix '.hist' (it should be concatenated to the original name)
Assuming that the input file contains just one line filled with:

cBabAa
samplefile.txt

the expected output should look as follows:

a -> 3
b -> 2
c -> 1
output

Tip: Use a lambda to change the sort order."""

from io import TextIOWrapper


def histogram(file : TextIOWrapper, filenameOutput:str="", close:bool = False) -> dict:
    """Goes thorugh each character in TextIOWrapper file object and returns dict histogram

    Args:
        file (TextIOWrapper): text file
        close (bool, optional): Specifies if TextIOWrapper object should be closed. Defaults to False.

    Returns:
        dict: Dictionary of histogram
    """
    histogramCount = dict()
    notCountedChars = ("\n", " ")
    
    # go through each character
    for char in file.read():
        char = char.lower()
        
        if char in notCountedChars or not char.isalpha():
            continue
        
        if char in histogramCount.keys():
            histogramCount[char] += 1
        else:
            histogramCount[char] = 1
            
    # sort the histogram
    histogramCount = dict(sorted(histogramCount.items(), key=(lambda item: item[1]), reverse=True))
        
    # close if specified
    if close: file.close()
    
    if fileName != "": outputHistogramToFile(histogramToString(histogramCount), fileName)
    
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

def outputHistogramToFile(histogramStr, fileName:str, filePath='C:\\Users\\kpsko\\Documents\\School\\1sem\\Python\\Course Exercise\\streams\\') -> None:
    # modify filename
    fileName: list = fileName.split('.')
    fileName.insert(-1, 'hist')
    fileName:str = '.'.join(fileName)
    
    newFile = open(filePath + fileName, "w")
    newFile.write(histogramStr)
    newFile.close()
    

try:
    fileName = input("Enter the file to analyze: ")
    stream = open('C:\\Users\\kpsko\\Documents\\School\\1sem\\Python\\Course Exercise\\streams\\'+fileName, 'r')
    print(histogramToString(histogram(stream, fileName, True)))
except OSError:
    print("File probably doesn't exist")