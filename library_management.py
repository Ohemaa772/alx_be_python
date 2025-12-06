class Book:
    def __init__(self, title, author):
        self.title = title          # public
        self.author = author        # public
        self._is_checked_out = False  # private attribute

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Make the book available again."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is currently available."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []   # private list of Book objects

    def add_book(self, book):
        """Add a Book object to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by its title."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    return f"'{title}' checked out successfully."
                return f"'{title}' is already checked out."
        return f"Book titled '{title}' not found."

    def return_book(self, title):
        """Return a book by its title."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    return f"'{title}' returned successfully."
                return f"'{title}' was not checked out."
        return f"Book titled '{title}' not found."

    def list_available_books(self):
        """Print a list of all available books."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")