# Task Manager API
from flask import Flask,jsonify,request
import sqlite3,os
app=Flask(__name__)
# database setup
def get_db():
    folder=os.path.dirname(__file__)
    path=os.path.join(folder,"Task_Manager_API.db")
    conn=sqlite3.connect(path)
    conn.row_factory=sqlite3.Row
    return conn
def create_table():
    conn=get_db()
    conn.execute("CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, status TEXT DEFAULT 'pending')")
    conn.commit()
    conn.close()
# Routes
# Home Page
@app.route("/")
def home():
    pass
# Get all tasks
@app.route("/tasks",methods=["GET"])
def get_all_tasks():
    pass
# Get a specific task
@app.route("/tasks/<int:id>",methods=["GET"])
def get_task(id):
    pass
# Add a task
@app.route("/tasks",methods=["POST"])
def add_task():
    pass
# Update a task
@app.route("/tasks/<int:id>",methods=["PUT"])
def update_task(id):
    pass
# Delete a task
@app.route("/tasks/<int:id>",methods=["DELETE"])
def delete_task(id):
    pass
# Entry point
if __name__=="__main__":
    create_table()
    # app.run(debug=True)