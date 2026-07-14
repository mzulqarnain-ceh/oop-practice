# Student Management System
import json
import os
folder=os.path.dirname(__file__)
path=os.path.join(folder, "student.json")
def save_data():
    with open(path,"w") as f:
        json.dump(students,f,indent=2)
def load_data():
    try:
        with open(path,"r") as f:
            return json.load(f)
    except (FileNotFoundError,json.JSONDecodeError):
        return []
students=load_data()
def add_student():
    try:
        roll=int(input("Enter your Roll No: "))
    except ValueError:
        print("Please enter a valid roll no")
        return
    if roll in [s["Roll"] for s in students]:
        print("Student already exists with this roll no")
        return
    name=input("Enter your name: ")
    try:
        class_no=int(input("Enter your class: "))
    except ValueError:
        print("Please enter a valid class_no")
        return
    try:
        marks=int(input("Enter your marks: "))
    except ValueError:
        print("Please enter valid marks")
        return
    students.append({"Roll":roll, "Name":name, "Class":class_no, "Marks":marks})
    save_data()
    print("Student added successfully")
def view_student():
    if len(students)==0:
        print("No student found")
    else:
        for s in students:
            print(f"Roll No: {s['Roll']} | Name: {s['Name']} | Class: {s['Class']} | Marks: {s['Marks']}")
def edit_student():
    roll=int(input("Enter the Roll No of student you want to edit: "))
    for s in students:
        if s['Roll']==roll:
            s['Name']=input("Enter the name: ")
            s['Class']=int(input("Enter the class no: "))
            s['Marks']=int(input("Enter the marks: "))
            save_data()
            print("Student updated successfully")
            return
    print(f"The does not exists of this {roll}")
def delete_student():
    roll=int(input("Enter the roll no of student you want to delete: "))
    for s in students:
        if s['Roll']==roll:
            students.remove(s)
            save_data()
            print("Student deleted successfully")
            return
    print("Student not found")\
# Menu
while True:
    print("""
          1 for add student
          2 for view student
          3 for edit student
          4 for delete student
          5 for exit""")
    try:
        choice=int(input("Enter you choice: "))
    except ValueError:
        print("Please enter a valid choice")
        continue
    if choice==1:
        add_student()
    elif choice==2:
        view_student()
    elif choice==3:
        edit_student()
    elif choice==4:
        delete_student()
    elif choice==5:
        break
    else:
        print("Please enter a valid no between 1-5")