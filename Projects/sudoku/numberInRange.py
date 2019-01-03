def numbersInRange(sudoku):
    for listSudoku in sudoku:
        for element in listSudoku:
            if  element not in range(1, len(listSudoku) + 1):
                return False
    return True


if __name__ == "__main__":

    correct = [[1,2,3],
               [2,3,1],
               [3,1,2]]

    incorrect = [[1,2,3,4],
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


    assert numbersInRange(correct) == True

    assert numbersInRange(incorrect) == True

    assert numbersInRange(incorrect2) == True

    assert numbersInRange(incorrect3) == False
    
    assert numbersInRange(incorrect4) == False

    assert numbersInRange(incorrect5) == False

    assert numbersInRange(irregular) == True

    assert numbersInRange(irregular2) == False

