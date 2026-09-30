class Book:
    def __init__(self,title,author,is_available):
        self.title = title
        self.author = author
        self.is_available = is_available
        
        
    def display_book(self):
        print("Title:",self.title)
        print("Author:",self.author)
        print("Available:",self.is_available)
        
        
    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            print(f"'{self.title}' has been borrowed.")
        else:
            print(f"'{self.title}' is not available for borrowing.")

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print(f"'{self.title}' has been returned.")
        else:
            print(f"'{self.title}' was not borrowed.")
            
            
book1 = Book("The Great Gatsby","F. Scott Fitzgerald",True)
book2 = Book("To Kill a Mockingbird","Harper Lee",True)
book3 = Book("1984","George Orwell",False)

books = [book1, book2, book3]

for book in books:
    book.display_book()
    
    
book1.borrow_book()
book1.borrow_book()
book2.borrow_book()
book1.return_book()
for book in books:
    book.display_book()
