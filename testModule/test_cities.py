import unittest
from testModule.city_functions import city_function


class TestCities(unittest.TestCase):
    def test_city_country(self):
        formatted_city = city_function('chengdu', 'china','30000000')
        self.assertEqual(formatted_city, 'chengdu,china-population 30000000')


unittest.main()
