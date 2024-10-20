class Rental:
    """
    A rental of a movie by a customer.
    """

    def __init__(self, movie, days_rented, price_code):
        """Initialize a new movie rental object."""
        self.movie = movie
        self.days_rented = days_rented
        self.price_code = price_code  # Added attribute

    def get_price(self):
        """Get the rental price."""
        return self.price_code.get_price(self.days_rented)

    def get_rental_points(self):
        """Get the rental points."""
        return self.price_code.get_rental_points(self.days_rented)

    def get_movie(self):
        """Get the movie associated with this rental."""
        return self.movie

    def get_days_rented(self):
        """Get the number of days this movie was rented."""
        return self.days_rented
