import logging
import sys
from pathlib import Path

# Add parent directory to path so we can import library_manager
sys.path.insert(0, str(Path(__file__).parent.parent))

from library_manager.inventory import LibraryInventory
from library_manager.book import Book

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def main():
    inventory = LibraryInventory()
    
    while True:
        print("\nLibrary Inventory Manager")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Search Book")
        print("6. Exit")
        
        try:
            choice = input("Choose an option: ").strip()
            
            if choice == '1':
                title = input("Title: ").strip()
                author = input("Author: ").strip()
                isbn = input("ISBN: ").strip()
                if title and author and isbn:
                    book = Book(title, author, isbn)
                    inventory.add_book(book)
                    print("Book added")
                else:
                    print("All fields required")
            
            elif choice == '2':
                isbn = input("ISBN to issue: ").strip()
                book = inventory.search_by_isbn(isbn)
                if book and book.is_available():
                    book.issue()
                    inventory.save_books()
                    print("Book issued")
                else:
                    print("Book not available or not found")
            
            elif choice == '3':
                isbn = input("ISBN to return: ").strip()
                book = inventory.search_by_isbn(isbn)
                if book:
                    book.return_book()
                    inventory.save_books()
                    print("Book returned")
                else:
                    print("Book not found")
            
            elif choice == '4':
                inventory.display_all()
            
            elif choice == '5':
                query = input("Search by title or ISBN: ").strip()
                if query.isdigit():
                    book = inventory.search_by_isbn(query)
                    if book:
                        print(book)
                    else:
                        print("Not found")
                else:
                    results = inventory.search_by_title(query)
                    if results:
                        for book in results:
                            print(book)
                    else:
                        print("No matches")
            
            elif choice == '6':
                print("Exiting")
                break
            
            else:
                print("Invalid choice")
        
        except Exception as e:
            logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()