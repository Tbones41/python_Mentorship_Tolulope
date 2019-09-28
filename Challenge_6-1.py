MAD_LIBS = open("demotext.txt", 'r+')

mad_libs_dict = {
            "NOUN": "",
            "VERB": "",
            "ADJECTIVE": "",
            "ADVERB": ""
    }


def mad_libs_function():

    result = ""
    for line in MAD_LIBS:
        split_line = line.split(" ")
        for word in split_line:
            if word in mad_libs_dict:
                print(result)
                mad_libs_dict[word] = input(f"Enter {word} here>> ")
                result += (mad_libs_dict.get(word) + " ")
            else:
                result += (word + " ")
    return MAD_LIBS.write(result)


mad_libs_function()
MAD_LIBS.close()


#    FAILED TESTS
#        |  |
#        |  |
#        |  |
#      __|__|__
#      \      /
#       \    /
#         \/

# def mad_func():
#     # noinspection SpellCheckingInspection
#     mad_libs = open('demotext.txt', "r")
#     mad_libs_dict = {
#         "NOUN": input("Insert a Noun here >> "),
#         "VERB": input("Insert a Verb here >> "),
#         "ADJECTIVE": input("Insert an Adjective here >> "),
#         "ADVERB": input("Insert an Adverb here >> ")
#     }
#
#     for x in mad_libs:
#         result = ""
#         string_split = x.split(" ")
#         for word in string_split:
#             if word in mad_libs_dict:
#                 word_new = mad_libs_dict.get(word)
#                 result += (word_new + " ")
#             else:
#                 result += word + " "
#         print(result)
# print(mad_func())
