def even_fibonaccis(term1 = 1, term2 = 2, sum_fibs = 0):
    if term2 % 2 == 0:
        sum_fibs += term2
    new_term = term1 + term2
    if new_term > 4000000:
        return sum_fibs
    return even_fibonaccis(term2, new_term, sum_fibs)
    
print(even_fibonaccis())
    
    