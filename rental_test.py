import unittest
from rental import Rental
from movie import RegularMovie, NewReleaseMovie, ChildrensMovie

class RentalTest(unittest.TestCase):
    
    def setUp(self):
        self.new_movie = NewReleaseMovie()
        self.regular_movie = RegularMovie()
        self.childrens_movie = ChildrensMovie()

    def test_movie_attributes(self):
        """Trivial test to catch refactoring errors or change in API of Movie."""
        m = RegularMovie()
        self.assertEqual("Air", "Air")

    def test_rental_price(self):
        """Test the rental price calculation."""
        rental = Rental("Dune: Part Two", 1, self.new_movie)
        self.assertEqual(rental.get_price(), 3.0)
        rental = Rental("Dune: Part Two", 5, self.new_movie)
        self.assertEqual(rental.get_price(), 15.0)
        
        rental = Rental("Air", 3, self.regular_movie)
        self.assertEqual(rental.get_price(), 3.5)
        
        rental = Rental("Frozen", 4, self.childrens_movie)
        self.assertEqual(rental.get_price(), 3.0)

    def test_frequent_renter_points(self):
        """Test the calculation of frequent renter points."""
        rental = Rental("Dune: Part Two", 1, self.new_movie)
        self.assertEqual(rental.get_rental_points(), 1)
        
        rental = Rental("Dune: Part Two", 3, self.new_movie)
        self.assertEqual(rental.get_rental_points(), 3)
        
        rental = Rental("Air", 3, self.regular_movie)
        self.assertEqual(rental.get_rental_points(), 1)
        
        rental = Rental("Frozen", 4, self.childrens_movie)
        self.assertEqual(rental.get_rental_points(), 1)
