## if you have an array of numbers, make a function to
# move all the zeros to the end of the list, while
# keeping the numbers postion in the original order
## End of the Quest.
list_of_strawberry = [2, 0, 9, 0, 0, 3, 5, 0, 6, 7, 0, 1, 100]


def sort_the_number(theZeros):  # (store the 0'rs)
    for findZero in theZeros:  # check for 0'rs
        if 0 in theZeros:  # catch the 0'rs
            theZeros.remove(0)
            theZeros.append(0)
    return theZeros


print(sort_the_number(list_of_strawberry))
