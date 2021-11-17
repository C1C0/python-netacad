def checkIfIncludesWord(word: dict, sequence: str)->bool:
    """
    Check if sequence of letters includes also sub-sequence
    of letters from word in the same order 
    """
    wordIndex = 0
    wordLength = len(word)

    for char in sequence:
        if wordIndex == wordLength:
            return True

        if char == word[wordIndex]:
            wordIndex += 1

    return wordIndex == wordLength

print("Yes" if checkIfIncludesWord(input(), input()) else "No") 