from Repositories.UsersRepository import UsersRepository
    
class AccountManagerService:
    
    def __init__(self):  
        self.__usersRepository=UsersRepository()

    def RegisterNewUser(self,FirstName,LastName,NationalCode):
        hasNationalCode=self.__usersRepository.CheckHasNationalCodeBefore(NationalCode)
        if(hasNationalCode==False):
            self.__usersRepository.Insert(FirstName,LastName,NationalCode)
            return (True,"User successfully registered.")
        else:
            return (False,"This national code has already been registered.")

    def GetAllUsers(self):
        users=self.__usersRepository.GetAllUsers()
        return users
    
    def DeleteUserByUserId(self,UserId):
        #Get user from db
        
        #check exist
        user=self.__usersRepository.GetUserByUserId(UserId)
        if (user is None):
            return (False,f"User with ID {UserId} does not exist.")
        
        #check exist histories of user 
        userHasAnyHistory = self.__usersRepository.CheckUserHasAnyHistory(UserId)
        if(userHasAnyHistory):
            return (False,"The user has a registered history. It cannot be deleted.")
        
        #Delete user
        self.__usersRepository.DeleteByUserId(UserId)
        return (True,"User Deleted.")
            
    def DeleteUserByNationalCode(self,NationalCode):
        #Get user from db
        
        #check exist
        user=self.__usersRepository.GetUserByNationalCode(NationalCode)
        if (user is None):
            return (False,f"User with national code {NationalCode} does not exist.")
        
        #check exist histories of user 
        userHasAnyHistory = self.__usersRepository.CheckUserHasAnyHistory(NationalCode)
        if(userHasAnyHistory):
            return (False,"The user has a registered history. It cannot be deleted.")
        
        #Delete user
        self.__usersRepository.DeleteByNationalCode(NationalCode)
        return (True,"User Deleted.")
            


