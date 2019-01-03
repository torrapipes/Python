from checkColumns import checkColumns
from checkRows import checkRows
from isSquare import isSquare
from numberInRange import numbersInRange 

def isCorrect(sudoku, test):

    if checkColumns(sudoku) and isSquare(sudoku) and numbersInRange(sudoku) and checkRows(sudoku):
        print("Sudoku number " + str(test) + " is correct")
    else:
        print("Sudoku number " + str(test) + " is not correct")

if __name__ == '__main__':

    # TEST CASE 1
    correct = [[1,2,3],
               [2,3,1],
               [3,1,2]]

    isCorrect(correct, 1)

    # TEST CASE 2
    incorrect = [[1,2,3,1],
                 [2,3,1,3],
                 [3,1,2,3],
                 [4,4,4,2]]

    isCorrect(incorrect, 2)

    # TEST CASE 3
    incorrect2 = [[1,2,3,4],
                  [2,3,1,2],
                  [4,1,2,3],
                  [2,3,1,4]]

    isCorrect(incorrect2, 3)

    # TEST CASE 4
    incorrect3 = [[1,2,3,4,5],
                  [2,3,1,5,6],
                  [4,5,2,1,3],
                  [3,4,5,2,1],
                  [5,6,4,3,2]]

    isCorrect(incorrect3, 4)

    # TEST CASE 5
    incorrect4 = [['a','b','c'],
                  ['b','c','a'],
                  ['c','a','b']]
    
    isCorrect(incorrect4, 5)

    # TEST CASE 6
    incorrect5 = [[1, 1.5],
                  [1.5, 1]]

    isCorrect(incorrect5, 6)

    # TEST CASE 7
    irregular = [[1,2,3],
                 [2,3,1]]

    isCorrect(irregular, 7)

    # TEST CASE 8
    irregular2 = [[1,2,3],
                  [2,3,1],
                  [3,1]]
    
    isCorrect(irregular2, 8)