# Given: Two positive integers a < b <10000
# Return: The sum of all odd integers from a through b inclusively. (Solve using
# for loops

a = int(input("Input Number 1: "))
b = int(input("Input Number 2: "))


def sum_odd_for(a, b):
    output = 0
    if 0 < a < b < 10000:
        for number in range(a, (b + 1)):
            if number % 2 == 1:
                output += number
        return output
    elif a > b:
        return "Number A should not be greater than Number B"
    elif a < 0:
        return "Number A should be a positive integer"
    elif b > 10000:
        return "Number A or B should not be greater than 10,000"


# Given: Two positive integers a < b <10000
# Return: The sum of all odd integers from a through b inclusively. (Solve using
# while loops


def sum_odd_while(a, b):
    result = 0
    b += 1
    while 0 < a < b < 10000:
        if 1 == 1:
            number = a
            if number % 2 == 1:
                result += number
            a += 1
        return result


print(f'For Loop = {sum_odd_for(a, b)}')
print(f'While Loop = {sum_odd_while(a, b)}')

