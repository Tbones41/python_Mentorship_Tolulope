def time_convert(num):
    hours = int(num) // 60
    mins = int(num) % 60
    output = f'{hours}:{mins}'
    return output


time_convert(input("Type the time in minutes >>> "))