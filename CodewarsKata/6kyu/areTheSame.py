# Given two arrays a and b write a function comp(a, b) (compSame(a, b) in Clojure)
# that checks whether the two arrays have the "same" elements, with the same multiplicities.
# "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.

def comp(array1,array2):
    for number in array1:
        if number ** 2 in array2:
            if array1.count(number) > 1:
                if array2.count(number ** 2) == 2:
                    return True
                else:
                    return False
            else:
                continue
        else:
            return False        
        

if __name__ == '__main__':
    
    # test case 1
    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
    assert comp(a1, a2) == True