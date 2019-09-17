def perfect_number_check(number):
    sum_of_range = 0
    for item in range(1, number):
        if number % item == 0:
            sum_of_range += item
    if sum_of_range == number:
        print("Perfect")
    else:
        print("Not Perfect")


perfect_number_check(int(input("Type Number: ")))
