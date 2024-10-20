import re
import unittest 
from customer import Customer
from rental import Rental
from pricing import RegularMovie, NewReleaseMovie, ChildrensMovie

class CustomerTest(unittest.TestCase): 
    """Tests of the Customer class"""
    
    def setUp(self):
        """Test fixture contains:
        c = a customer
        movies = list of some movies
        """
        self.c = Customer("Movie Mogul")
        self.new_movie = NewReleaseMovie()
        self.regular_movie = RegularMovie()
        self.childrens_movie = ChildrensMovie()
    
    def test_statement(self):
        stmt = self.c.statement()
        pattern = r".*Total [Cc]harges\s+(\d+\.\d\d).*"
        matches = re.match(pattern, stmt, flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("0.00", matches[1])
        
        # Add a rental
        self.c.add_rental(Rental("Mulan", 4, self.new_movie)) # days
        stmt = self.c.statement()
        matches = re.match(pattern, stmt.replace('\n', ''), flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("12.00", matches[1])
