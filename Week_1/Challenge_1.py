def first_reverse(sentence):
    split_sentence = sentence.split(" ")
    output_list = []
    for item in split_sentence:
        output_list.append(item)
    output_list.reverse()
    output = ""
    for each_word in output_list:
        output += each_word + " "
    return output


print(first_reverse(input("Type your sentence here to be reversed!! \n>> ")))
