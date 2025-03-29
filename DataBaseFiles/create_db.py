import sqlite3
import os

base_dir = os.path.dirname(os.path.abspath(__file__))  #Current route
db_Name = os.path.join(base_dir, "Taradod_Db.db")
conn=sqlite3.connect(db_Name)
cursor=conn.cursor()


cursor.execute(""" DROP TABLE IF EXISTS Users """)
cursor.execute(""" DROP TABLE IF EXISTS Taradods """)

cursor.execute("""
CREATE TABLE Users (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    NationalCode TEXT NOT NULL,
    UNIQUE(NationalCode)
)
""")


cursor.execute("""
CREATE TABLE Taradods (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    UserId INTEGER NOT NULL,
    ArrivalTime TEXT NOT NULL,
    DepartureTime TEXT NOT NULL,
    Date TEXT NOT NULL,
    FOREIGN KEY (UserId) REFERENCES Users(Id) ON DELETE CASCADE
)
""")

conn.commit()   
conn.close()