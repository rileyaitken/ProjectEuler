def prob6(n):
    """Finds absolute difference between sum of squares of first n natural numbers,
    and the square of the sum of the same numbers."""
    sum_squares = 0
    natural_sum = 0 
    for i in range(1, n + 1):
        sum_squares += i * i
        natural_sum += i
    square_sum = natural_sum * natural_sum 
    return abs(square_sum - sum_squares)

print(prob6(100))