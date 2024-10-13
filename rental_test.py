import unittest
from rental import Rental
from movie import Movie

class RentalTest(unittest.TestCase):
    
    def setUp(self):
        self.new_movie = Movie("Dune: Part Two", Movie.NEW_RELEASE)
        self.regular_movie = Movie("Air", Movie.REGULAR)
        self.childrens_movie = Movie("Frozen", Movie.CHILDRENS)

    def test_movie_attributes(self):
        """Trivial test to catch refactoring errors or change in API of Movie."""
        m = Movie("Air", Movie.REGULAR)
        self.assertEqual("Air", m.get_title())
        self.assertEqual(Movie.REGULAR, m.get_price_code())

    def test_rental_price(self):
        """Test the rental price calculation."""
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.get_movie().get_price(1), 3.0)
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_movie().get_price(5), 15.0)
        
        rental = Rental(self.regular_movie, 3)
        self.assertEqual(rental.get_movie().get_price(3), 3.5)
        
        rental = Rental(self.childrens_movie, 4)
        self.assertEqual(rental.get_movie().get_price(4), 3.0)

    def test_frequent_renter_points(self):
        """Test the calculation of frequent renter points."""
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.get_movie().get_frequent_renter_points(1), 1)
        
        rental = Rental(self.new_movie, 3)
        self.assertEqual(rental.get_movie().get_frequent_renter_points(3), 3)
        
        rental = Rental(self.regular_movie, 3)
        self.assertEqual(rental.get_movie().get_frequent_renter_points(3), 1)
        
        rental = Rental(self.childrens_movie, 4)
        self.assertEqual(rental.get_movie().get_frequent_renter_points(4), 1)
