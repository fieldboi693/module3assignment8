def add_book(library, book):
    if book not in library:
        library.append(book)
        print(f"Book '{book[0]}' by {book[1]} added to the library.")
    else:
        print(f"Book '{book[0]}' by {book[1]} already exists in the library.")

# Example usage
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

# Add a new book
add_book(library, ("Fahrenheit 451", "Ray Bradbury"))

# Attempt to add a duplicate book
add_book(library, ("1984", "George Orwell"))

# View updated library
print(library)