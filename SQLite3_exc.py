import sqlite3
import sys

def printDB():
    try:
        result = theCursor.execute("SELECT ID, FName, LName, Age, Address, Salary, HireDate FROM Employees")
        for row in result:
            print("ID : ",row[0])
            print("FName : ", row[1])
            print("LName : ", row[2])
            print("Age : ", row[3])
            print("Address : ", row[4])
            print("Salary : ", row[5])
            print("HireDate : ", row[6])

    except sqlite3.OperationalError:
        print("Table doesn't exist")
    except:
        print("Couldn't retrieve data from database")


db_conn = sqlite3.connect("test.db")
print("Database created")

theCursor = db_conn.cursor()

db_conn.execute("DROP TABLE IF EXISTS Employees")
db_conn.commit()

try:

    db_conn.execute("CREATE TABLE Employees(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, FName TEXT NOT NULL, LName TEXT NOT NULL, Age INTEGER NOT NULL, Address TEXT, Salary REAL, HireDate TEXT);")
    db_conn.commit()
    print("Table created")
except sqlite3.OperationalError:
    print("Table couldn't be created!")


db_conn.execute("INSERT INTO Employees (FName, LName, Age, Address, Salary, HireDate) "
                "VALUES ('Szymon', 'Janowski', 20, 'Sezamkowa 123', 100000, date('now'))")
db_conn.commit()

printDB()

try:
    db_conn.execute("ALTER TABLE Employees ADD COLUMN 'Image' BLOB DEFAULT NULL")
    db_conn.commit()
except sqlite3.OperationalError:
    print("Table couldn't be Altered")

theCursor.execute("SELECT SQLITE_VERSION()")
print("SQLite Version: ",theCursor.fetchone())

with db_conn:
    db_conn.row_factory = sqlite3.Row
    theCursor = db_conn.cursor()
    theCursor.execute("SELECT * FROM Employees")
    rows = theCursor.fetchall()
    for row in rows:
        print("{} {}".format(row["FName"], row["LName"]))

with open('dump.sql', 'w') as f:
    for line in db_conn.iterdump():
        f.write('%s\n' % line)

db_conn.close()
print("Database closed")





