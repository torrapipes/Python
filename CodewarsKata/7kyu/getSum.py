# Given two integers a and b, which can be positive or negative,
# find the sum of all the numbers between including them too and return it. If the two numbers are equal return a or b.


def get_sum(a,b):
    sum = 0
    if a > b:
        for number in range (b, a + 1):
            sum = sum + number
        return sum
    else:
        for number in range(a, b + 1):
            sum = sum + number
        return sum

if __name__ == "__main__":

    # test case 1
    assert get_sum(0,1) == 1

    # test case 2
    assert get_sum(0,-1) == -1
