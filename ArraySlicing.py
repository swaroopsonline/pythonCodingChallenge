# This Code aims to slice a given Array until it's length is not less than two
# Note: The slicing would be done on the very first element of the initial Array and thereafter on every array
# that will be formed on each iteration.
# Dated: 11th April 2023
import numpy as np


def printing_array(array_y):
    print(array_y)


def slicing_operation(array_length):
    k = 1

    while array_length > 2:
        array_x = arr1[k:]
        k = k + 1
        array_length = array_length - 1
        printing_array(array_x)


arr1 = np.array([1, 2, 3, 7, 5])
array1 = arr1
printing_array(array1)
# Do the required operation on the Array
arrayLength1 = len(array1)

slicing_operation(arrayLength1)  # ---> We are feeding the arrayLength1 to the function slicing_operation()
