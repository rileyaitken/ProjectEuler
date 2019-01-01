def reverse_str(string):
    """Returns the reverse of a given string."""
    return string[::-1]

def prob4(n):
    """Find the largest palindrome number that can be produced
    by multiplying two numbers of digits n."""
    largest = float('-inf')
    greatest = int("9" * n)
    smallest = int("1" + "0" * (n - 1))
    for i in range(greatest, smallest, -1):
        for j in range(i - 1, smallest, -1):
            if i * j < largest:
                break
            product = str(i * j)
            if reverse_str(product) == product and i * j > largest:
                largest = i * j
                num1 = i
                num2 = j
        if i * i - 1 < largest:
            break
    return largest, num1, num2

largest, num1, num2 = prob4(3)
print('Largest palindrome as product of two 3 digit numbers: {} with numbers {} {}'.format(largest, num1, num2))
            