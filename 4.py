# Task : Check for Prime Number

def prime_check(num):
    if num <= 1:
        return False  # 0 and 1 are not prime numbers

    for i in range(2, num):
        if num % i == 0:
            return False  # Found a divisor, so not prime

    return True  # No divisors found, so it's prime


print(prime_check(int(input())))