from AccountManagerService import AccountManagerService

managerService = AccountManagerService()

(isSuccess,message)=managerService.RegisterNewUser("Am433443ir55","333","455445")

print(isSuccess,message)



# cursor.execute("insert into users(FirstName,LastName) values (?,?)",("Amir","Shiry"))
# cursor.execute("insert into users(FirstName,LastName) values (?,?)",("Hossein","Rezaei"))
# cursor.execute("insert into Taradods(UserId,ArrivalTime,DepartureTime,Date) values (?,?,?,?)",(2,"2022-03-29 12:12:12","2022-03-29 12:12:12","2022-03-29"))

# conn.commit()   

# cursor.execute("select * from users")
# rows=cursor.fetchall()
# for row in rows:
#     print(row)

# print("  ")
# cursor.execute("select * from Taradods")
# rows=cursor.fetchall()
# for row in rows:
#     print(row)


