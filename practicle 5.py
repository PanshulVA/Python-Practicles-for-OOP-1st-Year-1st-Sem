string = input("Enter a string: ")
print(f"Original string: {string}")

char_find = input("Enter the character to find frequency: ")
frequency = string.count(char_find)
print(f"a. Frequency of '{char_find}': {frequency}")

char_replace = input("Enter the character to replace: ")
new_char = input("Enter the new character: ")
replace = string.replace(char_replace, new_char)
print(f"b. String after replacing '{char_replace}' with '{new_char}': '{replace}'")

char_remove = input("Enter the character to remove first occurrence: ")
remove = string.replace(char_remove, "", 1)
print(f"c. String after removing first '{char_remove}': '{remove}'")

char_remove_all = input("Enter the character to remove all occurrences: ")
remove_all = string.replace(char_remove_all, "")
print(f"d. String after removing all '{char_remove_all}': '{remove_all}'")
