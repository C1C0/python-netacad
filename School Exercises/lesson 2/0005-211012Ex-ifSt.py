txt = "I want to learn python!"
findingText = "learn"

if findingText in txt:
    print("Yes, {} is present.".format(findingText))

# cocatonation
a = "Hello"
b = "World"

c = a + b
print(c)

c = a + ' ' + b
print(c)