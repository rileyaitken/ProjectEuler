from math import gcd

def euclids_gcd(number, divisor):
    """Finds the greatest common divisor of two numbers using Euclid's algorithm."""
    while number > divisor:
        number -= divisor
    if number == 0:
        return divisor
    else:
        return euclids_gcd(divisor, number)

def find_lcm(a, b):
    """Finds the lowest common multiple of two numbers."""
    gcd_value = gcd(a, b)
    lcm = int((a * b) / gcd_value)
    return lcm

def prob5(n):
    """Returns the smallest possible number evenly divisible by all numbers
    from 1 to n."""
    lcm = find_lcm(n, n - 1)
    for i in range(n - 2, 0, -1):
        lcm = find_lcm(lcm, i)
    return lcm

lcm = prob5(20)
for i in range(1, 21):
    if lcm % i != 0:
        print("Bad result.")
print(lcm)

    