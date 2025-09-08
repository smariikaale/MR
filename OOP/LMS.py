#Library Management System:
#Classes: Book, Library. Add methods to add_book, remove_book, search_book. Use inheritance for different book types (e.g., EBook).

class Book:
    def __init__(self,name,author,genre):
        self.name=name
        self.author=author
        self.genre=genre
    def __str__(self):
        return f"{self.name} is being called."
    
class Ebook(Book):
    def __init__(self,name,author,genre,file_size):
        # self.name=name
        # self.author=author
        # self.genre=genre
        super().__init__(name,author,genre)
        self.file_size=file_size

class Library:
    books=[]
    def add_book(self,book):
        self.books.append(book.name)
        print(self.books)
    def remove_book(self,book):
        for i in self.books:
            if i==book:
                print("Book is found")
                print(self.books)
                self.books.remove(book)
                print("Book is removed")
                print(self.books)
                break
            else:
                print("Book not found")
    def search_book(self,book):
        for i in self.books:
            if i==book:
                print(f"Book is found at index {self.books.index(book)}")
                
                break
            else:
                print("Book not found")

book1=Book("Verity","Collen Hoover","Thriller")
print(book1)
ebook1=Ebook("The Kite Runner","Khaled Hossini","Historical Fiction","10mb")
print(ebook1)

l1=Library()
l1.add_book(book1)
l1.add_book(ebook1)

book_name=input("Enter the book name to remove:")
l1.remove_book(book_name)

book_name=input("Enter the book name to search:")
l1.search_book(book_name)
