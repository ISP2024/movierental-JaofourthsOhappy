class Rental:
    """
    A rental of a movie by customer.
    From Fowler's refactoring example.

    A realistic Rental would have fields for the dates
    that the movie was rented and returned, from which the
    rental period is calculated.
    For simplicity of this application only days_rented is recorded.
    """
    
    def __init__(self, movie, days_rented): 
    	"""Initialize a new movie rental object for
    	   a movie with known rental period (daysRented).
    	"""
    	self.movie = movie
    	self.days_rented = days_rented

    def get_movie(self):
    	return self.movie

    def get_days_rented(self):
    	return self.days_rented

    def get_price(self):
        """Calculate the rental price based on the movie's price code."""
        amount = 0
        if self.movie.get_price_code() == Movie.REGULAR:
            amount = 2.0
            if self.get_days_rented() > 2:
                amount += 1.5 * (self.get_days_rented() - 2)
        elif self.movie.get_price_code() == Movie.CHILDRENS:
            amount = 1.5
            if self.get_days_rented() > 3:
                amount += 1.5 * (self.get_days_rented() - 3)
        elif self.movie.get_price_code() == Movie.NEW_RELEASE:
            amount = 3 * self.get_days_rented()
        return amount