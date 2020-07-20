class Employee(object):
    def __init__(self, last_name, first_name, annual_salary):
        self.lastName = last_name
        self.firstName = first_name
        self.salary = annual_salary

    def give_raise(self, raises=5000):
        self.salary = self.salary + raises
