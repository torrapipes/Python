# Get the number n (n>0) to return the reversed sequence from n to 1.
# Example reverse_seq(5) -> [5,4,3,2,1]
# Example reverse_seq(20)-> [20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]

def reverse_seq(number):
    total = []
    for num in range(1, number + 1):
        total = total+[num]
    total.reverse()
    return total


if __name__ == "__main__":

    # test case 1
    assert reverse_seq(5) == [5,4,3,2,1]

    # test case 2
    assert reverse_seq(20) == [20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]



# Solution 2:

# def reverse_seq(number):
    # total = []
    # for num in range(1,number + 1):
        # total = total+[num]
    # return total[::-1]


# Solution 3:

# def reverse_seq(number):
    # newList = []
    # for num in range(1,number + 1):
        # newList.append(num)
    # return(newList[::-1])
