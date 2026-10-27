import json

class Book():
    """Class book."""

    def __init__(self, title, author, year, read=False):
        self.title = title
        self.author = author
        self.year = year
        self.read = read

    def mark_as_read(self):
        """Mark as read."""
        self.read = True

    def get_info(self):
        """Show info."""
        book_info = f"{self.title}, {self.author.title()}, {self.year}"
        return book_info


class Library():
    """Library of books."""

    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Add book."""
        self.books.append(book)

    def find_by_author(self, author):
        """Search by author."""
        found_books = []
        for book in self.books:
            if author.lower() in book.author.lower():
                found_books.append(book.get_info())
        return found_books
        
    def unread_books(self):
        """List of unread books."""
        unread_books = []
        for book in self.books:
            if not book.read:
                unread_books.append(book.get_info())
        return unread_books
        
    def save_to_file(self, filename):
        """Save books to file"""
        books_data = []
        for book in self.books:
            books_data.append({
                'title': book.title,
                'author': book.author,
                'year': book.year,
                'read': book.read
                })

        with open (filename, 'w') as f:
            json.dump(books_data, f)

    def load_from_file(self, filename):
        """Load file."""
        try:
            with open(filename) as f:
                books_data = json.load(f)
            self.books = []
        
            for book_data in books_data:
                book = Book(
                    title=book_data['title'],
                    author=book_data['author'],
                    year=book_data['year'],
                    read=book_data['read']
                    )
                self.books.append(book)

        except FileNotFoundError:
            self.books = []
