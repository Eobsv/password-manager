# FileNotFound
# with open("a_file.txt:") as file:
# file.read()

# try:
#     file = open('a_file.txt')
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open('a_file.txt', mode="w")
#     file.write("Something")
# except KeyError as error_message: # for keeping error msg
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("I made it") # It allows me to raise my own exception

# height = float(input("Height: "))
# weight = int(input("Weight: "))
# bmi = weight / height ** 2
#
# print("A situation for raising my own exception")
#
# if height > 3:
#     raise ValueError("Human height should not be over 3meters")


# KeyError
# a_dict = {"key": "Value"}
# value = a_dict{"non_existing_key"}

# IndexError
# fruit_list = ["apple", "banana", "pear"]
# # fruit = fruit_list['non_existing_index']
# def make_pie(index):
#     try:
#        fruit= fruit_list[index]
#     except IndexError:
#         print("Fruit pie")
#     else:
#         print(fruit + " Pie")
# make_pie(2)



# TypeError
# text = "abc"
# print(text + 5)
