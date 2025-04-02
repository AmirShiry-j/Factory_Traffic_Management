import sys
import os
from Services.AccountManagerService import AccountManagerService
from Services.TaradodService import TaradodService
from Utilities.UI_Helper import UI_Helper

class PromptManager:
    
    def __init__(self):  
        self.listWorkNumbers=(1,2,3,4,5)
        self.__MaxCountTry=2
        self.__accountManagerService=AccountManagerService()
        self.__taradodService=TaradodService()
        self.__uI_Helper=UI_Helper(self.__MaxCountTry)

    def ShowPromptWantToContinueYesOrNo(self):
        numberOfQestionsRemaining=self.__MaxCountTry

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
        print("1 - Register Taradod")
        print("2 - List Users")
        print("3 - Register new User")
        print("4 - Update User")
        print("5 - Delete User")

            
    def TakeWorkNumber(self):
        print()
        (isSuccess,workNumber) = self.__uI_Helper.get_WorkNumber_from_input(self.listWorkNumbers)
        return isSuccess,workNumber

    def ShowListUsers(self):
        self.ClearScreen()
        users=self.__accountManagerService.GetAllUsers()
        self.__uI_Helper.ShowUsers(users)

    def RegisterNewUser(self):
        self.ClearScreen()
        print("Worker or employee information form ...")
        print()
        firstName= input("Enter FirstName :  ")
        lastName= input("Enter LastName :  ")
        (isSuccessNatio,nationalCode)=self.__uI_Helper.get_NationalCode_from_input()
        if isSuccessNatio==False:
            return
        (isSuccess,message)=self.__accountManagerService.RegisterNewUser(firstName,lastName,nationalCode)
        print()
        print(message)

    def DeleteUser(self):
        self.ClearScreen()
        print("You have entered the user deletion process ...")
        print()

        (isSuccessWay,wayNumber)=self.__uI_Helper.get_WayNumberForDeleteUser_from_input()
        if isSuccessWay==False:
            return

        if wayNumber==1:
            (isSuccessUserId,userId)=self.__uI_Helper.get_UserId_from_input()
            if isSuccessUserId==False:
                return
            (isSuccess,message) = self.__accountManagerService.DeleteUserByUserId(userId)
            print()
            print(message)
            return
        
        else:
            (isSuccessNatio,nationalCode)=self.__uI_Helper.get_NationalCode_from_input()
            if isSuccessNatio==False:
                return
            
            (isSuccess,message) = self.__accountManagerService.DeleteUserByNationalCode(nationalCode)
            print()
            print(message)
            return
       

    
    def UpdateUser(self):
        self.ClearScreen()
        numberOfQestionsRemaining=self.__MaxCountTry

        print("You have entered the user updatation process ...")
        print()
        
        (isSuccessUserId,userId)=self.__uI_Helper.get_UserId_from_input()
        if isSuccessUserId==False:
            return

        firstName= input("Enter FirstName :  ")
        lastName= input("Enter LastName :  ")

        (isSuccessNatio,nationalCode)=self.__uI_Helper.get_NationalCode_from_input()
        if isSuccessNatio==False:
            return
        
        (isSuccess,message)=self.__accountManagerService.UpdateUser(userId,firstName,lastName,nationalCode)
        print()
        print(message)

    def RegisterTaradod(self):
        self.ClearScreen()
        numberOfQestionsRemaining=self.__MaxCountTry

        print("You have entered the taradod register  process ...")
        print()

        (isSuccessNatio,nationalCode)=self.__uI_Helper.get_NationalCode_from_input()
        if isSuccessNatio==False:
            return
        
        (isSuccessDate,year,month,day)=self.__uI_Helper.get_shamsi_date_from_input()
        if isSuccessDate==False:
            return

        (isSuccessArrivalTime,ArHour,ArMinute)=self.__uI_Helper.get_time_from_input("Arrival")
        if isSuccessArrivalTime==False:
            return
          
        (isSuccessDepartureTime,DeHour,DeMinute)=self.__uI_Helper.get_time_from_input("Departure")
        if isSuccessDepartureTime==False:
            return
        
        (isSuccessReg,messageReg) = self.__taradodService.RegisterTaradod(nationalCode,year,month,day,ArHour,ArMinute,DeHour,DeMinute)
        print()
        print(messageReg)