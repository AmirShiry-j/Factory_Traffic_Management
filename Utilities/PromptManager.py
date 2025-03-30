import sys
import os
from Services.AccountManagerService import AccountManagerService
from Utilities.UI_Helper import UI_Helper

class PromptManager:
    
    def __init__(self):  
        self.listWorkNumbers=(1,2,3)
        self.__MaxAskQueation=2
        self.__accountManagerService=AccountManagerService()
        self.__uI_Helper=UI_Helper()

    def ShowPromptWantToContinueYesOrNo(self):
        numberOfQestionsRemaining=self.__MaxAskQueation

        while(numberOfQestionsRemaining>0):

            print()
            strPrompt=input("Do you want to continue? (Yes/No)   :    ")
            strPrompt=strPrompt.lower()
            numberOfQestionsRemaining=numberOfQestionsRemaining-1

            if (strPrompt=="yes"):
                return True
            elif (strPrompt=="no"):
                return False
            else:
                print("The answer was unclear.")

        return False
    
    def Exist(self):
        print()
        print("The program is over.")
        sys.exit()
    
    def ClearScreen(self):
        os.system('cls' if os.name=='nt' else 'clear')
    
    def SayHello(self):
        self.ClearScreen()
        print("Hello , Welcome to this App")


    def ShowMenu(self):
        print()
        print("This is our work menu")
        print()
        print("1 - Register new User")
        print("2 - List Users")
        print("3 - Delete User")
        print()
            
    def TakeWorkNumber(self):
        numberOfQestionsRemaining=self.__MaxAskQueation
        strWorkNumber=""
        workNumberIsValid=False

        while(workNumberIsValid==False and numberOfQestionsRemaining>0):
            print()
            strWorkNumber = input("What do you want? Enter a Work Number  :  ")
            numberOfQestionsRemaining=numberOfQestionsRemaining-1
            
            if(strWorkNumber.isdigit()==False):
                print("The answer was unclear.")
                continue
            workNumber=int(strWorkNumber)
            #check WorkNumber is part of the menu list 
            numberIsExist = workNumber in self.listWorkNumbers
            if(numberIsExist==True):
                return True,workNumber
            else:
                print("The entered work number is not in the list..")
                continue
                
        return False,0
    
    def ShowListUsers(self):
        self.ClearScreen()
        users=self.__accountManagerService.GetAllUsers()
        self.__uI_Helper.ShowUsers(users)

    def RegisterNewUser(self):
        self.ClearScreen()
        print("Worker or employee information form ...")
        firstName= input("Enter FirstName :  ")
        lastName= input("Enter FirstName :  ")
        nationalCode= input("Enter NationalCode :  ")
        (isSuccess,message)=self.__accountManagerService.RegisterNewUser(firstName,lastName,nationalCode)
        print()
        print(message)

    def DeleteUser(self):
        self.ClearScreen()
        print("You have entered the user deletion process ...")
        print()
        print("How do you want to delete the user? Delete by ID or delete by national code.")
        print("choose one")
        print("1 - Delete by ID")
        print("2 - Delete by national code")

        numberOfQestionsRemaining=self.__MaxAskQueation
        strWayNumber=""
        wayNumberIsValid=False
        
        while(wayNumberIsValid==False and numberOfQestionsRemaining>0):
            print()
            strWayNumber=input("Enter the desired option number  :  ")
            numberOfQestionsRemaining=numberOfQestionsRemaining-1
            
            if(strWayNumber.isdigit()==False):
                print("The answer was unclear.")
                continue

            wayNumber=int(strWayNumber)
            #check WayNumber is part of the menu list 
            validWayNumberIsExist = wayNumber in (1,2)

            if(validWayNumberIsExist==True):
                numberOfQestionsRemaining=self.__MaxAskQueation
                
                if wayNumber==1:
                    userID="Do while :)"
                    while(userID.isdigit()==False and numberOfQestionsRemaining>0):
                        numberOfQestionsRemaining=numberOfQestionsRemaining-1
                        print()

                        userID=input("Enter ID :  ")
                        if(userID.isdigit()==False):
                            print("The answer was unclear.")
                            continue
                        
                        (isSuccess,message) = self.__accountManagerService.DeleteUserByUserId(userID)
                        print()
                        print(message)
                        return
                else:

                    nationalCode="Do while :)"
                    while(nationalCode.isdigit()==False and numberOfQestionsRemaining>0):
                        numberOfQestionsRemaining=numberOfQestionsRemaining-1
                        print()

                        nationalCode=input("Enter national code :  ")
                        if(nationalCode.isdigit()==False):
                            print("The answer was unclear.")
                            continue

                        (isSuccess,message) = self.__accountManagerService.DeleteUserByNationalCode(nationalCode)
                        print()
                        print(message)
                        return

            else:
                print("The number entered is not one of the options...")
                continue
        return 
