import sys
import os
from Services.AccountManagerService import AccountManagerService
from Services.TaradodService import TaradodService
from Utilities.UI_Helper import UI_Helper
from Services.DateConverter import DateConverter
from Services.JalaliDateRanges import JalaliDateRanges

class PromptManager:
    
    def __init__(self):  
        self.listWorkNumbers=(0,1,2,3,4,5,6)
        self.__MaxCountTry=3
        self.__accountManagerService=AccountManagerService()
        self.__taradodService=TaradodService()
        self.__dateConverter=DateConverter()
        self.__uI_Helper=UI_Helper(self.__MaxCountTry)
        self.__jalaliDateRanges=JalaliDateRanges()

    def ShowPromptWantToContinueYesOrNo(self):
        return self.__uI_Helper.get_answer_Continue_input()
    
    def Exist(self):
        print()
        print("The program is over.")
        sys.exit()
    
    def ClearScreen(self):
        os.system('cls' if os.name=='nt' else 'clear')
    
    def SayHello(self):
        self.ClearScreen()
        print("Hello, welcome to the employee traffic management program ! :)")


    def ShowMenu(self):
        
        print("What are you planning to do?")
        print("This is our menu")
        print()
        print("1 - Reporting of entry and exit")
        print("2 - Registering of entry and exit")
        print("3 - View the list of users")
        print("4 - New user registration")
        print("5 - Edit user information")
        print("6 - Delete user information")
        print("0 - Exit")

            
    def TakeWorkNumber(self):
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
        firstName= self.__uI_Helper.get_firstName_input()
        print()
        lastName= self.__uI_Helper.get_lastName_input()
        print()
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
        print()
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
        print()
        firstName= self.__uI_Helper.get_firstName_input()
        print()
        lastName= self.__uI_Helper.get_lastName_input()
        print()
        
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

        (isSuccessWhen,whenDateNumber)=self.__uI_Helper.get_WhenDate_for_RegisterTaradod_input()
        if isSuccessWhen==False:
            return

        year = month = day = 0
        match whenDateNumber:
            case 1:
                (year,month,day)=self.__dateConverter.GetTodayShamsi()
            case 2:
                (year,month,day)=self.__dateConverter.GetYesterdayShamsi()
            case 3:
                print()
                (isSuccessDate,year,month,day)=self.__uI_Helper.get_shamsi_date_from_input()
                if isSuccessDate==False:
                    return

        
        print()
        (isSuccessNatio,nationalCode)=self.__uI_Helper.get_NationalCode_from_input()
        if isSuccessNatio==False:
            return

        print()
        
        (isSuccessArrivalTime,ArHour,ArMinute)=self.__uI_Helper.get_time_from_input("Arrival")
        if isSuccessArrivalTime==False:
            return
        
        print()

        (isSuccessDepartureTime,DeHour,DeMinute)=self.__uI_Helper.get_time_from_input("Departure")
        if isSuccessDepartureTime==False:
            return

        (isSuccessReg,messageReg) = self.__taradodService.RegisterTaradod(nationalCode,year,month,day,ArHour,ArMinute,DeHour,DeMinute)
        print()
        print(messageReg)


    def Report(self):
        self.ClearScreen()
        numberOfQestionsRemaining=self.__MaxCountTry

        print("You have entered the Report process ...")
        print()

        (isSuccessNatio,nationalCode)=self.__uI_Helper.get_NationalCode_from_input()
        if isSuccessNatio==False:
            return

        print()

        (isSuccessWhen,whenDateNumber)=self.__uI_Helper.get_WhenDate_for_report_input()
        if isSuccessWhen==False:
            return

        start_unix= end_unix = 0
        match whenDateNumber:
            case 1:#this month
                (start_unix, end_unix)=self.__jalaliDateRanges.this_month()
            case 2:#last month
                (start_unix, end_unix)=self.__jalaliDateRanges.last_month()
            case 3:#this year
                (start_unix, end_unix)=self.__jalaliDateRanges.this_year()
            case 4:#last year
                (start_unix, end_unix)=self.__jalaliDateRanges.last_year()
            case 5:#baze zamani
                print()
                (isSuccessStartDate,start_year , start_month, start_day)=self.__uI_Helper.get_shamsi_date_with_title_from_input("Start")
                if isSuccessStartDate==False:
                    return
                print()
                (isSuccessEndDate,end_year, end_month, end_day)=self.__uI_Helper.get_shamsi_date_with_title_from_input("End")
                if isSuccessEndDate==False:
                    return
                (start_unix, end_unix)=self.__jalaliDateRanges.custom_range_unix(start_day,start_month,start_year,end_day, end_month, end_year)
                
        print()
        
        (isSuccessReport,messageReport,records,sumKarkards) = self.__taradodService.GetReportForOneUser(nationalCode,start_unix,end_unix)
        print()
        if isSuccessReport==False:
            print(messageReport)
        else:
            self.ClearScreen()
            self.__uI_Helper.ShowReport(records,sumKarkards)