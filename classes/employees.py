# Create a class that contains information about employees of a company and define methods to get/set employee name, job title, and start date.

# Consider the concept of aggregation, and modify the Company class so that you assign employees to a company.

# class Company(object):
#     """This represents a company in which people work"""

#     def __init__(self, name, title, start_date):
#         self.name = name
#         self.title = title
#         self.start_date = start_date

#     def get_name(self):
#         """Returns the name of the company"""
        
#         return self.name

class Company():
    """This represents a company in which people work"""
    def __init__(self, name):
        self.name = name

        self.employees = set()

    def get_name(self):
    #     """Returns the name of the company"""
        return self.name



class Employee():

    def __init__(self, fn, ln, title, start_date):
        self.firstName = fn
        self.lastName = ln
        self.title = title
        self.start_date = start_date

    def get_firstName(self):
        return self.firstName

    def get_lastName(self):
        return self.lastName

    def get_title(self):
      return self.title

    def get_start_date(self):
      return self.start_date


# Create a company, and three employees, and then assign the employees to the company.

if __name__ == "__main__":

    Bangazon = Company("Bangazon") #creates the company

    dara = Employee("Dara", "Thomas", "BA Developer", "April 3")
    steve = Employee("Steve", "Brownlee", "Coach Bossman", "January 1")
    meg = Employee("Megan", "Ducharme", "Queen TA", "April 3")

    Bangazon.employees.add(dara)
    Bangazon.employees.add(steve)
    Bangazon.employees.add(meg)

    print(Bangazon.employees)
    print(Bangazon.name)

