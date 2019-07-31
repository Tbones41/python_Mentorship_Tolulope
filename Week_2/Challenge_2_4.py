def even_or_odd(num):
    if int(num) % 2 == 0:
        return "This number is an EVEN number"
    elif int(num) % 2 == 1:
        return "This number is an ODD number"
    else:
        return "This is not a valid number"


print(even_or_odd(input("Type a number here: ")))
