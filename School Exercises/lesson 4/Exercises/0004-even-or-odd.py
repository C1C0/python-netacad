def is_number_even(number):
    return number % 2 == 0

test_data = [20, 60, 80, 87]
test_results = [True, True, True, False]
for i in range(len(test_data)):
    nr = test_data[i]
    print(nr, "->", end="")
    result = is_number_even(nr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
