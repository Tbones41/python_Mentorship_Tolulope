def sum_odd(a, b):
    output = 0
    while 0 < a < b < 10000:
        for number in range(a, (b+1)):
            if number % 2 == 1:
                output += number
        return output
    else:
        if a > b:
            return "Number A should not be greater than Number B"
        elif a or b < 0:
            return "Number A or B should be a positive integer"
        elif a or b > 10000:
            return "Number A or B should not be greater than 10,000"
        else:
            return "Error in input. Please check"


print(sum_odd(int(input("Input Number A: ")), int(input("Input Number B: "))))
