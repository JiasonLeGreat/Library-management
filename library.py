import json
import os
from book import Book

class LibraryManager():
    def __init__(self, filename="library_data.json"):
        self.filename = filename
        self.books = self._load_data()

    def _load_data(self):
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []

    def _save_data(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(self.books, file, indent=4)

    def add_book(self, author, title, book_id, is_borrowed):
        if any(book['id'] == book_id for book in self.books):
            print(f"❌ Error: A book with id {id} already exists.")
            return False
        
        new_book = Book(author, title, book_id, is_borrowed)
        self.books.append(new_book.to_dict())
        self._save_data()
        print(f"✅ Success: '{title}' added to the library.")
        return True

    def view_books(self):
        if not self.books:
            print("📭 The library is currently empty.")
            return

        print("\n--- Library Catalog ---")
        for i, book in enumerate(self.books, 1):
            status = "Borrowed" if book['is_borrowed'] else "Available"
            print(f"{i}. Title: {book['title']} | Author: {book['author']} | Id: {book['id']} | Status: [{status}]")

    def borrow_book(self, id: str):
        for book in self.books:
            if book['id'] == id:
                if book['is_borrowed']:
                    print("⚠️ This book is already borrowed.")
                    return
                book['is_borrowed'] = True
                self._save_data()
                print(f"📖 You have successfully borrowed '{book['title']}'.")
                return
        print("❌ Error: Book with that Id not found.")

    def return_book(self, id: str):
        for book in self.books:
            if book['id'] == id:
                if not book['is_borrowed']:
                    print("⚠️ This book was not borrowed.")
                    return
                book['is_borrowed'] = False
                self._save_data()
                print(f"↩️ You have successfully returned '{book['title']}'.")
                return
        print("❌ Error: Book with that Id not found.")
