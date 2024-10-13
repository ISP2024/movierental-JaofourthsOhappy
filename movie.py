class Movie:
    """A movie available for rent."""

    def __init__(self, title):
        """Initialize a movie with a title."""
        self.title = title

    def get_title(self):
        """Get the movie title."""
        return self.title
    
    def get_price(self, days_rented):
        """Calculate the price for renting this movie."""
        raise NotImplementedError("Subclasses should implement this method")
    
    def get_frequent_renter_points(self, days_rented):
        """Calculate frequent renter points for this movie."""
        return 1  # Default implementation returns 1 frequent renter point


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
