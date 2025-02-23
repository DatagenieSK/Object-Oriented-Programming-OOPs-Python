'''
magic method = Dunder method (double underscore) __init__, __str__, __eq__,
               They are aitomatically called by many of python's built-in operations.
               they allow developer to define or customize the behavior of objects
'''

class Book:

    def __init__(self,title,author,num_pages):
        self.title = title
        self.author = author
        self.numpages = num_pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.numpages < other.numpages
    def __gt__(self, other):
        return self.numpages > other.numpages

    def __add__(self, other):
        return self.numpages + other.numpages

    def __sub__(self, other):
        return self.numpages - other.numpages
    def __contains__(self, item):
        return item in self.title or item in self.author

    def __getitem__(self, item):
        if item == "title":
            return self.title
        elif item == "author":
            return self.author
        elif item == "pages":
            return  self.numpages

        else:
            return f"{item} not found"





book1 = Book("Harry Potter", "J.K. Rowling", 223)
book2 = Book("the Hobbit", "J.R.R", 310)


print(book1)
print(book1 == book2)
print(book2 < book1)
print(book2 > book1)
print(book2 + book1)
print(book2 - book1)
print("Harry" in book1)
print(book1["title"])
print(book1["author"])
print(book1["pages"])


