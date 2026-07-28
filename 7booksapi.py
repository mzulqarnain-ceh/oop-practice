from flask import Flask,jsonify,request
import sqlite3,os
app=Flask(__name__)
# database setup
def get_db():
    folder=os.path.dirname(__file__)
    path=os.path.join(folder,"Books_api.db")
    conn=sqlite3.connect(path)
    conn.row_factory=sqlite3.Row
    return conn
def create_table():
    conn=get_db()
    conn.execute("CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY AUTOINCREMENT,title TEXT NOT NULL,author TEXT NOT NULL)")
    conn.commit()
    conn.close()
# Routes
@app.route("/")
def home():
    return jsonify({"message":"Welcome to Books api",
    "routes":{
        "GET /books":"Get all books",
        "GET /books/<id>":"Get specific book",
        "POST /books":"Add book",
        "PUT /books/<id>":"Update a book",
        "DELETE /books/<id>":"Delete a book"
        }
    })
@app.route("/books",methods=["GET"])
def get_all_books():
    conn=get_db()
    books=conn.execute("SELECT * FROM books").fetchall()
    book_list=[{"id":book["id"],"title":book["title"],"author":book["author"]} for book in books]
    return jsonify(book_list)
@app.route("/books/<int:id>",methods=["GET"])
def get_book(id):
    conn=get_db()
    book=conn.execute("SELECT * FROM books WHERE id=?",(id,)).fetchone()
    conn.close()
    if book is None:
        return jsonify({"Error":"Book Not Found"}),404
    return jsonify({"id":book["id"], "title":book["title"],"author":book["author"]})
@app.route("/books",methods=["POST"])
def add_book():
    data=request.get_json()
    if not data or "title" not in data or "author" not in data:
        return jsonify({"Error": "Title and author are required"}),400
    conn=get_db()
    conn.execute("INSERT INTO books (title,author) VALUES(?,?)",(data["title"],data["author"]))
    conn.commit()
    conn.close()
    return jsonify({"message":"Book Added Successfully"}),201
@app.route("/books/<int:id>",methods=["PUT"])
def update_book(id):
    data=request.get_json()
    if not data or "title" not in data or "author" not in data:
        return jsonify({"Error":"Title and author are required"}),400
    conn=get_db()
    book=conn.execute("SELECT * FROM books WHERE id=?",(id,)).fetchone()
    if book is None:
        conn.close()
        return jsonify({"Error":"Book Not Found"}),404
    conn.execute("UPDATE books SET title=?,author=? WHERE id=?",(data["title"],data["author"],id))
    conn.commit()
    conn.close()
    return jsonify({"Message":"Book updated successfully"})
@app.route("/books/<int:id>",methods=["DELETE"])
def delete_book(id):
    conn=get_db()
    book=conn.execute("SELECT * FROM books WHERE id=?",(id,)).fetchone()
    if book is None:
        return jsonify({"Error":"Book not found"}),404
    conn.execute("DELETE FROM books WHERE id=?",(id,))
    conn.commit()
    conn.close()
    return jsonify({"Message":"Book deleted successfully"})
if __name__=="__main__":
    create_table()
    app.run(debug=True)


# Book add krny k lye
# $body = @{ title = "Python Basics"; author = "Ali" } | ConvertTo-Json
# Invoke-RestMethod -Method Post -Uri http://127.0.0.1:5000/books -ContentType "application/json" -Body $body
# book update krny k lye, id change kr lena jis ko update krna ha aur title aur name b set kr lena
# $body = @{ title = "New Book Name"; author = "New Author" } | ConvertTo-Json
# Invoke-RestMethod -Method Put -Uri http://127.0.0.1:5000/books/1 -ContentType "application/json" -Body $body
# book delete krnay k lye,id change kr lena 
# Invoke-RestMethod -Method Delete -Uri http://127.0.0.1:5000/books/1