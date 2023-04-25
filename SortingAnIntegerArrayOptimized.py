# -------------------- This is an Optimized Code to sort an unsorted Integer Array.---------------------------
# Dated: 25th April 2023
import numpy as np


def print_the_sorted_array(new_array):
    # print(f"The last array is {new_array}")
    last_int = new_array[0]
    sorted_array.append(last_int)
    print("The sorted Array is shown below")
    print(sorted_array)


def forming_the_sorted_array(acquired_int, new_array):
    # print("The Given unsorted Array is")
    # print(array1_list)
    for i in range(len(acquired_int)):
        for j in range(len(new_array)):
            if acquired_int[i] == new_array[j]:
                num1 = new_array[j]
                # print(f"The evicted num1 is {num1}")
                sorted_array.append(num1)
                # print(sorted_array)
                new_array.remove(num1)
                # print(array1_list)
                extraction_of_each_array_integer(new_array)
                exit()


def finding_the_smallest_integer_operation(emp_list, new_array):
    # Note: In the below if statement the occurrence of the smallest integer will always be
    # length of (array-1)
    length_of_array = len(new_array)
    if len(emp_list) > length_of_array - 2:
        integer_set = set(emp_list)
        required_int = list(integer_set)
        # print(f"The smallest integer of the Array is {required_int[0]}")
        forming_the_sorted_array(required_int, new_array)


def comparison_of_each_extracted_array_integer(y, array_list):
    empty_list = []
    for i in range(len(array_list)):
        if y < array_list[i]:
            empty_list.append(y)
        elif y > array_list[i]:
            empty_list = []

    # print(f"Before sending to printing operation {empty_list}")
    # emp_list = set(empty_list)
    finding_the_smallest_integer_operation(empty_list, array_list)


def extraction_of_each_array_integer(array_list):
    if len(array_list) == 1:
        # print("The length is now 1")
        print_the_sorted_array(array_list)
    for x in range(len(array_list)):
        y = array_list[x]
        comparison_of_each_extracted_array_integer(y, array_list)


# ----------------------------Actual statements start here -------------------------------------
array1 = np.array([5, 2, 7, 11, 8, 6, 9, 81, 33, 52, 76, 21, 201, 111, 19])
array1_list = list(array1)
print("The given Array is")
print(array1_list)
length_of_array1 = len(array1_list)

sorted_array = []
# Extract the integers of the array to an empty_list
extraction_of_each_array_integer(array1_list)

# -------------------------------------------Sample output is------------------------------------------------
# /usr/bin/python3.10 /home/swaroop/PycharmProjects/pythonCodingChallenge/SortingAnIntegerArrayOptimized.py
# The given Array is
# [5, 2, 7, 11, 8, 6, 9, 81, 33, 52, 76, 21, 201, 111, 19]
# The sorted Array is shown below
# [2, 5, 6, 7, 8, 9, 11, 19, 21, 33, 52, 76, 81, 111, 201]
#
# Process finished with exit code 0
