from math import sqrt
from itertools import count, islice

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def prob7(n):
    """Find the nth prime number."""
    if n == 1:
        return 2
    
    prime_count = 2
    prime = 3
    
    while prime_count < n:
        number = prime + 2
        while not isPrime(number):
            number += 2
        prime = number
        prime_count += 1
    
    return prime

print(prob7(5))
print(prob7(6))
print(prob7(2))
print(prob7(10001))
        