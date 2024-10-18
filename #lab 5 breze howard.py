#lab 5 breze howard

#creating class and attributes
class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.read = False

    def description(self):
        print("title:", self.title)
        print("author:", self.author)
        print("pages:", self.pages)
        print()

    def markasread(self):
        self.read = True
        print(f"You've marked '{self.title}' as read.")
    
    def __str__(self):
        return f"{self.title} - {self.author} - {self.pages}"
    
#create two book objects
book1 = Book("Pride and Prejudice", "Jane Austen", 432)
book2 = Book("Moby-Dick", "Herman Melville", 635)

#printing descriptions
print(book1.description())
print(book2.description())

#mark first book as read
book1.markasread()

#part 2 - creating class and attributes to buy the books, view the purchased books, and mark books as already read
class EbookReader():
    def __init__(self):
        self.availablebooks = [
            Book("Pride and Prejudice", "Jane Austen", 432),
            Book("Moby-Dick", "Herman Melville", 635),
            Book("The Adventures of Sherlock Holmes", "Arthur Conan Doyle", 307),
            Book("Frankenstein", "Mary Shelley", 280)
        ]
        self.purchasedbooks = []

    def buybook(self, title):
        for book in self.availablebooks:
            if book.title.lower() == title.lower():
                self.purchasedbooks.append(book)
                print(f"You have purchased '{book.title}'.")
                return
        print("Book not found.")

    def viewpurchasedbooks(self):
        if not self.purchasedbooks:
            print("You have no purchased books.")
            return
        print("Your purchased books:")
        for book in self.purchasedbooks:
            print(book.description())

    def readbook(self, title):
        for book in self.purchasedbooks:
            if book.title.lower() == title.lower():
                if not book.read:
                    book.markasread()
                else:
                    print(f"You have already read '{book.title}'.")
                return
        print("Book not found in your purchases.")

#example
reader = EbookReader()

#buying books
reader.buybook("Pride and Prejudice")
reader.buybook("Moby-Dick")

#view purchased books
reader.viewpurchasedbooks()

#reading a book
reader.readbook("Pride and Prejudice")

#reading the same book again
reader.readbook("Pride and Prejudice")