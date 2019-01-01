from math import sqrt
from itertools import count, islice

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def prob3(n):
    """Find the prime factors of number n."""
    factors = {}
    if n % 2 == 0:
        factors[2] = 0
        while n % 2 == 0:
            n / 2
            factors[2] += 1
    
    i = 3
    while i <= sqrt(n):
        if n % i == 0:
            factors[i] = 0
            while n % i == 0:
                n /= i
                factors[i] += 1
        else:
            i += 2
    
    if n > 1:
        factors[n] = 1
        
    return factors

factors = prob3(600851475143)
print(type(factors))
result_string = "Prime factorisation of n = " + str(600851475143) + "is as follows" 
for key, value in factors.items():
    result_string += ", {} to the power of {}".format(key, value)
print(result_string)
        