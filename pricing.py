class PriceStrategy:
    """Base class for different movie pricing strategies."""
    
    def get_price(self, days_rented):
        """Calculate the price for the rental period."""
        raise NotImplementedError("Subclasses should implement this method")
    
    def get_rental_points(self, days_rented):
        """Calculate frequent renter points."""
        return 1  # Default is 1 frequent renter point


class RegularMovie(PriceStrategy):
    """Pricing strategy for regular movies."""

    def get_price(self, days_rented):
        amount = 2.0
        if days_rented > 2:
            amount += 1.5 * (days_rented - 2)
        return amount


class NewReleaseMovie(PriceStrategy):
    """Pricing strategy for new release movies."""

    def get_price(self, days_rented):
        return 3 * days_rented

    def get_rental_points(self, days_rented):
        return days_rented  # Earn 1 point per day rented


class ChildrensMovie(PriceStrategy):
    """Pricing strategy for children's movies."""

    def get_price(self, days_rented):
        amount = 1.5
        if days_rented > 3:
            amount += 1.5 * (days_rented - 3)
        return amount
