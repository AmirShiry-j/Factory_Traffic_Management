import sqlite3

class UsersRepository:    

    def __init__(self):  
        self.__db_Name="Taradod_Db.db"

    def Insert(self,FirstName,LastName,NationalCode):
        conn=sqlite3.connect(self.__db_Name)
        cursor=conn.cursor()
        cursor.execute("PRAGMA foreign_keys = ON ")
        cursor.execute("insert into users(FirstName,LastName,NationalCode) values (?,?,?)",(FirstName,LastName,NationalCode))
        conn.commit()   
        conn.close()

    def CheckHasNationalCodeBefore(self,NationalCode):
        conn=sqlite3.connect(self.__db_Name)
        cursor=conn.cursor()
        cursor.execute(f"select count(*) from users where NationalCode='{NationalCode}'")
        count=cursor.fetchone()[0]
        conn.close()

        return count>0
    
    def GetAllUsers(self):
        conn=sqlite3.connect(self.__db_Name)
        cursor=conn.cursor()
        cursor.execute(f"select Id,FirstName,LastName,NationalCode from Users")
        rows=cursor.fetchall()
        return rows
