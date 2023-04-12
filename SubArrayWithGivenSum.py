# This Code aims to slice a given Array until it's length is not less than two
# Note: The slicing would be done on the very first element of the initial Array and thereafter on every array
# that will be formed on each iteration.
# Dated: 11th April 2023
import numpy as np


def check_for_summation_equality(array_s):
    i = 0
    j = 1
    empty_list = []

    array_length = len(array_s)
    # print("Attempting from the first Array element, i.e., ", array_s[i])
    empty_list.append(array_s[i])

    while j < array_length:

        summation = array_s[i] + array_s[j]
        if summation == S:
            # print("Summation ends with the last Array element, i.e., ", array_s[j])
            empty_list.append(array_s[j])
            print("Following are the end integers from left to the right", empty_list)
            exit()
        elif not summation == S:
            # empty_list.clear()
            array_s[i] = summation
            j = j + 1


def printing_array(array_y):
    print(array_y)


def slicing_operation(array_length):
    k = 1

    while array_length >= 2:
        array_x = arr1[k:]
        k = k + 1
        array_length = array_length - 1
        check_for_summation_equality(array_x)


# ----------------------------------- Here starts the Code statements -------------------------------------
S = 12
print(f"The required sum is {S}")
arr1 = np.array([1, 2, 3, 7, 5])
array1 = arr1
print("The given Array is ", array1)
print("-------------------------------------------")
# Do the required operation on the Array

check_for_summation_equality(array1)
arrayLength1 = len(array1)

slicing_operation(arrayLength1)  # ---> We are feeding the arrayLength1 to the function slicing_operation()

# -------------------------Sample Output when 'S = 12' is---------------------------------------
# The required sum is 12
# The given Array is  [1 2 3 7 5]
# -------------------------------------------
# Following are the end integers from left to the right [2, 7]

