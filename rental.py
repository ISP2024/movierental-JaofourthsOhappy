class Rental:
    """
    A rental of a movie by a customer.
    """

    def __init__(self, movie, days_rented): 
        """Initialize a new movie rental object."""
        self.movie = movie
        self.days_rented = days_rented

    def get_movie(self):
        """Get the movie associated with this rental."""
        return self.movie

    def get_days_rented(self):
        """Get the number of days this movie was rented."""
        return self.days_rented
