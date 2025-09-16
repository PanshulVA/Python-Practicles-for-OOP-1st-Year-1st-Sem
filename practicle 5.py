string="practicles are the best way to learn programming"
print(f"Original string {string}")

char_find='p'
frequency=string.count(char_find)
print(f"a. Frequency of '{char_find}': {frequency}")

char_replace='p'
new_char="P"
replace=string.replace(char_replace, new_char)
print(f"b. String after replacing '{char_replace}' with '{new_char}': '{replace}'")


char_remove='m'
remove=string.replace(char_remove, "", 1)
print(f"c. String after removing first '{char_remove}': '{remove}'")

char_remove_all='a'
remove_all=string.replace(char_remove_all, "")
print(f"c. String after removing all '{char_remove_all}': '{remove_all}'")
