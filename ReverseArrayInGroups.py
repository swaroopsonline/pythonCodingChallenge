# Given an array arr[] of positive integers of size N. Reverse every sub-array group of size K.
# Note: If at any instance, there are no more subarrays of size greater than or equal to K, then reverse the
# last subarray (irrespective of its size). You shouldn't return any array, modify the given array in-place.
import numpy as np


def append_the_remaining_integers_in_reverse_order(sub_array):
    length_subarray = len(sub_array)
    # print(f"length of Sub_array is {length_subarray}")
    x = length_subarray - 1
    while not x < 0:
        empty_list.append(sub_array[x])
        # print(empty_list)
        x = x - 1

    else:
        print(f"Reversed every sub-array group of size {K} is {empty_list}")
        exit()


def check_for_the_length_of_extracted_array(extracted_array):
    # print(extracted_array)
    if len(extracted_array) >= K:
        extract_and_reverse_the_subarray(extracted_array)
    elif len(extracted_array) < K:
        append_the_remaining_integers_in_reverse_order(extracted_array)


def extract_and_reverse_the_subarray(list_array):
    global K
    j = K - 1
    while not j < 0:
        empty_list.append(list_array[j])
        list_array.remove(list_array[j])
        j = j - 1

    # print(empty_list)
    # print(list_array)
    check_for_the_length_of_extracted_array(list_array)


# ----------------------------Actual statements start here -------------------------------------

N = 5
K = 3

empty_list = []
array1 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
list_array1 = list(array1)
print(f"The given Array is {list_array1}")

extract_and_reverse_the_subarray(list_array1)

# -------------------------------------------Sample Output-----------------------------------------
# /usr/bin/python3.10 /home/swaroop/PycharmProjects/pythonCodingChallenge/ReverseArrayInGroups.py
# The given Array is [1, 2, 3, 4, 5, 6, 7, 8]
# Reversed every sub-array group of size 3 is [3, 2, 1, 6, 5, 4, 8, 7]
#
# Process finished with exit code 0

