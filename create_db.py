import sqlite3

conn=sqlite3.connect("Taradod_Db.db")
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

# cursor.execute("""
# alter table Users add constraint Nathonal_Code unique(NationalCode);
# """)


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