def prime_is_true(num):
    if num <= 1:
        return False
    # Only check up to sqrt(num)
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def generate_prime(n):
    "Return all primes up to n"
    primes = []
    for i in range(2, n + 1):
        if prime_is_true(i):
            primes.append(i)
    return primes


def generate_prime_2(n):
    "Return the first n prime numbers"""
    primes = []
    candidate = 2
    while len(primes) < n:
        if prime_is_true(candidate):
            primes.append(candidate)
        candidate += 1
    return primes


num = int(input("Enter the number: "))

# Check if num is prime
if prime_is_true(num):
    print("The number is a prime")
else:
    print("The number is not a prime")

# All primes up to num
primes_up_to_num = generate_prime(num)
print(f"Prime numbers up to {num}: {primes_up_to_num}")

# First num primes
first_n_primes = generate_prime_2(num)
print(f"First {num} prime numbers: {first_n_primes}")
