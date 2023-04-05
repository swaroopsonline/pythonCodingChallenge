# ---------------------------- To check if two arrays are equal or not ---------------------------------
# Dated: 3rd April 2023
import numpy as np

# Description: Given two arrays A and B of equal size N, the task is to find if given arrays are equal or not.
# Two arrays are said to be equal if both of them contain same set of elements, arrangements (or permutation)
# of elements may be different though.
# Note : If there are repetitions, then counts of repeated elements must also be same for two array to be equal.

# Note: In the below example an Array is declared. However, an array will always consider its elements of the same
# DataType.
# arr1 = np.array(["Hyundai", 1, "Volvo", "Maruti", False])
arr1 = np.array([2, "Logan", "Fiat", True, "Volvo", 3])

arr2 = np.array(["Volvo", True, "Fiat", "Logan", 2, 3, 3, 3, 3, 3, 4])

# First converting both the Arrays to List

listarr1 = list(arr1)
listarr2 = list(arr2)

# Converting both the Arrays to Set to identify the Unique elements
set1 = set(listarr1)
listset1 = list(set1)

set2 = set(listarr2)
listset2 = list(set2)

# Declaring an empty list by the name of listarr to extract the common elements of both the Arrays.
listarr = list()


# Creating a Function to extract the common elements from both the Arrays
def common_elements():
    for i in range(len(listset1)):
        for j in range(len(listset2)):
            if listset1[i] == listset2[j]:
                listarr.append(listset1[i])


if len(listarr1) == len(listarr2):
    common_elements()
    print("Both the Arrays are equal in size")
    print("Common elements for the same sized arrays are", listarr)
elif len(listarr1) != len(listarr2):
    common_elements()
    print("Both the Arrays are not equal in size")
    print("Common elements for the varied sized arrays are", listarr)

if len(listarr) == len(listset1):
    if len(listarr) == len(listset2):
        print("The Arrays are equal in content")
    else:
        print("The Arrays are not equal in content ----> There you are")
else:
    print("The Arrays are not equal in content")
