import sys
import os
from Services.AccountManagerService import AccountManagerService
from Utilities.UI_Helper import UI_Helper

class PromptManager:
    
    def __init__(self):  
        self.listWorkNumbers=(1,2)
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
        print()
        print("Hello , Welcome to this App")


    def ShowMenu(self):
        print()
        print("This is our menu")
        print()
        print("1 - Register new User")
        print("2 - List Users")
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
                print("The work number entered was not valid.")
                
        return False,0
    
    def ShowListUsers(self):
        self.ClearScreen()
        users=self.__accountManagerService.GetAllUsers()
        self.__uI_Helper.ShowUsers(users)