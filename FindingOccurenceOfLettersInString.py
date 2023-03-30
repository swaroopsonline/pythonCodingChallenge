# ------------------------- Finding Occurrence of characters in a String -----------------------------
# Dated: 30th March 2023

string1 = input('Enter any String:')

# string1 = "honolulu"
# Converting String into a List
strList = list(string1)
# print(strList)

# Converting String into a Set
strSet = set(string1)
# print(strSet)

listStrSet = list(strSet)
# print(listStrSet)
# print(listStrSet[4])

# Now apply the for loop to count the occurrences of characters in a String.

for i in range(len(listStrSet)):
    x = 0
    for j in range(len(strList)):
        if listStrSet[i] == strList[j]:
            x = x + 1
        else:
            continue

    print(f"The Occurrence of {listStrSet[i]} is {x}")
