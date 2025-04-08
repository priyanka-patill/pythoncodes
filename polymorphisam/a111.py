# Define the Book class
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_details(self):
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.year}")

# Create instances of the Book class
book1 = Book("ABC", "xyz", 1962)
book2 = Book("pqr", "LMM", 2001)

# Call the method to display details of the books
book1.display_details()
book2.display_details()
