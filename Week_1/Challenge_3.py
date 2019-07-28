def number_factorial(first_number):
    factorial = first_number - 1
    while factorial > 0:
        first_number *= factorial
        factorial -= 1
    return first_number


print(number_factorial(int(input("enter number here: "))))
