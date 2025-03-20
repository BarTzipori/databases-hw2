import unittest
import Solution as Solution
from Utility.ReturnValue import ReturnValue
from Tests.AbstractTest import AbstractTest

from Business.Owner import Owner
from Business.Customer import Customer
from Business.Apartment import Apartment
from datetime import date,datetime

'''
    Simple test, create one of your own
    make sure the tests' names start with test
'''


class Test(AbstractTest):
    def test_customer(self) -> None:
        c1 = Customer(1, 'a1')
        self.assertEqual(ReturnValue.OK, Solution.add_customer(c1), 'regular customer')
        c2 = Customer(2, 'a2')
        self.assertEqual(ReturnValue.OK, Solution.add_customer(c2), 'invalid name')
        c3= Customer(3, 'a3')
        self.assertEqual(ReturnValue.OK, Solution.add_customer(c3), 'invalid name')
        o1 = Owner(1, 'o1')
        self.assertEqual(ReturnValue.OK, Solution.add_owner(o1), 'regular customer')
        a1 = Apartment(1, "blabla", "blabla", "blabla", 1)
        self.assertEqual(ReturnValue.OK, Solution.add_apartment(a1), 'regular apartment')
        a2= Apartment(2, "blabla", "blabla2", "blabla", 1)
        self.assertEqual(ReturnValue.OK, Solution.add_apartment(a2), 'regular apartment')
        a3= Apartment(3, "blabla3", "blabla23", "blabla3", 1)
        self.assertEqual(ReturnValue.OK, Solution.add_apartment(a3), 'regular apartment')
        d1 = date(2023,4,1)
        d2 = date(2023,4,10)
        d3 = date(2023,5,1)
        d4 = date(2023,5,10)
        d5 = date(2023,5,11)
        d6 = date(2023, 5, 12)
        d7 = date(2023,5,13)
        d8 = date(2023, 5, 14)
        d9 = date(2023, 6, 12)
        self.assertEqual(ReturnValue.OK, Solution.customer_made_reservation(1, 1, d1, d2, 1), 'regular res')
        self.assertEqual(ReturnValue.OK, Solution.customer_made_reservation(1, 1, d3, d4, 1), 'regular res')
        self.assertEqual(ReturnValue.OK, Solution.customer_made_reservation(1, 1, d5, d6, 1), 'regular res')
        self.assertEqual(ReturnValue.BAD_PARAMS, Solution.customer_made_reservation(3, 1, d5, d6, 1), 'regular res')
        self.assertEqual(ReturnValue.OK, Solution.customer_made_reservation(3, 3, d7, d8, 1), 'regular res')
        self.assertEqual(ReturnValue.OK, Solution.owner_owns_apartment(1, 1), 'add ownership')





# *** DO NOT RUN EACH TEST MANUALLY ***
if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)
