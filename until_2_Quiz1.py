def prime_factors(n):
    factors = []
    factor = 2
    while n > 1:
        if n % factor == 0:
            factors.append(factor)
            n = n // factor
        else:
            factor += 1
    return factors
 
numbers = [18, 39, 63, 126, 792]

for number in numbers:
    result = prime_factors(number)
    print(f"Prime factors of {number} = {result}")
