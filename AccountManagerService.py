from UsersRepository import UsersRepository
    
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



