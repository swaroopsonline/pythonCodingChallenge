# Given an array of N integers. Find the first element that occurs at least K number of times.
# Dated: 5th May 2023
# This code is a work in progress.

import numpy


def find_the_first_occurrence(occur_list, reversed_list):
    for a in range(len(occur_list)):
        for b in range(len(reversed_list)):
            if occur_list[a] == reversed_list[b]:
                print(f"{occur_list[1]} has the first occurrence")
                exit()


def reverse_original_list(origin_list, occur_list):
    # print(f"occur_list is {occur_list}")
    # print(f"origin_list is {origin_list}")

    len_origin_list = len(origin_list)
    z = len_origin_list - 1
    while not z < 0:
        reverse_list.append(origin_list[z])
        z = z - 1

    print(reverse_list)

    find_the_first_occurrence(occur_list, reverse_list)


def compare_occurrence_with_original(occur_list, origin_list):
    reverse_original_list(origin_list, occur_list)


def compare_the_two_lists(list_unique, list_original):
    for i in range(len(list_unique)):
        counter = 0
        for j in range(len(list_original)):

            if list_unique[i] == list_original[j]:
                counter = counter + 1
            else:
                continue

        if counter >= 2:
            occurrence_list.append(list_unique[i])
            # print(f"{list_unique[i]} is the first number to occur {counter} times")
            # break

    print(occurrence_list)
    compare_occurrence_with_original(occurrence_list, list_original)


# ----------------------------Actual statements start here -------------------------------------

N = 7,
K = 2

array1 = numpy.array([1, 7, 4, 3, 7, 8, 4])
list_array1 = list(array1)
print(list_array1)

set_list = set(list_array1)
# print(set_list)

list_array_unique = list(set_list)
# print(list_array_unique)

occurrence_list = []
reverse_list = []

compare_the_two_lists(list_array_unique, list_array1)
