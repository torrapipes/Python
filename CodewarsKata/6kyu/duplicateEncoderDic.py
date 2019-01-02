# The goal of this exercise is to convert a string to a new string where each character
# in the new string is '(' if that character appears only once in the original string, or ')' 
# if that character appears more than once in the original string. 

def duplicateEncoderDic(word):
    upperWord = word.upper()
    result = ""
    dictionary = {}
    for letter in upperWord:
        if letter in dictionary:
            dictionary[letter] = ")"
        else:
            dictionary[letter] = "("


    for letter in upperWord:
        result = result + dictionary[letter]
    
    return result


if __name__ == "__main__":

    # test case 1 
    assert duplicateEncoderDic("din") == "((("

    # test case 2
    assert duplicateEncoderDic("recede") == "()()()"
    
    # test case 3
    assert duplicateEncoderDic("Success") == ")())())"
    
    # test case 4
    assert duplicateEncoderDic("(( @") == "))(("