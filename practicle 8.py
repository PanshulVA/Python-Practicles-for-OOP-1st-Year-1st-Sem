input_list = eval(input("Enter a list: "))
print(f"Input list:{input_list}")

cubes=[]
for item in input_list:
    if isinstance(item, int) and item % 2 == 0:
        cubes.append(item ** 3)
print(f"a. Cubes of even integers (using for loop): {cubes}")

cubes_comp=[item ** 3 for item in input_list if isinstance(item, int) and item % 2 ==0]
print(f"b. Cubes of even integers (using list comprehension): {cubes_comp}")
