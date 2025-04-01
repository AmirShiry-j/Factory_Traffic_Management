import sqlite3
import os

class TaradodsRepository:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))  #Current route
        tempPath = os.path.join(base_dir, "Taradod_Db.db")
        self.__db_Name = tempPath.replace("Repositories","DataBaseFiles")

    def Insert(self, UserId, Year, Month, Day, ArrivalTimeUnix, DepartureTimeUnix):
        conn = sqlite3.connect(self.__db_Name)
        cursor = conn.cursor()
        cursor.execute("PRAGMA foreign_keys = ON") 

        cursor.execute("""
            INSERT INTO Taradods (UserId, Year, Month, Day, ArrivalTimeUnix, DepartureTimeUnix) 
            VALUES (?, ?, ?, ?, ?, ?)
        """, (UserId, Year, Month, Day, ArrivalTimeUnix, DepartureTimeUnix))

        conn.commit()
        conn.close() 

    def Update(self, Id, Year, Month, Day, ArrivalTimeUnix, DepartureTimeUnix):
        conn = sqlite3.connect(self.__db_Name)
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE Taradods 
            SET Year = ?, Month = ?, Day = ?, ArrivalTimeUnix = ?, DepartureTimeUnix = ? 
            WHERE Id = ?
        """, (Year, Month, Day, ArrivalTimeUnix, DepartureTimeUnix, Id))

        conn.commit()
        conn.close()
        
    def DeleteById(self,Id):
        conn=sqlite3.connect(self.__db_Name)
        cursor=conn.cursor()
        cursor.execute("PRAGMA foreign_keys = ON ")
        cursor.execute("DELETE from Taradods where id="+str(Id))
        conn.commit()   
        conn.close()

    def GetTaradod(self, UserId, Year, Month, Day):
        conn = sqlite3.connect(self.__db_Name)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM Taradods 
            WHERE UserId = ? AND Year = ? AND Month = ? AND Day = ?
        """, (UserId, Year, Month, Day))

        record = cursor.fetchone()

        conn.close()
        return record 