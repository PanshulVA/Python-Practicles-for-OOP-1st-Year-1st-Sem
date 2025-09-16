num=int(input("Enter the number: "))

def create_cubes_dic():
    cubes_dic={i: i**3 for i in range(num+1)}
    print(f"Dictionary of cubes for keys 1 to 5:\n", cubes_dic )
    
create_cubes_dic()