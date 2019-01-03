def checkRows(sudoku):
    for list in sudoku:
        position = 0
        variation = 0
        while variation < len(list) - 1:
            if list[position] == list[variation + 1]:
                return False
            else:
                variation = variation + 1
        position = position + 1
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


    assert checkRows(correct) == True

    assert checkRows(incorrect) == False

    assert checkRows(incorrect2) == True

    assert checkRows(incorrect3) == True

    assert checkRows(incorrect4) == True

    assert checkRows(incorrect5) == True

    assert checkRows(irregular) == True

    assert checkRows(irregular2) == True
