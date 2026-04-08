# Test book_library.py.
import unittest
from book_project import Book, Library
import os


class BookTest(unittest.TestCase):
    """Test class Book."""

    def setUp(self):
        self.new_book = Book('crime and punishment',
                             'dostoevsky', 1866, read=False)

    def test_mark_as_read(self):
        """Test mark as read."""
        self.new_book.mark_as_read()
        self.assertEqual(self.new_book.read, True)

    def test_get_info(self):
        """Test get information."""
        info = self.new_book.get_info()
        self.assertEqual(info, 'crime and punishment, Dostoevsky, 1866')


class LibraryTest(unittest.TestCase):
    """Test class Library."""

    def setUp(self):
        self.library = Library()
        self.book1 = Book('crime and punishment', 'dostoevsky', 1866)
        self.book2 = Book('1984', 'orwell', 1949)
        self.book3 = Book('idiot', 'dostoevsky', 1869)
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        self.library.add_book(self.book3)

    def test_add_book(self):
        """Test add book in library."""
        self.library.books = [] # Cleaning setUp library
        count = len(self.library.books)
        new_book = Book('crime and punishment', 'dostoevsky', 1866)
        self.library.add_book(new_book)
        self.assertIn(new_book, self.library.books)
        self.assertEqual(len(self.library.books), count + 1)

    def test_find_by_author(self):
        """Test find_by_author."""
        found = self.library.find_by_author('dostoevsky')
        self.assertEqual(found, ['crime and punishment, Dostoevsky, 1866',
                         'idiot, Dostoevsky, 1869'])
        self.assertEqual(len(found), 2)
        found = self.library.find_by_author('tolstoy')  # Test not existed author
        self.assertEqual(found, [])

    def test_unread_books(self):
        """Tets unread books list."""
        self.book2.mark_as_read()
        unread = self.library.unread_books()
        self.assertNotIn(self.book2.get_info(), unread)
        self.assertIn(self.book1.get_info(), unread)
        self.assertIn(self.book3.get_info(), unread)

    def test_save_and_load(self):
        """Test save and load to file."""

        self.library.save_to_file('test_books.json')
        # creating new library and loading
        new_library = Library()
        new_library.load_from_file('test_books.json')
        # check how many books were loaded
        self.assertEqual(len(new_library.books), len(self.library.books))
        self.assertEqual(new_library.books[1].title,
                         self.library.books[1].title)
        self.assertEqual(new_library.books[1].author,
                         self.library.books[1].author)

        os.remove('test_books.json')


if __name__ == '__main__':
    unittest.main()
