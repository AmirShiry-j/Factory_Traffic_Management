from AccountManagerService import AccountManagerService

managerService = AccountManagerService()

(isSuccess,message)=managerService.RegisterNewUser("Am433443ir55","333","455445")

rows=managerService.GetAllUsers()

print(f"{"UserId".ljust(20)} {"FirstName".ljust(20)} {"LastName".ljust(20)} {"NationalCode".ljust(20)} ")
for row in rows:
   print(f"{str(row[0]).ljust(20)} {str(row[1]).ljust(20)} {str(row[2]).ljust(20)} {str(row[3]).ljust(20)} ")




