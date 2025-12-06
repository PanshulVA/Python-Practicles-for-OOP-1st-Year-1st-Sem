string1=(input("Enter the first string: "))
string2=(input("Enter the second string: "))
num= int(input("Enter the number of characters to swap: "))

if num>len(string1) or num>len(string2):
    print("Error: number is larger than the string itself")
else:
    new_1 = string2[:num] + string1[num:]
    new_2 = string1[:num] + string2[num:]
    
print(f"The original string was {string1} & {string2}")
print(f"Strings after swapping {num} characters are {new_1} & {new_2}")    
