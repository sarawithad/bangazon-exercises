import random

#Classes added for Exercise 1 (Defining Classes-_Departments) plus budget methods for Exercise 2 (Overriding Classes)
class Department:

	def __init__(self, name, supervisor, location, employee_count):
		self.name = name
		self.supervisor = supervisor
		self.location = location
		self.employee_count = employee_count
		self.budget = 32000
		self.employees = set()
	
	def get_dept_name(self):
		return self.name

	def count_employees(self):
		return self.employee_count

	def find_department(self):
		return self.location

	def find_supervisor(self):
		return self.supervisor

	def get_budget(self):
		return self.budget

	def get_employees(self):
		return self.employees


class Design(Department):

	def __init__(self, name, supervisor, location, employee_count):
		super().__init__(name, supervisor,location, employee_count)
		self.logos = set()

		self.budget = super().get_budget() + 8000

	def add_logos(self, logo_name, logo_image):

		self.logos.add(letterhead_logo, letterhead_image_file)


class Sales(Department):

	def __init__(self, name, supervisor, location, employee_count):
		super().__init__(name, supervisor,location, employee_count)
		self.awards = ()

		self.budget = super().get_budget() - 7000

	def add_awards(self, award_name, award_year):

		self.awards.add("best sales ever", "2009")


class Legal(Department):

	def __init__(self, name, supervisor, location, employee_count):
		super().__init__(name, supervisor,location, employee_count)
		self.policies = ()

		self.budget = super().get_budget() + 100000

	def add_policies(self, policy_name, policy_content):

		self.policies.add(("no_fraternization", "abcd123"))


class Technology(Department):

	def __init__(self, name, supervisor, location, employee_count):
		super().__init__(name, supervisor,location, employee_count)
		self.computers = ()

		self.budget = super().get_budget() -1000

	def add_computer_equipment(self, computer_type):

		self.add_computer_equipment(computer_type)


class Finance(Department):

	def __init__(self, name, supervisor, location, employee_count):
		super().__init__(name, supervisor,location, employee_count)
		self.calculators = ()

		self.budget = super().get_budget() + 2500

	def add_calculators(self, calculator_type):

		self.add_computer_equipment(calculator_type)


#Classes added for Exercise 3 (Method Overloading)
class Employee():

	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name

	def __str__(self):
		return "{} {}".format(self.first_name, self.last_name)

	def eat(self, companions = None, food = None):

		restaurants = ["burrito palace", "gyro nation", "little italy", "best sandwich shop ever"]
		chosen_restaurant = random.choice(restaurants)


		if companions is None and food is not None:
				print("{} ate a {} at the office today.".format(self.first_name, food))

		elif companions is None and food is None:
			print("{} ate alone at {}.".format(self.first_name, chosen_restaurant))
			return chosen_restaurant

		elif companions is not None and food is None:
			print("{} ate at {} with {}.".format(self.first_name, chosen_restaurant, (", ".join(companions))))

		elif companions is not None and food is not None:
			print("{} ate {} at {} with {}.".format(self.first_name, food, chosen_restaurant, (", ".join(companions))))



#Classes added for exercise 4 (multiple inheritance)
class FullTime():

	def __init__(self):
		self.hours_per_week = 40
		self.employmentType = "FullTime"


class Partime():

	def __init__(self):
		self.hours_per_week = 24
		self.employmentType = "PartTime"

class HumanResources(Employee, FullTime):
	def  __init__(self, first_name, last_name):
		super().__init__(first_name, last_name) #super here denotes Employee
		FullTime.__init__(self)

	def __str__(self):
		return "{} {} is a {} employee.".format(self.first_name, self.last_name, self.employmentType)


class Unsecured(Department, Employee):
	def __init__(self):
		self.securityCard = False


class Secured(Department, Employee):
	def __init__(self):
		self.securityCard = True


class isHandicapped(Employee):
	def __init__(self):
		self.handicap = True
		self.handiStatus = "handicapped"	

class notHandicapped(Employee):
	def __init__(self):
		self.handicap = False
		self.handiStatus = " not handicapped"	





if __name__ == '__main__':


	# Instantiates then prints the name of each of department instance (Exercise 1)
	design = Design("Design", "Carrie Carson", "Seattle", 5)
	sales = Sales("Sales", "Bill Williams", "Dallas", 50)
	technology = Technology("Technology", "Leah Lawson", "Seattle", 15)
	finance = Finance("Finance", "Larry Lewis", "Dallas", 10)
	legal = Legal("Legal", "Mary Miller", "Seattle", 8)

	print(design.name)
	print(sales.name)
	print(technology.name)
	print(finance.name)
	print(legal.name)

	#Prints adjusted budget for each department (Exercise 2)
	print("design budget = ", design.budget)
	print("sales budget = ", sales.budget)
	print("technology budget = ", technology.budget)
	print("finance budget = ", finance.budget)
	print("legal budget = ", legal.budget)


	#Print statements from method overloadng (Exercise 3)
	carl = Employee("Carl", "Carlson")
	print(carl)
	print(carl.eat())
	carl.eat(food="taco")
	carl.eat(companions =["Moe", "Larry", "Curly"])
	carl.eat(food="pizza", companions= ["Larry", "Moe", "Curly"])

	#Print statement from multiple inheritance (Exercise 4)
	HRemployee = HumanResources("Don", "Daniels")
	print(HRemployee)





