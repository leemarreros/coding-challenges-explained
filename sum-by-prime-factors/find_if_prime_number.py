def is_prime(n):
    # when n is 1 or less than 1:
    if n <= 1:
        return False

    # range(2, n) will iterate until n - 1
    for div in range(2, n):
        # if the modulus of n % div is 0, it means that
        # n is divisible by a given div, which makes it not a prime number
        if n % div == 0:
            return False

    # True if n was not divisible for the range between 2 to n - 1
    return True
