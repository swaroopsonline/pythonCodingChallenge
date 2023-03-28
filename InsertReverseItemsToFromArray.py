# ---------------------------------- Date: 28 March 2023 ---------------------------------------------
# This code reverses an order of an Array in Python
import numpy as np

arr1 = np.array(["Fiat", "Maruti", "Volvo","Jaguar","Mazeratti","Bentley","Honda"])
print("type of arr1 before delete is ",type(arr1))
print("arr1 before delete", arr1)

# Converting array back to list

listArray1 = list(arr1)
listArray2 = []


i = len(listArray1)
j = i - 1

for i in range(len(listArray1)):

    listArray2.append(listArray1[j])
    j = j - 1



# Delete arr1

del arr1
# Converting list back to the array
arr1 = np.array(listArray2)
print("arr1 after delete", arr1)
print("Type of arr1 after delete and reversing the order is ", type(arr1))
