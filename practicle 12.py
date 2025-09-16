t1=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(f"The original tuple is:, {t1}\n")

half_tuple=len(t1)//2
print("Halves of tuple is")
print(t1[:half_tuple])
print(t1[half_tuple:])

even_numbers= tuple(num for num in t1 if num %2==0)
print("/n The even numbers in the tupleare:")
print(even_numbers)


t2=(11, 12, 13)
concatenated= t1+t2
print(f"\n Concatenated tuple of {t1} & {t2} is \n{concatenated}")


max_tuple=max(concatenated)
min_tuple=min(concatenated)

print(f"The maximum value of tuple is: {max_tuple} \n& The minmum value of tuple is: {min_tuple}")