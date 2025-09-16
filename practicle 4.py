char= input("Enter a character: ")
char = char[0]

if char.isalpha():
    print(f"{char} is a letter")
    if char.isupper():
        print(f"{char} is an uppercase letter")
    else:
        print(f"{char} is a lowercase letter")
elif char.isdigit():
    dig_name ={'0':'Zero',
               '1':"One",
               '2':"Two",
               '3':"Three",
               '4':"Four",
               '5':"Five",
               '6':"Six",
               '7':"Seven",
               '8':"Eight",
               '9':"Nine"
               }
    print(f"{char} is a numeric digit: {dig_name.get(char)}")
else:
    print(f"{char} is a special character")