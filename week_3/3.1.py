class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f'{self.title} by {self.author}'
    
    def is_long_read(self):
        return self.pages > 300
    

book = Book("War and Peace", "Leo Tolstoy", 1225)
print(book)
print(book.is_long_read())

algebra = Book("Algebra", "Michael Artin", 200)
print(algebra)
print(algebra.is_long_read())