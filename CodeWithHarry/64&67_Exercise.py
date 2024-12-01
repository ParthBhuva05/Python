# Exercise_6: Library Management System in Python

# write a library class with no_of_books and books as two instance variables.write a program to create a library from this library class and show how you can print all books, add a book and get the number of books using different method. show that your program doesn't persist the books after the program is stopped! 



class Library:
    def __init__(self):
        self.numberOfBooks = 0
        self.books = []

    def addBook(self, book):
        self.books.append(book)
        self.numberOfBooks = len(self.books)

    def shoeInfo(self):
        print(f"The library has {self.numberOfBooks} books")
        print(f"The books are----------")
        for book in self.books:
            print(book)


library1 = Library()
library1.addBook("Harry Potter1")
library1.addBook("Harry Potter2")
library1.addBook("Harry Potter3")
library1.shoeInfo()