# library_system.py

class Book:
    """Base class for all books."""
    def __init__(self, title, author):
        # Store title and author for every book
        self.title = title
        self.author = author

    def __str__(self):
        # Human-friendly string used by print()
        return f"{self.title} by {self.author}"


class EBook(Book):
    """Derived class for electronic books (inherits from Book)."""
    def __init__(self, title, author, file_size):
        # Call base class constructor to set title and author
        super().__init__(title, author)
        # Initialize the extra attribute for ebooks
        self.file_size = file_size  # in MB (integer)

    def __str__(self):
        # Extend the base string to include file size
        return f"{self.title} by {self.author} - File Size: {self.file_size}MB"


class PrintBook(Book):
    """Derived class for print books (inherits from Book)."""
    def __init__(self, title, author, page_count):
        # Call base class constructor to set title and author
        super().__init__(title, author)
        # Initialize the extra attribute for print books
        self.page_count = page_count  # integer number of pages

    def __str__(self):
        # Extend the base string to include page count
        return f"{self.title} by {self.author} - Pages: {self.page_count}"


class Library:
    """Composition: Library has a collection of Book objects."""
    def __init__(self):
        # Start with an empty list of books
        self.books = []

    def add_book(self, book):
        # Add a Book (or EBook/PrintBook) instance to the library
        self.books.append(book)

    def list_books(self):
        # Print details of each book; handle empty library
        if not self.books:
            print("Library is empty.")
            return

        for index, book in enumerate(self.books, start=1):
            # Using the book's __str__ for readable output
            print(f"{index}. {book}")
