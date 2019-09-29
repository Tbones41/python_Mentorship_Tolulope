def upper_or_lower_count(string):
    count_upper = 0
    count_lower = 0
    for letter in string:
        if letter == " ":
            count_upper += 0
        elif letter == letter.upper():
            count_upper += 1
        else:
            count_lower += 1
    print(f"Number of Uppercase letters is {count_upper} and Number of Lowercase letters is {count_lower}")


upper_or_lower_count(input("Enter your sentence here: "))
