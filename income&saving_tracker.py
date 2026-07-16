# Personal Income & Savings Tracker
import sqlite3
import os
from datetime import date
folder=os.path.dirname(__file__)
path=os.path.join(folder,"saving.db")
conn=sqlite3.connect(path)
cursor=conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS expense(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL,
    type TEXT CHECK(type IN ('INCOME', 'EXPENSE')),
    category TEXT,
    date TEXT
)
""")

def add_transaction():
    try:
        amount=float(input("Enter amount: "))
        if amount<=0:
            print("Amount should be greater than 0")
            return
    except ValueError:
        print("Please enter a valid amount")
        return
    type=input("Enter type: income or expense: ").strip().upper()
    if type not in ("INCOME","EXPENSE"):
        print("Type must be income or expense")
        return
    category=input("Enter category: ")
    if category=="":
        print("Category must not be empty")
        return
    today=str(date.today())
    cursor.execute("INSERT INTO expense(amount,type,category,date) VALUES(?,?,?,?)",(amount,type,category,today))
    conn.commit()
    print("Transaction added successfully!")
def view_all_transactions():
    cursor.execute("SELECT * FROM expense")
    rows=cursor.fetchall()
    if len(rows)==0:
        print("No transaction found")
    else:
        for r in rows:
            print(f"ID: {r[0]} | Amount: {r[1]} | type: {r[2]} | category: {r[3]} | date: {r[4]}")
def view_balance():
    cursor.execute(""" 
            SELECT
                SUM(CASE WHEN type='INCOME' THEN amount ELSE 0 END) AS total_imcome,
                SUM(CASE WHEN type='EXPENSE' THEN amount ELSE 0 END) AS total_expense
            FROM expense""")
    result=cursor.fetchone()
    total_income=result[0] or 0
    total_expense=result[1] or 0
    current_balance=total_income-total_expense
    print("Total Income: ", total_income)
    print("Total Expense: ", total_expense)
    print("Current Balance: ", current_balance)
def view_monthly_report():
    cursor.execute("""
        SELECT
            SUBSTR(date, 1, 7) AS month,
            SUM(CASE WHEN type = 'INCOME' THEN amount ELSE 0 END) AS total_income,
            SUM(CASE WHEN type = 'EXPENSE' THEN amount ELSE 0 END) AS total_expense
        FROM expense
        GROUP BY SUBSTR(date, 1, 7)
        ORDER BY month
    """)

    rows = cursor.fetchall()

    for month, total_income, total_expense in rows:
        print(f"{month} | Income: {total_income} | Expense: {total_expense}")
def delete_transaction():
    try:
        id=int(input("Enter the transaction id you want to delete: "))
    except ValueError:
        print("Please enter a valid id")
        return
    cursor.execute("SELECT * FROM expense WHERE id=?",(id,))
    row=cursor.fetchone()
    if row is None:
        print("No transaction id found")
    else:
        cursor.execute("DELETE FROM expense WHERE id=?",(id,))
        conn.commit()
        print(f"Transaction with id: {id} deleted successfully")
while True:
    print("""
    1 for add transaction
    2 for view all transactions
    3 for view balance
    4 for view monthly report
    5 for delete transaction
    6 for exit""")
    try:
        choice=int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid choice")
        continue
    if choice==1:
        add_transaction()
    elif choice==2:
        view_all_transactions()
    elif choice==3:
        view_balance()
    elif choice==4:
        view_monthly_report()
    elif choice==5:
        delete_transaction()
    elif choice==6:
        break
    else:
        print("Please enter a number between 1-6")
conn.close()