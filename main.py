from AccountManagerService import AccountManagerService
from UI_Utility import UI_Utility

managerService = AccountManagerService()
uI_Utility=UI_Utility()

(isSuccess,message)=managerService.RegisterNewUser("Am433443ir55","333","455445")

users=managerService.GetAllUsers()
uI_Utility.ShowUsers(users)




