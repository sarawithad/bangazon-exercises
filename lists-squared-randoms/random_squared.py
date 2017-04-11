# Instructions

# Using the random module and the range method, generate a list of 20 random numbers between 0 and 49.

# import random

# random_numbers = [...insert awesome code here...]
# print(random_numbers)

# With the resulting list, use a list comprehension to build a new list that contains each number squared. For example, if the original list is [2, 5], the final list will be [4, 25].

import random

def get_numbers():
	for i in range(20):
		yield random.randint(0,49)

number_list = list()		

for random_number in get_numbers():
	number_list.append(random_number)
print("randoms: ", number_list)

squared_numbers = [n*n for n in number_list]
print("squared randoms: ", squared_numbers)
