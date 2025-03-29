from AccountManagerService import AccountManagerService
from UI_Utility import UI_Utility

managerService = AccountManagerService()
uI_Utility=UI_Utility()

(isSuccess,message)=managerService.DeleteUserByUserId(3)
print(str(isSuccess)+" "+message)


users=managerService.GetAllUsers()
uI_Utility.ShowUsers(users)




