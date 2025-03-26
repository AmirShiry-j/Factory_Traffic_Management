from UsersRepository import UsersRepository
    
class AccountManagerService:
    
    def __init__(self):  
        self.__usersRepository=UsersRepository

    def RegisterNewUser(self,FirstName,LastName,NationalCode):
        self.__usersRepository.Insert(FirstName,LastName,NationalCode)
        hasNationalCode=self.__usersRepository.CheckHasNationalCodeBefore(NationalCode)
        if(hasNationalCode==False):
            return True,"کاربر با موفقیت ثبت شد"
        else:
            return False,"این کد ملی قبلا ثبت شده"



