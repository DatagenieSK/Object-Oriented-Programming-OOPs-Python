#aggregation = represents a relationship where one object ( the whole)
#contains reference to one or more INDEPENDENT objects (the parts)


class Liabrary:
    def __init__(self, name):
        self.name = name
        self.books = []
    def add_book(self,book):
        self.books.append(book)
    def list_book(self):
        return {f"{book.title} by {book.author}" for book in self.books}
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


liab = Liabrary("National liabrary")

book1 = Book("Harry Potter", "j.k Rowling")

book2 = Book("the habbit", "J.R.R")


liab.add_book(book1)
liab.add_book(book2)

print(liab.name)
print(liab.list_book())

#better format

for book in liab.list_book():
    print(book)