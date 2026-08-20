class Book:
    def __init__(self, author: str, title: str, book_id: int, is_borrowed: bool):
        self.author = author
        self.title = title
        self.book_id = book_id
        self.is_borrowed = is_borrowed

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "id": self.book_id,
            "is_borrowed": self.is_borrowed
        }
