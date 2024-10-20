class Movie:
    """A movie available for rent."""

    def __init__(self, title, movie_type):
        """Initialize a movie with a title and type."""
        self.title = title
        self.movie_type = movie_type

    def get_title(self):
        """Get the movie title."""
        return self.title

    def get_movie_type(self):
        """Get the movie type."""
        return self.movie_type
    
class RegularMovie(Movie):
    """A regular movie."""

    def get_price(self, days_rented):
        """Calculate price for regular movie."""
        amount = 2.0
        if days_rented > 2:
            amount += 1.5 * (days_rented - 2)
        return amount


class NewReleaseMovie(Movie):
    """A new release movie."""

    def get_price(self, days_rented):
        """Calculate price for new release movie."""
        return 3 * days_rented

    def get_frequent_renter_points(self, days_rented):
        """New releases earn 1 point per day rented."""
        return days_rented


class ChildrensMovie(Movie):
    """A children's movie."""

    def get_price(self, days_rented):
        """Calculate price for children's movie."""
        amount = 1.5
        if days_rented > 3:
            amount += 1.5 * (days_rented - 3)
        return amount
