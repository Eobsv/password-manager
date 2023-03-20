# FileNotFound
# with open("a_file.txt:") as file:
# file.read()
try:
    file = open('a_file.txt')
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open('a_file.txt', mode="w")
    file.write("Something")
except KeyError as error_message: # for keeping error msg
    print(f"The key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")

# KeyError
# a_dict = {"key": "Value"}
# value = a_dict{"non_existing_key"}

# IndexError
# fruit_list = ["apple", "banana", "pear"]
# fruit = fruit_list['non_existing_index']

# TypeError
# text = "abc"
# print(text + 5)
