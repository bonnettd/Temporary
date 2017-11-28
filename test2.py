"""Gives two methods for printing the elements of a list backwards"""
def print_backwards(myList):
    for i in range(len(myList)-1, -1, -1):
        print(myList[i])

    # second method
    print("The backwards list is " + str(myList[::-1]))
    return 0


"""Print the elements of a list in ascending order"""
def print_ascending(myList):
    ascended_list = sorted(myList, key = int)
    print("The ascending list is " + repr(ascended_list))


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [4, 6, 3, 5, 1, 9, 2]
print_backwards(list1)
print_ascending(list2)
