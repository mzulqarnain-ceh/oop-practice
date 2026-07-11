from abc import ABC,abstractmethod
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def introduce(self):
        print(f"My name is {self.name} and i am {self.age} years old")
class Member(Person):
    def __init__(self,name,age,member_id,borrowed_books=None):
        super().__init__(name,age)
        self.member_id=member_id
        self.__borrowed_books=borrowed_books or []
    @property
    def borrowed_books(self):
        return self.__borrowed_books
    @borrowed_books.setter
    def borrowed_books(self,value):
        self.__borrowed_books=value
    def borrow_book(self,book):
        if len(self.__borrowed_books)>=3:
            print(f"{self.name} limit Exceeded")
        else:
            self.__borrowed_books.append(book)
    def remove_book(self,book):
        self.__borrowed_books.remove(book)
    def show_books(self):
        print(f"Borrowed Books: {[book.title for book in self.__borrowed_books]}")
    def __str__(self):
        return f"Name: {self.name} | Age: {self.age} | Member_ID: {self.member_id} | Borrowed Books: {self.__borrowed_books}"
class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.__is_available = True
    @property
    def is_available(self):
        return self.__is_available
    def checkout(self):
        self.__is_available = False
    def checkin(self):
        self.__is_available = True
    def __str__(self):
        return f"Book Name is {self.title} and Author is {self.author}"
class AbstractLibrary(ABC):
    @abstractmethod
    def add_book(self):
        pass
    @abstractmethod
    def remove_book(self):
        pass
    @abstractmethod
    def search_book(self):
        pass
class Library(AbstractLibrary):
    def __init__(self,library_name,books=None):
        self.library_name=library_name
        self.__books=books or []
    def add_book(self,book):
        self.__books.append(book)
    def remove_book(self,title):
        for book in self.__books:
            if book.title==title:
                self.__books.remove(book)
                print(f"{book.title} removed")
                return
        print("Book Not Found")
    def search_book(self,title):
        for book in self.__books:
            if book.title==title:
                print(book)
                return
        print("Book not Found")
    def lend_book(self,title,member):
        for book in self.__books:
            if book.title==title:
                if book.is_available:
                    book.checkout()
                    member.borrow_book(book)
                    print(f"{title} mil gyi ha {member.name} ko ")
                else:
                    print(f"{title} abi available nai ha ")
                return
        print("Book library mein nahi hai")
    def accept_return(self,title,member):
        for book in self.__books:
            if book.title==title:
                book.checkin()
                member.remove_book(book)
                print(f"{title} returned to library")
                return
        print("This book is not from this library")
    def __len__(self):
        return len(self.__books)
    @classmethod
    def create_library(cls,name):
        return cls(name)
    @staticmethod
    def library_info():
        print("Library Working Hours: 9AM - 5PM")
    def __str__(self):
        book_list=", ".join([book.title for book in self.__books])
        return f"Library: {self.library_name} | Books: {book_list}"
# Library banao
lib = Library.create_library("City Library")
Library.library_info()
print(lib)

# Books banao aur add karo
b1 = Book("Python Basics", "Ali Ahmed")
b2 = Book("OOP Concepts", "Sara Khan")
b3 = Book("Data Structures", "Umar Farooq")
lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)
print(lib)        # library info
print(len(lib))   # total books

# Member banao
m1 = Member("Haider", 20, "M001")
m1.introduce()

# Book lend karo
lib.lend_book("Python Basics", m1)
m1.show_books()

# Book wapas karo
lib.accept_return("Python Basics", m1)
m1.show_books()

# Search karo
lib.search_book("OOP Concepts")
lib.search_book("AI Book")  # Not found