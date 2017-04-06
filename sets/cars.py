# Instructions

# Create an empty set named showroom.
# Add four of your favorite car model names to the set.
# Print the length of your set.
# Pick one of the items in your show room and add it to the set again.
# Print your showroom. Notice how there's still only one instance of that model in there.
# Using update(), add two more car models to your showroom with another set.
# You've sold one of your cars. Remove it from the set with the discard() method.

showroom = set()
showroom.add("Audi A8")
showroom.add("Jeep Wrangler")
showroom.add("GMC Yukon")
showroom.add("BMW 330")
print(showroom)
print(len(showroom))

showroom.add("GMC Yukon")
print(showroom)

showroom2 = set()
showroom2.add("Honda Pilot")
showroom2.add("Ford F150")
print(showroom2)

showroom.update(showroom2)
print(showroom)

showroom.discard("Ford F150")
print(showroom)

# Acquiring more cars

# Now create another set of cars in a variable junkyard. Someone who owns a junkyard full of old cars has approached you about buying the entire inventory. In the new set, add some different cars, but also add a few that are the same as in the showroom set.
# Use the intersection method to see which cars exist in both the showroom and that junkyard.
# Now you're ready to buy the cars in the junkyard. Use the union method to combine the junkyard into your showroom.
# Use the discard() method to remove any cars that you acquired from the junkyard that you want in your showroom.

junkyard = set()
junkyard.add("pinto")
junkyard.add("jalopy")
junkyard.add("Chevy Nova")
junkyard.add("Audi A8")
junkyard.add("Honda Pilot")
junkyard.add("GMC Yukon")
print(junkyard)

all_cars = showroom.intersection(junkyard)
print(all_cars)

cars_now_owned = showroom.union(junkyard)
print(cars_now_owned)

cars_now_owned.discard("jalopy")
cars_now_owned.discard("pinto")
print(cars_now_owned)



