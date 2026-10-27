# Menu for book_library.py.
from book_library import Book, Library

def main():
    """Creating an interface"""

    library = Library()
    library.load_from_file('books.json')

    while True: # Menu
        print("\n1. Add book")
        print("2. Find by author")
        print("3. Show unread")
        print("4. Mark as read")
        print("5. Exit")

        choice = input("Select an action: ")

        if choice == '1':
            """Add a book"""
            title = input("Name: ").lower()
            author = input("Author: ").lower()
            year = input("Year: ")
            book = Book(title, author, year)
            library.add_book(book)
            print("The book has been added!")

        elif choice == '2':
            """Find by author"""
            author = input("Author: ")
            books = library.find_by_author(author)
            if books:
                for book in books:
                    print(book)
            else:
                print("No books found")

        elif choice == '3':
            """Show unread"""
            unread = library.unread_books()

            if unread:
                print("Unread books: ")
                for book in unread:
                    print(book)
            else:
                print("There are no unread books.")

        elif choice == '4':
            """Mark as read"""
            title = input("Enter the title of the book: ").lower()

            found = False
            for book in library.books:
                if book.title.lower() == title:
                    book.mark_as_read()
                    print(f"The book '{book.title}' is marked as read")
                    found = True
                    break
            if not found:
                print("Book not found.")

        else:
            """Exit"""
            library.save_to_file('books.json')
            print("Saved. Goodbye!")
            break

                    
if __name__ == '__main__':
    main()
