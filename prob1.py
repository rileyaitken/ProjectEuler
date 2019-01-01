def sumMultiples3And5(n):
    """Finds the sum of all multiples of 3 and 5 below given number n."""
    sum = 0
    for i in range(3, n, 3):
        sum += i
        print(i)
    for i in range(5, n, 5):
        if i % 3 == 0 and i % 5 == 0:
            continue
        sum += i
        print(i)
    return sum

print(sumMultiples3And5(1000))