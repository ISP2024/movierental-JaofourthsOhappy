from movie import Movie
from rental import Rental
from customer import Customer
from pricing import RegularMovie, NewReleaseMovie, ChildrensMovie

def make_movies():
    """Some sample movies."""
    return [
        Movie("Air", RegularMovie()),
        Movie("Oppenheimer", RegularMovie()),
        Movie("Frozen", ChildrensMovie()),
        Movie("Bitconned", NewReleaseMovie()),
        Movie("Particle Fever", RegularMovie())
    ]


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    for movie in make_movies():
        customer.add_rental(Rental(movie, days, movie.price_code))
        days = (days + 2) % 5 + 1
    print(customer.statement())
