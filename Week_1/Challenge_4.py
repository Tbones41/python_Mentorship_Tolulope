def check_nums(num1, num2):
    if num2 > num1:
        return "True"
    elif num2 == num1:
        return "-1"
    else:
        return "False"


check_nums(float(input("Input Number 1: ")), float(input("Input Number 2: ")))
