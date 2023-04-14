# This Code intends to derive a Sub-Array from a given Array, adding the integers of which
# the given Sum could be derived.
# Dated: 14th April 2023
import numpy as np


def find_the_sub_array_from_greater_array(tuple_list, end_integer_list):
    new_empty_list = []

    for i in range(len(end_integer_list)):
        for j in range(len(tuple_list)):
            if end_integer_list[i] == tuple_list[j]:
                new_empty_list.append(j)

    # print("The relevant indexes of the larger array are ", new_empty_list)

    x = new_empty_list[0]
    y = new_empty_list[1]

    sub_array = []

    for k in range(x, y + 1):
        sub_array.append(tuple_list[k])

    print("And the Sum could be derived by adding the integers from the following Sub-array", sub_array)


def do_the_sub_array_operation(emp_list):  # ------> Here we do the operations to derive the Sub-Array

    list_from_tuple = list(tuple_arr1)  # -------> Here tuple is converted to a list for easy operation.
    find_the_sub_array_from_greater_array(list_from_tuple, emp_list)


def check_for_summation_equality(array_s):
    i = 0
    j = 1
    empty_list = []
    empty_array = []

    array_length = len(array_s)
    # print("Attempting from the first Array element, i.e., ", array_s[i])
    empty_list.append(array_s[i])

    while j < array_length:

        summation = array_s[i] + array_s[j]
        if summation == S:
            empty_list.append(array_s[j])
            print("Following are the end integers of the Sub-Array from the left and right", empty_list)
            # catch_the_empty_list(empty_list)
            do_the_sub_array_operation(empty_list)
            exit()
        elif not summation == S:
            array_s[i] = summation
            j = j + 1


# def printing_array(array_y):
#     print(array_y)


def slicing_operation(array_length):
    k = 1

    while array_length >= 2:
        array_x = array1[k:]
        k = k + 1
        array_length = array_length - 1
        check_for_summation_equality(array_x)

    else:
        print("The Sum could not be deduced from the given Array of elements")


# ----------------------------------- Here starts the Code statements -------------------------------------
S = int(input("Please enter the Sum in the form of a two digit integer :"))
print(f"The required sum is {S}")
arr1 = np.array([1, 2, 3, 7, 5])
tuple_arr1 = tuple(arr1)
# print("Tuple of Array is ",tuple_arr1)
array1 = arr1
print("The given Array is ", arr1)
print("-------------------------------------------")

# Do the required operation on the Array
check_for_summation_equality(array1)
arrayLength1 = len(array1)
slicing_operation(arrayLength1)  # ---> We are feeding the arrayLength1 to the function slicing_operation()

# -------------------------Sample Output when 'S = 15' is---------------------------------------
# The required sum is 15
# The given Array is  [1 2 3 7 5]
# -------------------------------------------
# Following are the end integers of the Sub-Array from the left and right [3, 5]
# And the Sum could be derived by adding the integers from the following Sub-array [3, 7, 5]
#
# Process finished with exit code 0
