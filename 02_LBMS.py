# Library Book Management System
import json
import os
folder=os.path.dirname(__file__)
path=os.path.join(folder, "Books.json")
def save_data():
    with open(path ,"w") as f:
        json.dump(books,f,indent=2)
def load_data():
    try:
        with open(path, "r") as f:
            return json.load(f)
    except (FileNotFoundError , json.JSONDecodeError):
        return []
books=load_data()
def add_book():
    try:
        book_id=int(input("Enter Book ID: "))
    except ValueError:
        print("Please enter a valid Book Id")
        return
    if book_id in [b["Book_id"] for b in books]:
        print("Book already exists")
        return
    title=input("Enter the title of book: ")
    author=input("Enter the name of author: ")
    try:
        quantity=int(input("Enter the quantity of book: "))
    except ValueError:
        print("Please enter a valid quantity")
        return
    books.append({"Book_id": book_id, "Title": title, "Author": author, "Quantity": quantity})
    save_data()
    print("Book added successfully")
def view_book():
    if len(books)==0:
        print("No Book Found")
    else:
        for b in books:
            print(f"Book ID: {b['Book_id']} | Book Title: {b['Title']} | Author: {b['Author']} | Quantity: {b['Quantity']}")
def edit_book():
    try:
        book_id=int(input("Enter the Id of book you want to edit: "))
    except ValueError:
        print("Please enter a valid Book id")
        return
    for b in books:
        if b['Book_id']==book_id:
            b['Title']=input("Enter the title of book: ")
            b['Author']=input("Enter the name of author: ")
            b['Quantity']=int(input("Enter the quantity of book: "))
            save_data()
            print("Book updated successfully")
            return
    print("Book Not Found")
def delete_book():
    try:
        book_id=int(input("Enter the id of the book you want to delete: "))
    except ValueError:
        print("Please enter a valid Book id")
        return
    for b in books:
        if b['Book_id']==book_id:
            books.remove(b)
            save_data()
            print("Book deleted successfully")
            return
    print("Book Not Found")
def issue_book():
    try:
        book_id=int(input("Enter the Book id you want to issue: "))
    except ValueError:
        print("Please enter a valid Book id")
        return
    for b in books:
        if b['Book_id']==book_id:
            if b['Quantity']>0:
                b['Quantity']-=1
                save_data()
                print("Book Issued Successfully")
                return
            else:
                print("Book not available")
            return
    print("Book Not Found")
def return_book():
    try:
        book_id=int(input("Enter the Book id you want to return: "))
    except ValueError:
        print("Please enter a valid Book id")
        return
    for b in books:
        if b['Book_id']==book_id:
            b['Quantity']+=1
            save_data()
            print("Returned Successfully")
            return
    print("Book Not Found")
# Menu
while True:
    print("""
          1. Add Book
          2. View Books
          3. Edit Book
          4. Delete Book
          5. Issue Book
          6. Return Book
          7. Exit """)
    try:
        choice=int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid choice")
        continue
    if choice==1:
        add_book()
    elif choice==2:
        view_book()
    elif choice==3:
        edit_book()
    elif choice==4:
        delete_book()
    elif choice==5:
        issue_book()
    elif choice==6:
        return_book()
    elif choice==7:
        break
    else:
        print("Please enter a valid choice between 1-7")