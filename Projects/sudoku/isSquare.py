def isSquare(sudoku):
    for list in sudoku:
        if len(list) != len(sudoku):
            return False
    return True

if __name__ == '__main__':

    correct = [[1,2,3],
               [2,3,1],
               [3,1,2]]
    incorrect = [[1,2,3,1],
                 [2,3,1,3],
                 [3,1,2,3],
                 [4,4,4,2]]

    incorrect2 = [[1,2,3,4],
                  [2,3,1,2],
                  [4,1,2,3],
                  [2,3,1,4]]

    incorrect3 = [[1,2,3,4,5],
                  [2,3,1,5,6],
                  [4,5,2,1,3],
                  [3,4,5,2,1],
                  [5,6,4,3,2]]

    incorrect4 = [['a','b','c'],
                  ['b','c','a'],
                  ['c','a','b']]

    incorrect5 = [[1, 1.5],
                  [1.5, 1]]

    irregular = [[1,2,3],
                 [2,3,1]]

    irregular2 = [[1,2,3],
                  [2,3,1],
                  [3,1]]


    assert isSquare(correct) == True

    assert isSquare(incorrect) == True

    assert isSquare(incorrect2) == True

    assert isSquare(incorrect3) == True

    assert isSquare(incorrect4) == True

    assert isSquare(incorrect5) == True

    assert isSquare(irregular) == False

    assert isSquare(irregular2) == False
