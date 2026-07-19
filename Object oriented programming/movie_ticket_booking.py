class MovieTicket:

    def __init__(self):
        self.movies = {}

    def add_movie(self, movie, price):
        if movie in self.movies:
            print("Movie already exists.")
        else:
            self.movies[movie] = price
            print(f"{movie} has been added.")

    def remove_movie(self, movie):
        if movie in self.movies:
            del self.movies[movie]
            print(f"{movie} has been removed.")
        else:
            print("Movie not found.")

    def search_movie(self):
        movie = input("Enter movie name: ")

        if movie in self.movies:
            print("\nMovie Found")
            print(f"Movie : {movie}")
            print(f"Ticket Price : Rs.{self.movies[movie]}")
        else:
            print("Movie not available.")

    def display_movies(self):
        if not self.movies:
            print("No movies available.")
            return

        print("\n----- MOVIE LIST -----")
        for movie, price in self.movies.items():
            print(f"Movie : {movie}")
            print(f"Ticket Price : Rs.{price}")
            print()

    def book_ticket(self):
        movie = input("Enter movie name: ")

        if movie in self.movies:
            tickets = int(input("Enter number of tickets: "))
            total = tickets * self.movies[movie]

            print("\n----- BOOKING DETAILS -----")
            print(f"Movie : {movie}")
            print(f"Tickets : {tickets}")
            print(f"Total Amount : Rs.{total}")
            print("Booking Successful!")
        else:
            print("Movie not available.")


ticket = MovieTicket()

while True:

    print("\n===== Movie Ticket Booking System =====")
    print("1. Add Movie")
    print("2. Remove Movie")
    print("3. Search Movie")
    print("4. Display Movies")
    print("5. Book Ticket")
    print("6. Exit")

    option = int(input("Enter your choice: "))

    if option == 1:
        movie = input("Enter movie name: ")
        price = int(input("Enter ticket price: "))
        ticket.add_movie(movie, price)

    elif option == 2:
        movie = input("Enter movie name: ")
        ticket.remove_movie(movie)

    elif option == 3:
        ticket.search_movie()

    elif option == 4:
        ticket.display_movies()

    elif option == 5:
        ticket.book_ticket()

    elif option == 6:
        print("Thank you for using Movie Ticket Booking System.")
        break

    else:
        print("Invalid choice.")