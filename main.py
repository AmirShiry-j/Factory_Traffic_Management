from Services.AccountManagerService import AccountManagerService
from Utilities.UI_Utility import UI_Utility

managerService = AccountManagerService()
uI_Utility=UI_Utility()

# (isSuccess,message)=managerService.DeleteUserByNationalCode(3920934121)
# print(str(isSuccess)+" "+message)


# users=managerService.GetAllUsers()
# uI_Utility.ShowUsers(users)

uI_Utility.ShowPromtYesNo()


