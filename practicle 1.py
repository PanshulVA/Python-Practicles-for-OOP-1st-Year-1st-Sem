import cmath

a=float(input("Enter the coefficient a: "))
b=float(input("Enter the coefficient b: "))
c=float(input("Enter the coefficient c: "))

dis=(b**2) - (4*a*c)

if a == 0:
    print("This is not a quadratic equation because 'a' cannot be zero.")
else:
    
    if dis>0:
        root1= (-b - dis**0.5) / (2*a)
        root2= (-b + dis**0.5) / (2*a)
        print("The roots of the eqn are:", root1,"&",root2)

    elif dis==0:
        root3= -b/ (2*a)

        print("The roots of the eqn are:", root3)

    else:   
        root4 = (-b - cmath.sqrt(dis)) / (2*a)
        root5 = (-b + cmath.sqrt(dis)) / (2*a)
        print("The roots are complex:", root4,"&",root5)
    