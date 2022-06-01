def primes(param):
    factors = list()
    divisor = 2
    while divisor <= param:
        if param % divisor == 0:
            factors.append(divisor)
            param = param // divisor
        else:
            divisor += 1
    print(factors)
