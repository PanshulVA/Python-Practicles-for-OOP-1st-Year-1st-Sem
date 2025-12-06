rows = int(input("Enter the number of rows: "))

print("The pyramid")
for i in range(rows):
    print(" " * (rows - i -1), end="")
    print("*" * (2*i+1))
print()
print()
print("The reverse pyramid")
for i in range(rows -1, -1, -1):
    print(" " * (rows - i -1), end="")
    print("*" * (2*i+1))