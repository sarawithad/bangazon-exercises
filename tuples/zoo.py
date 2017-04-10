# Create a tuple named zoo that contains your favorite animals.

zoo = ("panda", "elephant", "leopard", "monkey", "flamingo", "giraffe")

# Find one of your animals using the .index(value) method on the tuple.
index = zoo.index("panda")
print(index)

# Determine if an animal is in your tuple by using for value in tuple.
for animal in zoo:
	print(animal)

# Create a variable for each of the animals in your tuple with this cool feature of Python.
# (lizard, fox, mammoth) = zoo
# print(lizard)

(panda, elephant, leopard, monkey, flamingo, giraffe) = zoo
print(giraffe)

# Convert your tuple into a list.
new_zoo = list(zoo)

# Use extend() to add three more animals to your zoo.
new_zoo.extend(["cheetah", "peacock", "otter"])

# Convert the list back into a tuple.
final_zoo = tuple(new_zoo)
print("final zoo: ", final_zoo)