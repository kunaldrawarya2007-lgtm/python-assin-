import logging

class LibraryInventory:
    def __init__(self, filename='books.txt'):
        self.filename = filename
        self.books = []
        self.load_books()

    def load_books(self):
        try:
            with open(self.filename, 'r') as f:
                for line in f:
                    parts = line.strip().split(',')
                    if len(parts) == 4:
                        title, author, isbn, status = parts
                        self.books.append(Book(title, author, isbn, status))
        except FileNotFoundError:
            logging.info("No existing catalog found, starting fresh")
        except Exception as e:
            logging.error(f"Error loading catalog: {e}")
            self.books = []

    def save_books(self):
        try:
            with open(self.filename, 'w') as f:
                for book in self.books:
                    f.write(f"{book.title},{book.author},{book.isbn},{book.status}\n")
        except Exception as e:
            logging.error(f"Failed to save catalog: {e}")

    def add_book(self, book):
        self.books.append(book)
        self.save_books()

    def search_by_title(self, title):
        return [book for book in self.books if title.lower() in book.title.lower()]

    def search_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def display_all(self):
        if not self.books:
            print("No books in inventory")
        for book in self.books:
            print(book)