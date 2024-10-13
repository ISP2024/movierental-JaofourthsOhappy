from rental import Rental
from movie import Movie
import logging

class Customer:
    """A customer who rents movies.

    The customer object holds information about the
    movies rented for the current billing period,
    and can print a statement of his rentals.
    """

    def __init__(self, name: str):
        """Initialize a new customer."""
        self.name = name
        self.rentals = []

    def add_rental(self, rental: Rental):
        """Add a rental for this customer"""
        if rental not in self.rentals:
            self.rentals.append(rental)
    
    def get_name(self):
        """Get the customer's name."""
        return self.name
    
    def statement(self):
        """Create a statement of rentals for the current period.

        Print all the rentals in the current period, 
        along with total charges and frequent renter points.
        
        Returns:
            The statement as a string.
        """
        total_amount = 0   # total rental charges
        frequent_renter_points = 0
        statement = f"Rental Report for {self.name}\n\n"
        header_fmt = "{:40s}  {:6s} {:6s}\n"
        statement += header_fmt.format("Movie Title", "  Days", " Price")
        rental_fmt = "{:40s}  {:6d} {:6.2f}\n"
        
        for rental in self.rentals:
            # get the rental price from Rental class
            amount = rental.get_price()

            # compute the frequent renter points
            if rental.get_movie().get_price_code() == Movie.NEW_RELEASE:
                frequent_renter_points += rental.get_days_rented()
            else:
                frequent_renter_points += 1

            # add a detail line to the statement
            statement += rental_fmt.format(
                            rental.get_movie().get_title(), 
                            rental.get_days_rented(), 
                            amount)
            
            total_amount += amount

        # footer: summary of charges
        statement += "\n"
        statement += "{:40s}  {:6s} {:6.2f}\n".format(
                       "Total Charges", "", total_amount)
        statement += "Frequent Renter Points earned: {}\n".format(frequent_renter_points)

        return statement
    

    def get_price(self, rental: Rental):
        """Calculate the price for a given rental."""
        amount = 0
        if rental.get_movie().get_price_code() == Movie.REGULAR:
            amount = 2.0
            if rental.get_days_rented() > 2:
                amount += 1.5 * (rental.get_days_rented() - 2)
        elif rental.get_movie().get_price_code() == Movie.CHILDRENS:
            amount = 1.5
            if rental.get_days_rented() > 3:
                amount += 1.5 * (rental.get_days_rented() - 3)
        elif rental.get_movie().get_price_code() == Movie.NEW_RELEASE:
            amount = 3 * rental.get_days_rented()
        return amount
