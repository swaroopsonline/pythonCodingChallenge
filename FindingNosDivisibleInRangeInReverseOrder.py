""""
Find the nos divisible by 3 between 500 to 700 in reverse order
"""

j=700
for i in range(500,700):

    if j%3 == 0:
        print(j)
    j=j-1

print("----------------------")

j=700
for i in range(200):

    if j%3 == 0:
        print(j)
    j=j-1
