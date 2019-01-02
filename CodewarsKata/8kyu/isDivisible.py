# Create a function isDivisible(n, x, y) that checks if a number n is divisible by two numbers x AND y.
# All inputs are positive, non-zero digits.

def isDivisible(n, x, y):
    if n % x == 0 and n % y == 0:
        return True
    else: 
        return False


if __name__ == "__main__":

    # test case 1
    assert isDivisible(3,3,4) == False

    # test case 2
    assert isDivisible(12,3,4) == True

    # test case 3
    assert isDivisible(8,3,4) == False

    # test case 4
    assert isDivisible(48,3,4) == True