# Create a Department class. Create some simple properties and methods on Department. You are going to create some derived classes that inherit from Department, so make sure that the properties/methods you add are general to all Departments.


class Department:

	def __init__(self, name, supervisor, location, employee_count):
		self.name = name
		self.supervisor = supervisor
		self.location = location
		self.employee_count = employee_count
		self.budget = 32000
	
	def get_dept_name(self):
		return self.name

	def count_employees(self):
		return self.employee_count

	def find_department(self):
		return self.location

	def find_supervisor(self):
		return self.supervisor

	# def meet(self):
	# 	print()

	def get_budget(self):
		return self.budget


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

if __name__ == '__main__':
	# main()

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

	print("design budget = ", design.budget)
	print("sales budget = ", sales.budget)
	print("technology budget = ", technology.budget)
	print("finance budget = ", finance.budget)
	print("legal budget = ", legal.budget)



