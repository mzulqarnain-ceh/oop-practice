# Expense Tracker
import sqlite3
import os
from datetime import date
folder=os.path.dirname(__file__)
path=os.path.join(folder,"expense.db")
conn=sqlite3.connect(path)
cursor=conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS expense(id INTEGER PRIMARY KEY AUTOINCREMENT, amount REAL,category TEXT,description TEXT,date TEXT)")
# ADD EXPENSE FUNCTION
def add_expense():
    try:
        amount=float(input("Enter the amount/price: "))
        if amount<=0:
            print("Please enter a amount that is greater than 0")
            return
    except ValueError:
        print("Please enter a valid amount/price")
        return
    category=input("Enter the category of expense: ")
    description=input("Enter the description of expense: ")
    if category=="" or description=="":
        print("Category and Description must not be empty")
        return
    today=str(date.today())
    cursor.execute("INSERT INTO expense(amount,category,description,date) values(?,?,?,?)",(amount,category,description,today))
    conn.commit()
    print("Expense Added Successfully!")
def view_all_expenses():
    cursor.execute("SELECT * FROM expense")
    rows=cursor.fetchall()
    if len(rows)==0:
        print("No Expense Found")
    else:
        for r in rows:
            print(f"ID: {r[0]} | Amount: {r[1]} | Category: {r[2]} | Description: {r[3]} | Date: {r[4]}")
def view_category_summary():
    print("Categories available are: ")
    cursor.execute("SELECT DISTINCT category FROM expense")
    rows=cursor.fetchall()
    for r in rows:
        print(r[0])
    cat=input("Enter the category that you want to summarize: ")
    cursor.execute("SELECT category, SUM(amount) FROM expense WHERE category=? GROUP BY category",(cat,))
    rows=cursor.fetchall()
    if len(rows)==0:
        print("No expense found in this category")
    else:
        for r in rows:
            print(f"Category: {r[0]} | Amount: {r[1]}")
def view_monthly_summary():
    cursor.execute("SELECT substr(date,1,7), SUM(amount) FROM expense GROUP BY substr(date,1,7)")
    rows=cursor.fetchall()
    if len(rows)==0:
        print("No Expens found")
    else:
        for r in rows:
            print(f"Month: {r[0]} | Amount: {r[1]}")
def delete_expense():
    try:
        id=int(input("Enter the expense id you want to delete: "))
    except ValueError:
        print("Please enter a valid expense id")
        return
    cursor.execute("SELECT * FROM expense WHERE id=?",(id,))
    row=cursor.fetchone()
    if row is None:
        print(f"No expense found of this id: {id}")
    else:
        cursor.execute("DELETE FROM expense WHERE id=?",(id,))
        conn.commit()
        print("Expense Deleted successfully!")
# Menue
while True:
    print("""
        1 for add expense
        2 for view all expenses
        3 for view category summary
        4 for view monthly summary
        5 for delete expense
        6 for exit""")
    try:
        choice=int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid choice")
        continue
    if choice==1:
        add_expense()
    elif choice==2:
        view_all_expenses()
    elif choice==3:
        view_category_summary()
    elif choice==4:
        view_monthly_summary()
    elif choice==5:
        delete_expense()
    elif choice==6:
        break
    else:
        print("Please enter a number between 1-6")
