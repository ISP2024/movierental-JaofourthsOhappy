class Rental:
    """
    A rental of a movie by customer.
    A realistic Rental would have fields for the dates
    that the movie was rented and returned, from which the
    rental period is calculated. For simplicity of this 
    application only days_rented is recorded.
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
