class Movie:
    """
    A movie available for rent.
    """
    # The types of movies (price_code). 
    REGULAR = 0
    NEW_RELEASE = 1
    CHILDRENS = 2
    
    def __init__(self, title, price_code):
        """Initialize a new movie."""
        self.title = title
        self.price_code = price_code

    def get_price_code(self):
        """Get the price code."""
        return self.price_code
    
    def get_title(self):
        """Get the movie title."""
        return self.title
    
    def get_price(self, days_rented):
        """Calculate the price for renting this movie."""
        if self.price_code == Movie.REGULAR:
            amount = 2.0
            if days_rented > 2:
                amount += 1.5 * (days_rented - 2)
        elif self.price_code == Movie.CHILDRENS:
            amount = 1.5
            if days_rented > 3:
                amount += 1.5 * (days_rented - 3)
        elif self.price_code == Movie.NEW_RELEASE:
            amount = 3 * days_rented
        else:
            raise ValueError(f"Unknown price code {self.price_code}")

        return amount

    def get_frequent_renter_points(self, days_rented):
        """Calculate frequent renter points for this movie."""
        if self.price_code == Movie.NEW_RELEASE:
            return days_rented
        return 1

    def __str__(self):
        return self.title
