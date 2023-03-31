# This Code will implement the Fibonacci series in Python. And a list of fibonacci series for up to 22
# occurrences will be printed.
# Dated: 31st March 2023.

x = 0
y = 1

list1 = [x, y]

for i in range(0, 10):
    x = x + y
    y = x + y

    list1.append(x)
    list1.append(y)

print(list1)
print("The length of the fibonacci list is", len(list1))
