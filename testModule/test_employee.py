import unittest
from testModule.Employee import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.my_employee = Employee('long', 'zhou', 10000)
        self.result = ['long', 'zhou', 10000]

    def test_give_default_raise(self):
        self.assertEqual(self.result[0], self.my_employee.lastName)
        self.assertEqual(self.result[1], self.my_employee.firstName)
        self.assertEqual(self.result[2], self.my_employee.salary)

    def test_give_custom_raise(self):
        self.my_employee.give_raise(raises=12000)
        self.assertEqual(self.result[2] + 12000, self.my_employee.salary)

if __name__ == '__main__':
    unittest.main()
