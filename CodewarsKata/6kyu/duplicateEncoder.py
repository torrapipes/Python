# The goal of this exercise is to convert a string to a new string where each character
# in the new string is '(' if that character appears only once in the original string, or ')' 
# if that character appears more than once in the original string. 

def duplicateEncoder(word):
    word = word.upper()
    result = ""
    for letter in word:
        if word.count(letter) > 1:
            result = result + ")"
        else:
            result = result + "(" 
    return result

if __name__ == "__main__":

    # test case 1 
    assert duplicateEncoder("din") == "((("

    # test case 2
    assert duplicateEncoder("recede") == "()()()"
    
    # test case 3
    assert duplicateEncoder("Success") == ")())())"
    
    # test case 4
    assert duplicateEncoder("(( @") == "))(("
    


