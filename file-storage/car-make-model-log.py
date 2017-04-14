import sys

#lists have to be available globally to append correctly
make_list = list()
model_list = list()

# Create a single class that implements all functionality.
class Automobile:

# Create a method for reading the car-makes file.
	def read_car_makes():
		with open("car-makes.txt", "r") as makes:
			for carmake in makes:
				carmake = carmake.replace("\n", " ")
				make_list.append(carmake)
			# print(make_list)

# Create a method for reading the car-models file.
	def read_car_models():
		with open("car-models.txt", "r") as models:
			for carmodel in models:
				carmodel = carmodel.replace("\n", " ")
				model_list.append(carmodel)
			# print(model_list)


# # Create a method that invokes the previous two methods and generates a dictionary.
# # The dictionary keys will be the make names.
# # The value for each key will be a list of model names.
# # {
# #     "Toyota": ["Camry"],
# #     ...
# # }

	def combine_make_model():
		make_model_dict = dict()

		Automobile.read_car_makes() #invoke read makes
		Automobile.read_car_models() #invoke read models
		for carmake in make_list: #iterate through makes to add to new dictionary
			make_model_dict[carmake] = list()
			for carmodel in model_list: #iterate through makes to add to new dictionary
				if carmake[0] == carmodel[0]:
					make_model_dict[carmake].append(carmodel[2:]) 

		print(make_model_dict)



if __name__ == '__main__':

	Automobile.combine_make_model()



	
