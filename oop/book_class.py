class Book:
    def __init__(self, title, author, year):
        """Initializes a Book instance with title, author, and year."""
        self.title = title
        self.author = author
        self.year = year
    
    def __del__(self):
        """Prints a message upon object deletion."""
        print(f"Deleting {self.title}")
    
    def __str__(self):
        """Returns a string representation of the Book instance."""
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        """Returns an official string representation of the Book instance."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
from book_class import Book

def main():
    my_book = Book("1984", "George Orwell", 1949)
    print(my_book)

    print(repr(my_book)) 
    del my_book

if __name__ == "__main__":
    main()
