# Reverse a number

num = 123456

print(num)

stringNum = str(num)

list1 = list(stringNum)

list2 = []
i = len(list1)
j = i - 1
print(list1)

for i in range(len(list1)):

    list2.append(list1[j])
    j = j - 1

print(list2)

# Concatenate characters from the list into a string using join()

reversed_string = ''.join(list2)
print(reversed_string)

reversed_num = int(reversed_string)
print(reversed_num)





