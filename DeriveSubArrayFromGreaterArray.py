# ------This Code will derive a Sub-Array from an Array when the end integers of a Sub-Array are known------
# Dated: 14th April 2023

list1 = [1, 2, 3, 7, 5]
list2 = [2, 7]  # ------> These are the end integers from which the Sub-array from the larger Array will be derived.

empty_list = []

for i in range(len(list2)):
    for j in range(len(list1)):
        if list2[i] == list1[j]:
            empty_list.append(j)

print("The relevant indexes of the larger array are ", empty_list)

x = empty_list[0]
y = empty_list[1]

# print(x)
# print(y)
sub_array = []

for k in range(x, y + 1):
    sub_array.append(list1[k])

print(sub_array)
