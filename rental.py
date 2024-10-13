class Rental:
    """
    A rental of a movie by a customer.

    A realistic Rental would have fields for the dates
    that the movie was rented and returned, from which the
    rental period is calculated. For simplicity, only days_rented is recorded.
    """
    
    def __init__(self, movie, days_rented): 
        """Initialize a new movie rental object for
        a movie with known rental period (daysRented).
        """
        self.movie = movie
        self.days_rented = days_rented

    def get_movie(self):
        """Get the movie associated with this rental."""
        return self.movie

    def get_days_rented(self):
        """Get the number of days this movie was rented."""
        return self.days_rented

    def get_price(self):
        """Calculate the price for this rental."""
        price_code = self.get_movie().get_price_code()

        if price_code == Movie.REGULAR:
            amount = 2.0
            if self.get_days_rented() > 2:
                amount += 1.5 * (self.get_days_rented() - 2)
        elif price_code == Movie.CHILDRENS:
            amount = 1.5
            if self.get_days_rented() > 3:
                amount += 1.5 * (self.get_days_rented() - 3)
        elif price_code == Movie.NEW_RELEASE:
            amount = 3 * self.get_days_rented()
        else:
            raise ValueError(f"Unknown price code {price_code}")

        return amount

    def get_frequent_renter_points(self):
        """Calculate frequent renter points for this rental."""
        if self.get_movie().get_price_code() == Movie.NEW_RELEASE:
            return self.get_days_rented()
        return 1
