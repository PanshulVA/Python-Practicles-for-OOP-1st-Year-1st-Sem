def prime_is_true(num):
    if(num<=1):
        return False
    for i in range(2, num): 
        if num % i == 0:
            return False
    return True

def generate_prime():
    primes=[]
    for i in range (2, num+1):
        if prime_is_true(i):
            primes.append(i)
    return primes


def generate_prime_2():
    primes=[]
    num1 = 2
    while len(primes)<num:
        if prime_is_true(num1):
            primes.append(num1)
        num1 +=1
    return primes

num=int(input("Enter the first number: "))

if prime_is_true(num):
    print("The number is a prime")
else:
    print("The number is not a prime")
primes_up_to_num = generate_prime()
print(f"Prime numbers upto {num}: {primes_up_to_num}")

first_n_primes=generate_prime_2()
print(f"First {num} prime numbers: {first_n_primes}")
