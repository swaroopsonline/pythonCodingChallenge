# This Code will showcase the Dictionary use cases(which is nothing but the hashmap implementation in Python)
# Dated: 19th April 2023

"""
CREATE
"""

# Creating an empty dictionary

data1 = {}  # -----> 1st way of creating an empty dictionary
print(type(data1))

data2 = dict()  # -----> 2nd way of creating an empty dictionary
print(type(data2))

# Creating a regular dictionary

data3 = {
    "name": "Harry",
    "age": 22,
    "salary": 60000,
    134: "Class Number",
    "Class Students": ["Hermione", "Ron", "Haguid"],
    45.6: 5
}
print(data3)

# Can we give a list as key for a dictionary? ---> Ans: No
# Mutable data types cannot be taken as a key

data4 = {
    (1, 2, 3, 4, 5): "Dumbledore"
}
print(type(data4))
print(data4)

# Can we convert a list of tuples into a dictionary? ---> Ans: Yes
list_1 = [(1, 2), ("name", "Rory"), ("age", 33)]
print(list_1)

data5 = dict(list_1)
print(type(data5))
print(data5)

# Can we convert a list of lists into a dictionary? -----> Yes

list_2 = [[1, 2], ["ajay", "amir"], [45.3, 9]]

data6 = dict(list_2)
print(type(data6))
print(data6)

# Can we convert a list of Sets into a dictionary? Ans: Yes

list_3 = [{"Harry", "Ron"}, {43, 5}, {4.8, "Marks"}]
data7 = dict(list_3)
print(type(data7))
print(data7)

# Can we declare Dictionaries in a Tuple? -----> Ans: Yes
tuple1 = ({'Ron': 'Harry', 'Student': 'Yes'}, {45: 8}, {"Age": 23})
print(tuple1)
print(type(tuple1))

print(type(tuple1[0]))

# Can we declare Lists in a Tuple? -----> Ans Yes
tuple2 = ([1, 2], ["Harry", "Hermione"], [45.9, True])
print(type(tuple2))
print(tuple2)

# Can we declare Sets in a Tuple? -----> Ans Yes
tuple3 = ({1, 3, 4, 6.7}, {"asdf", 4, False})
print(type(tuple3))
print(tuple3)

# How to read complete dictionary ?
example = {1: 2, "name": "Ashish"}
print(example)

# How to read a single value of a key in dictionary ?
print(example[1])
print(example["name"])
print(example.get(12))  # ------> It will return 'None'

# How to update a single value of a key in dictionary ?
data8 = {"name": "Ankit", "age": 11, 1: 45, 4.5: "Ashish", 7: 3}
print("Before changing the name", data8)
data8["name"] = "Ashish"
print("After changing the name", data8)

# How to add a new key value pair in a dictionary?
data8["salary"] = 180000
print("data8 with a new key & value pair", data8)

# Understanding popitem() function -----> It will remove 'key value pairs' one by one from the right end of
# the dictionary.
example2 = {1: 2, "name": "Ashish"}
example2.popitem()
print("example2 after doing a popitem", example2)

example2.pop(1)  # -----> It will remove the items for the given keys, i.e the corresponding key & value pair
# will be removed.
print("example2 after doing pop", example2)

# example2.popitem()
# print("example2 after doing popitem a second time", example2)

example3 = {1: 2, 2: 3, 3: 4, 4: 5, 5: 6}
print(1 in example3)
print(11 not in example3)
print(44 in example3)
