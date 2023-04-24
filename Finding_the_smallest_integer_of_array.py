# This is a simple code to find out the smallest integer of an unsorted Array
# Dated: 24th April 2023
import numpy as np


def extraction_of_each_array_integer():
    for x in range(len(array1_list)):
        y = array1_list[x]
        comparison_of_each_extracted_array_integer(y)


# x = array1_list[3]
# y = array1_list[1]

def printing_operation(emp_list):
    # Note: In the below if statement the occurrence of the smallest integer will always be
    # length of (array-1)
    if len(emp_list) > length_of_array1 - 2:
        integer_set = set(emp_list)
        required_int = list(integer_set)
        print(f"The smallest integer of the Array is {required_int[0]}")
        # print(emp_list)


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

# Extract the integers of the array to an empty_list
extraction_of_each_array_integer()

# -------------------------------------------Sample output is------------------------------------------------
# /usr/bin/python3.10 /home/swaroop/PycharmProjects/pythonCodingChallenge/Finding_the_smallest_integer_of_array.py
# The smallest integer of the Array is 2
#
# Process finished with exit code 0
