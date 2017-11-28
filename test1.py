"""If the index is a multiple of 3 then replace the value at
    that index with "This index was changed"
    """
def switch_index(myList):
    for i in range(len(myList)):
        if i == 0:
            myList[i] = myList[i]
        elif (i%3) == 0:
            myList[i] = "This index was changed"
        else:
            myList[i] = myList[i]
        print(myList[i])

    print("" + "\n")
    print("Now switching by values \n")
    return 0


"""If the value at any given index is a multiple of 3, then
    replace the value with "This value got changed"
    """
def switch_value(myList):
    for i in range(len(myList)):
        if (myList[i] % 3) == 0:
            myList[i] = "This value got changed"
        print(myList[i])

    print("")
    return 0


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [1, 6, 4, 5, 9, 12, 2, 8, 3, 10]
switch_index(list1)
switch_value(list2)
