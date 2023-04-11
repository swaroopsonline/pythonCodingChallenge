# This Code aims to slice a given Array until it's length is not less than two
# Note: The slicing would be done on the very first element of the initial Array and thereafter on every array
# that will be formed on each iteration.
# Dated: 11th April 2023
import numpy as np


def printing_result_array(array_s):
    print("The resulting Sub-Array is ", array_s)


def check_for_summation_equality(array_s):
    i = 0
    j = 1
    summation = 0
    array_length = len(array_s)
    print("Attempting from the first Array element, i.e., ", array_s[i])
    while j < array_length:
        summation = array_s[i] + array_s[j]
        if summation == S:
            printing_result_array(array_s)
            print("Summation ends with the last Array element, i.e., ", array_s[j])
            break
        elif not summation == S:
            # print("The given sum could not be deduced from the given array of elements")
            array1[i] = summation
            j = j + 1


def printing_array(array_y):
    print(array_y)


def slicing_operation(array_length):
    k = 1

    while array_length > 2:
        array_x = arr1[k:]
        k = k + 1
        array_length = array_length - 1
        # printing_array(array_x)
        # Do the required operation on the Array
        check_for_summation_equality(array_x)


# ----------------------------------- Here starts the Code statements -------------------------------------
S = 5
print(f"The required sum is {S}")
arr1 = np.array([1, 2, 3, 7, 5])
array1 = arr1
print("The given Array is ",array1)
# Do the required operation on the Array
check_for_summation_equality(array1)
arrayLength1 = len(array1)

slicing_operation(arrayLength1)  # ---> We are feeding the arrayLength1 to the function slicing_operation()
