# Description: Given an array of size N-1 such that it only contains distinct integers in the range of
# 1 to N.
# Find the missing element.
# Dated: 21st April 2023
import numpy as np

N = 8
array1 = np.array([5, 2, 8, 1, 4, 7, 3])
list1 = list(array1)
print(list1)

# Firstly check if N(i.e., 8) is missing in the given array
list1.sort()
length = len(list1)


def find_the_missing_integer():
    # Let's form an array of size 8 with integers from 1 to 8

    empty_array = []

    for i in range(1, 9):
        if i == 0:
            continue
        else:
            empty_array.append(i)

    # print(empty_array)

    length_of_list1 = len(list1)

    for x in range(len(list1)):
        if list1[x] != empty_array[x]:
            print(f"The missing integer is {empty_array[x]}")
            exit()


if N == list1[length - 1]:
    find_the_missing_integer()
else:
    print(f"{N} is the missing integer")
    exit()
