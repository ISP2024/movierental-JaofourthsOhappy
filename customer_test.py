import re
import unittest 
from customer import Customer
from rental import Rental
from movie import RegularMovie, NewReleaseMovie, ChildrensMovie

class CustomerTest(unittest.TestCase): 
    """Tests of the Customer class"""
    
    def setUp(self):
        """Test fixture contains:
        c = a customer
        movies = list of some movies
        """
        self.c = Customer("Movie Mogul")
        self.new_movie = NewReleaseMovie("Mulan")
        self.regular_movie = RegularMovie("CitizenFour")
        self.childrens_movie = ChildrensMovie("Frozen")
    
    def test_statement(self):
        stmt = self.c.statement()
        # get total charges from statement using a regex
        pattern = r".*Total [Cc]harges\s+(\d+\.\d\d).*"
        matches = re.match(pattern, stmt, flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("0.00", matches[1])
        
        # add a rental
        self.c.add_rental(Rental(self.new_movie, 4)) # days
        stmt = self.c.statement()
        matches = re.match(pattern, stmt.replace('\n', ''), flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("12.00", matches[1])
