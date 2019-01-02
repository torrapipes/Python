# Write function alternateCase which switch every letter in string from upper to lower and from lower to upper.
# E.g: Hello World -> hELLO wORLD


def alternateCase(word):
    return word.swapcase()


if __name__ == "__main__":

    # test case 1
    assert alternateCase("hello world") == "HELLO WORLD"

    # test case 2
    assert alternateCase("HELLO WORLD") == "hello world"

    # test case 3
    assert alternateCase("hello WORLD") == "HELLO world"

    # test case 4
    assert alternateCase("HeLLo WoRLD") == "hEllO wOrld"
    
    # test case 5
    assert alternateCase("1a2b3c4d5e") == "1A2B3C4D5E"
    

    #Solution 2:
    
    # def upper_lower(nombre):
        # for letra in nombre:
            # if letra == letra.uppercase():
                # letra.lowercase()
            # else:
                # letra.uppercase()