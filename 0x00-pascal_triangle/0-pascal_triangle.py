#!/usr/bin/python3
"""Module with one function pascal_triangle"""


def pascal_triangle(n):
    """Function to print the pascal triangle"""
    if n <= 0:
        return []
    myarray = []
    i = 0
    while i < n:
        if i == 0:
            myarray.append([1])
        elif i == 1:
            myarray.append([1, 1])
        else:
            sublist = []
            for index in range(i + 1):  # add values to the sub list
                if index == 0 or index == i:
                    sublist.append(1)
                else:
                    sublist.append(myarray[i-1][index] + myarray[i-1][index - 1])
            myarray.append(sublist)  # add the sublist to the main array
        i += 1

    return myarray