# 1. Use input() function to complete the following code to ask for user's name.
#Type your answer here.
my_name = input("What's your name: ")
print("Hello!, " +my_name )

# 2. What will the variable var be equal to? And why?
var = 100
var = 200 + 300
# because 200 + 300 = 500 which overwrites former value of variable "var"
var= 500

# 3. Use input() to get a string (hint: this should be a number) and print it as an integer.
print(int(input("Put Number: ")))

# 4. Complete the code to create a converter that converts miles to kms?
# Type your answer here.
Distance = float(input("Put the number of miles to convert into kms?"))
result= Distance * 1.609344
print("Kms:", result)

# 5. Define two variables as arguments using input() and print their sum.
x = int(input("First Variable: "))
y = int(input("Second Variables: "))
print(x + y)

# 6. Use input() to get value for minutes and convert it to seconds.
seconds = int(input("Minutes: ")) * 60

# 7. Concatenate a string "name" with string "Python" and print the result.
print("name" + "Python")

# 8. Use input() function to get value for Danish kroner (DKK) and convert it to American dollars (USD)
dkk = float(input("DKK: "))
usd = dkk * 0.15537

# What is the output of the following snippet?
"""
x = 5
y = 7
z = x
b = y
y = z
t = b
x = t
print(x,y)
"""
# Answer: the output is : 7 5


#10. Input two strings, first_name and last_name. Print a single string in the format "last, first".
first_name = input("First name: ")
last_name = input("Last name: ")

print(last_name, first_name)

# #Additional 
# 1. Write a code that prints True when num1 is equal to num2; otherwise print False.
num1 = 2
num2 = 2
print("True" if num1 == num2 else "False")

# 2. Write a code that prints True if an integer is divisible by 5, and False otherwise.
print("True" if num1 % 5 == 0 else "False")