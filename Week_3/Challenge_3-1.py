def friends(entered_names):
    split_names = entered_names.split(" ")
    new_names = []
    for names in split_names:
        if len(names) == 4:
            new_names.append(names)
    return new_names


print(friends(input("Type the list of names here separated by a space only \n>> ")))
