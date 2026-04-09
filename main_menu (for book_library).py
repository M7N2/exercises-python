from book_library import Book, Library

def main():
    """Создание интерфейса"""

    library = Library()
    library.load_from_file('books.json')

    while True: # Menu
        print("\n1. Добавить книгу")
        print("2. Найти по автору")
        print("3. Показать непрочитанные")
        print("4. Отметить как прочитанную")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            """Добавить книгу"""
            title = input("Название: ").lower()
            author = input("Автор: ").lower()
            year = input("Год: ")
            book = Book(title, author, year)
            library.add_book(book)
            print("Книга добавлена!")

        elif choice == '2':
            """Найти по автору"""
            author = input("Автор: ")
            books = library.find_by_author(author)
            if books:
                for book in books:
                    print(book)
            else:
                print("Книги не найдены")

        elif choice == '3':
            """Показать непрочитанные"""
            unread = library.unread_books()

            if unread:
                print("Непрочитанные книги: ")
                for book in unread:
                    print(book)
            else:
                print("Нет непрочитанных книг.")

        elif choice == '4':
            """Отметить как прочитанную"""
            title = input("Введите название книги: ").lower()

            found = False
            for book in library.books:
                if book.title.lower() == title:
                    book.mark_as_read()
                    print(f"Книга '{book.title}' отмечена как прочитанная")
                    found = True
                    break
            if not found:
                print("Книга не найдена.")

        else:
            """Выход"""
            library.save_to_file('books.json')
            print("Сохранено. До свидания!")
            break

                    
if __name__ == '__main__':
    main()
