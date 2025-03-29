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

    def DeleteByUserId(self,UserId):
        conn=sqlite3.connect(self.__db_Name)
        cursor=conn.cursor()
        cursor.execute("PRAGMA foreign_keys = ON ")
        cursor.execute("DELETE from users where id="+str(UserId))
        conn.commit()   
        conn.close()

    def CheckUserHasAnyHistory(self,UserId):
        conn=sqlite3.connect(self.__db_Name)
        cursor=conn.cursor()
        cursor.execute(f"select count(*) from Taradods where UserId='{UserId}'")
        count=cursor.fetchone()[0]
        conn.close()

        return count>0
    
    
    def GetUserByUserId(self,UserId):
        conn=sqlite3.connect(self.__db_Name)
        cursor=conn.cursor()
        cursor.execute(f"select Id,FirstName,LastName,NationalCode from Users where id="+str(UserId))
        row=cursor.fetchone()
        return row
    
    def GetUserByNationalCode(self,NationalCode):
        conn=sqlite3.connect(self.__db_Name)
        cursor=conn.cursor()
        cursor.execute(f"select Id,FirstName,LastName,NationalCode from Users where NationalCode="+str(NationalCode))
        row=cursor.fetchone()
        return row

    def DeleteByNationalCode(self,NationalCode):
        conn=sqlite3.connect(self.__db_Name)
        cursor=conn.cursor()
        cursor.execute("PRAGMA foreign_keys = ON ")
        cursor.execute("DELETE from users where NationalCode="+str(NationalCode))
        conn.commit()   
        conn.close()