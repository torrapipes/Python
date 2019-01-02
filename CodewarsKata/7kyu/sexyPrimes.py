# Sexy primes are pairs of two primes that are 6 apart. 
# In this kata, your job is to complete the function sexy_prime(x, y) which returns true if x & y are sexy,
# false otherwise.

def isPrime(number):
    divisor = 2
    while divisor < number and number % divisor != 0:
            divisor = divisor + 1
    if divisor == number:
        return True
    else:
        return False


def sexy_prime(x, y):
    if (x - y == 6 or x - y == -6) and isPrime(x) and isPrime(y):
        return True
    else:
        return False


if __name__ == "__main__":

    # test case 1
    assert sexy_prime(5, 11) == True

    # test case 2
    assert sexy_prime(13, 19) == True

    # test case 3
    assert sexy_prime(83, 89) == True

    # test case 4
    assert sexy_prime(1, 11) == False
