# Ask user to enter numbers separated by spaces
numbers = input("Enter numbers separated by spaces: ")

# Convert the input into a list of strings
num_list = numbers.split()

print("Input:", num_list)

# --- a. Using for loop ---
cubes = []
for n in num_list:
    # Check if n is an integer
    if n.isdigit():
        n = int(n)
        # Check if it is even
        if n % 2 == 0:
            cubes.append(n ** 3)
        else: raise ValueError("Number is not even")

print("a. Cubes of even numbers (for loop):", cubes)

# --- b. Using list comprehension ---
cubes_comp = [int(n) ** 3 for n in num_list if n.isdigit() and int(n) % 2 == 0]

print("b. Cubes of even numbers (list comprehension):", cubes_comp)