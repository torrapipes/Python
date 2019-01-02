# In this kata I have to create a function that takes in a list and returns a list with the reverse order.


def reverseListOrder(list):
    return list.reverse()



if __name__ == "__main__":

    # test case 1
    assert reverseListOrder(["tail", "body", "head"]) == ["head","body","tail"]

    # test case 2
    assert reverseListOrder(["bot", "mid", "top"]) == ["top","mid","bot"]


# Solution 2:

# def reverseListOrder(list):
    # temp = lista[0]
    # lista[0] = lista[2]
    # lista[2] = temp
   

# Solution 3:

# def reverseListOrder(list):
    # return list[::-1]


# Solution 4:

# def reverseListOrder(list):
  # newList=[]
  # newList.append(list[2])
  # newList.append(list[1])
  # newList.append(list[0])
  # return newList
