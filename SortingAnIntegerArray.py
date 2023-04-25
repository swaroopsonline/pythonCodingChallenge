# -------------------- This is a Code to sort an unsorted Integer Array.---------------------------
# Dated: 25th April 2023
import numpy as np


def extraction_of_each_array_integer():
    for x in range(len(array1_list)):
        y = array1_list[x]
        comparison_of_each_extracted_array_integer(y)


def do_the_pop(acquired_int, formed_array):
    for i in range(len(acquired_int)):
        for j in range(len(formed_array)):
            if acquired_int[i] == formed_array[j]:
                num1 = formed_array[j]
                # print(f"The evicted num1 is {num1}")
                sorted_array.append(num1)
                # print(sorted_array)
                formed_array.remove(num1)
                # print(formed_array)
                do_the_extraction(formed_array)
                exit()


def print_operation(emp_list, new_array):
    length_of_new_array = len(new_array)
    if len(emp_list) > length_of_new_array - 2:
        integer_set = set(emp_list)
        required_int = list(integer_set)
        # print(f"The smallest integer of the Array is {required_int[0]}")
        # do_the_pop_operation_from_the_array(required_int)
        do_the_pop(required_int, new_array)


def do_the_comparison(y, new_array):
    empty_list = []

    for i in range(len(new_array)):
        if y < new_array[i]:
            empty_list.append(y)
        elif y > new_array[i]:
            empty_list = []

    # print(f"the new empty_list is {empty_list}")
    print_operation(empty_list, new_array)


def print_the_sorted_array(new_array):
    # print(f"The last array is {new_array}")
    last_int = new_array[0]
    sorted_array.append(last_int)
    print("The sorted Array is shown below")
    print(sorted_array)


def do_the_extraction(new_array):
    if len(new_array) == 1:
        # print("The length is now 1")
        print_the_sorted_array(new_array)

    for x in range(len(new_array)):
        y = new_array[x]
        do_the_comparison(y, new_array)


def do_the_pop_operation_from_the_array(acquired_int):
    print("The Given unsorted Array is")
    print(array1_list)
    for i in range(len(acquired_int)):
        for j in range(len(array1_list)):
            if acquired_int[i] == array1_list[j]:
                num1 = array1_list[j]
                # print(f"The evicted num1 is {num1}")
                sorted_array.append(num1)
                # print(sorted_array)
                array1_list.remove(num1)
                # print(array1_list)
                do_the_extraction(array1_list)
                exit()


def printing_operation(emp_list):
    # Note: In the below if statement the occurrence of the smallest integer will always be
    # length of (array-1)
    if len(emp_list) > length_of_array1 - 2:
        integer_set = set(emp_list)
        required_int = list(integer_set)
        # print(f"The smallest integer of the Array is {required_int[0]}")
        do_the_pop_operation_from_the_array(required_int)


def comparison_of_each_extracted_array_integer(y):
    empty_list = []
    for i in range(len(array1_list)):
        if y < array1_list[i]:
            empty_list.append(y)
        elif y > array1_list[i]:
            empty_list = []

    # print(f"Before sending to printing operation {empty_list}")
    # emp_list = set(empty_list)
    printing_operation(empty_list)


# ----------------------------Actual statements start here -------------------------------------
array1 = np.array([5, 2, 7, 11, 8, 6, 9])
array1_list = list(array1)
length_of_array1 = len(array1_list)

sorted_array = []
# Extract the integers of the array to an empty_list
extraction_of_each_array_integer()

# -------------------------------------------Sample output is------------------------------------------------
# /usr/bin/python3.10 /home/swaroop/PycharmProjects/pythonCodingChallenge/SortingAnIntegerArray.py
# The Given unsorted Array is
# [5, 2, 7, 11, 8, 6, 9]
# The sorted Array is shown below
# [2, 5, 6, 7, 8, 9, 11]
#
# Process finished with exit code 0
