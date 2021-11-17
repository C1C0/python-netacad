"""

  # ### ### # # ### ### ### ### ### ### 
  #   #   # # # #   #     # # # # # # # 
  # ### ### ### ### ###   # ### ### # # 
  # #     #   #   # # #   # # #   # # # 
  # ### ###   # ### ###   # ### ### ###

"""


def transformNumber(number : int) -> str:
  """
  Transforms number to seven-segment display form 
  """
  segments = {
    0:"""
###
# #
# #
# #
###""",
    1:"""
  #
  #
  #
  #
  #""",
    2:"""
###
  #
###
#  
###""",
    3:"""
###
  #
# #
  #
###""",
    4:"""
# #
# #
###
  #
  #""",
    5:"""
###
#  
###
  #
###""",
    6:"""
###
#  
###
# #
###""",
    7:"""
###
  #
  #
  #
  #""",
    8:"""
###
# #
###
# #
###""",
    9:"""
###
# #
###
  #
  #"""
}

  finalNumber = ''
  numberOfRows = 5
  # reason of 4: each char: ***\n
  charsInSegmentRow = 4

  # We print numbers by row
  for row in range(numberOfRows):
      # prints specified line of number
      for x in number:

          # if char is space, just provide space
          if x == ' ':
            finalNumber += ' '
            continue
        
          beginSubstr = 0 + (charsInSegmentRow * row)
          endSubstr = beginSubstr + charsInSegmentRow

          finalNumber += segments[int(x)][beginSubstr:endSubstr].replace("\n", '') + " "

      finalNumber += " \n"

  return finalNumber

def checkIfNumericWithSpace(number: str) -> bool:
  for char in number:
    # check if char is space
    if char == ' ':
      continue

    # if not space, then check if number
    if not char.isnumeric():
      return False

  return True

def printAndEnd(message: str) -> None:
    print(message)
    exit()


########################

number = input().strip()

if not checkIfNumericWithSpace(number):
    printAndEnd("Provided String does not consist only of numbers and spaces")

print(transformNumber(number))