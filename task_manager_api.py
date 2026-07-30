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
    return jsonify({"message":"welcome to home page of task manager api",
    "routes":{
     "GET /tasks":"Get all tasks",
     "GET /tasks/<id>":"Get a specific task",
     "POST /tasks":"Add a new task",
     "PUT /tasks/<id>":"Update a task",
     "DELETE /tasks/<id>":"Delete a task",
     "GET /tasks/pending":"Get all pending tasks"   
    }
    })
# Get all tasks
@app.route("/tasks",methods=["GET"])
def get_all_tasks():
    conn=get_db()
    tasks=conn.execute("SELECT * FROM tasks").fetchall()
    conn.close()
    tasks_list=[{"id":task["id"], "title":task["title"],"status":task["status"]} for task in tasks]
    return jsonify(tasks_list)
# Get a specific task
@app.route("/tasks/<int:id>",methods=["GET"])
def get_task(id):
    conn=get_db()
    task=conn.execute("SELECT * FROM tasks WHERE id=?",(id,)).fetchone()
    conn.close()
    if task is None:
        return jsonify({"error":"task not found"}),404
    return jsonify({"id":task["id"],"title":task["title"],"status":task["status"]}),200
# Add a task
@app.route("/tasks",methods=["POST"])
def add_task():
    data=request.get_json()
    if not data or "title" not in data:
        return jsonify({"message":"title must be required"}),400
    conn=get_db()
    conn.execute("INSERT INTO tasks(title) VALUES(?)",(data["title"],))
    conn.commit()
    conn.close()
    return jsonify({"message":"task added successfully"}),201
# Update a task
@app.route("/tasks/<int:id>",methods=["PUT"])
def update_task(id):
    data=request.get_json()
    if not data or "status" not in data:
        return jsonify({"message":"status value required either completed or not"}),400
    conn=get_db()
    task=conn.execute("SELECT * FROM tasks WHERE id=?",(id,)).fetchone()
    if task is None:
        conn.close()
        return jsonify({"error":"task not found"}),404
    conn.execute("UPDATE tasks SET status=? WHERE id=?",(data["status"],id))
    conn.commit()
    conn.close()
    return jsonify({"message":"task updated successfully"})
# Delete a task
@app.route("/tasks/<int:id>",methods=["DELETE"])
def delete_task(id):
    conn=get_db()
    task=conn.execute("SELECT * FROM tasks WHERE id=?",(id,)).fetchone()
    if task is None:
        conn.close()
        return jsonify({"error":"task not found"}),404
    conn.execute("DELETE FROM tasks WHERE id=?",(id,))
    conn.commit()
    conn.close()
    return jsonify({"message":"task deleted successfully"})
# Get all pending tasks
@app.route("/tasks/pending",methods=["GET"])
def get_all_pending_tasks():
    conn=get_db()
    tasks=conn.execute("SELECT * FROM tasks WHERE status='pending'").fetchall()
    conn.close()
    if len(tasks)==0:
        return jsonify({"message":"no pending tasks are available, all tasks are completed"})
    pending_tasks=[{"id":task["id"],"title":task["title"],"status":task["status"]} for task in tasks]
    return jsonify(pending_tasks)
# Entry point
if __name__=="__main__":
    create_table()
    app.run(debug=True)