# Class for Book
class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def display_info(self):
        print(f"Book: {self.title} by {self.author} | Available copies: {self.copies}")

    def borrow(self):
        if self.copies > 0:
            self.copies -= 1
            print(f"You borrowed '{self.title}'.")
        else:
            print(f"Sorry, '{self.title}' is not available.")

    def return_book(self):
        self.copies += 1
        print(f"You returned '{self.title}'.")

# Create book objects
book1 = Book("The Alchemist", "Paulo Coelho", 3)
book2 = Book("Wings of Fire", "A.P.J. Abdul Kalam", 2)

# Interact with books
book1.display_info()
book1.borrow()
book1.display_info()
book1.return_book()
book1.display_info()

book2.borrow()
book2.borrow()
book2.borrow()  # This will show not available
