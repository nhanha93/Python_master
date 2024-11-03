# sent = input("Enter a sentence: ")
# print(sent.upper())
# num_of_words = input("Enter a paragraph: ")
# print(len(num_of_words))
# digit_check = input("Enter a string: ")
# print(digit_check.isdigit())
# a_to_o = input("Enter another string to replace 'a' with 'o': ")
# print(a_to_o.replace("a","o"))
def initials(name):
    name_parts = name.split()
    initials = [part[0].upper() for part in name_parts]
    return initials

full_name = input("Enter first and last name: ")
print("Your initials are: ", initials(full_name))

    

