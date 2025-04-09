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
    
    
    def GetReportForOneUser(self, UserId, start_unix,end_unix):
        conn = sqlite3.connect(self.__db_Name)
        cursor = conn.cursor()
        cursor.execute("PRAGMA foreign_keys = ON") 

        cursor.execute("""
            with first_infoes as (
                       
            select t.year,t.month,t.day,t.ArrivalTimeUnix,t.DepartureTimeUnix, (t.DepartureTimeUnix - t.ArrivalTimeUnix) as duration_unix
            from Taradods t
            where t.UserId=? and (t.ArrivalTimeUnix>=? and t.DepartureTimeUnix<=?) 
                       
                       )

            select c.year,c.month,c.day,
                        time(c.ArrivalTimeUnix, 'unixepoch') AS ArrivalTime , 
                       time(c.DepartureTimeUnix, 'unixepoch') AS DepartureTime,
                       
                       time(c.duration_unix, 'unixepoch') AS duration,
                       c.duration_unix
                       
            from first_infoes c
            order by c.ArrivalTimeUnix
            

        """, (UserId, start_unix,end_unix))
        rows=cursor.fetchall()
        conn.commit()
        conn.close() 

        totalDurtionUnix = sum(item[6] for item in rows)

        return rows,self.format_seconds(totalDurtionUnix)
    
    def format_seconds(self,seconds):
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        remaining_seconds = seconds % 60
        return f"{hours}:{minutes:02}:{remaining_seconds:02}"