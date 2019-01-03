def checkColumns(sudoku):
    length = len(sudoku)
    for column in range(0, length):
        columnList = []
        for row in sudoku:
            if len(row) >= column + 1:
                columnList.append(row[column])
        for number in columnList:
            if columnList.count(number) > 1:
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


    assert checkColumns(correct) == True

    assert checkColumns(incorrect) == False

    assert checkColumns(incorrect2) == False

    assert checkColumns(incorrect3) == True

    assert checkColumns(incorrect4) == True

    assert checkColumns(incorrect5) == True

    assert checkColumns(irregular) == True

    assert checkColumns(irregular2) == True