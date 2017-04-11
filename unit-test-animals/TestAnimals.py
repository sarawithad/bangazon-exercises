import unittest
from animals import *

# def setUpModule():

# def tearDownModule():


class TestAnimals(unittest.TestCase):

	# In the test class' setUpClass() method, create an instance of Animal and Dog.
	@classmethod
	def setUpClass(self):
		self.animal = Animal("Sparky", "Porcupine")
		self.sam = Dog("Sam")

	# Write test cases to verify the I/O of the following methods of Animal and Dog:

	# Animal object has the correct name property.

	# Set a species and verify that the object property of species has the correct value.
	def test_animal_name_property_has_correct_value(self):
		self.assertEqual(self.animal.name, "Sparky")

	def test_animal_species_property_has_correct_value(self):
		self.assertEqual(self.animal.species, "Porcupine")

	def test_dog_species_property_has_correct_value(self):
		self.assertEqual(self.sam.species, "Dog")

	# Invoking the walk() method set the correct speed on the both objects.
	def test_walk_method_sets_speed(self):
		legs = 4
		self.animal.set_legs(legs)
		self.animal.walk()

		self.sam.set_legs(legs)
		self.sam.walk()

		self.assertEqual(self.animal.speed, 0.4)
		self.assertEqual(self.sam.speed, 0.8)


	# The animal object is an instance of Animal.
	def test_animal_is_correct_type(self):
		self.assertIsInstance(self.animal, Animal)


	# The dog object is an instance of Dog.
	def test_dog_is_correct_type(self):
		self.assertIsInstance(self.sam, Dog)


if __name__ == '__main__':
    unittest.main()

#Test to run in command line: python -m unittest discover -s . -p "TestAnimals.py" -v

