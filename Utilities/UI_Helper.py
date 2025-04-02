import re

class UI_Helper:
    
    def __init__(self,maxCoutTry):  
        self.__MaxCountTry=maxCoutTry

    
    def get_answer_Continue_input(self):
        maxTry=self.__MaxCountTry
        attempts = 0  

        while attempts < maxTry:
            answer = input("Do you want to continue? (Yes/No)   :    ") 
            answer=answer.lower()
            
            if (answer=="yes"):
                return True
            elif (answer=="no"):
                return False
            else:
                print("The answer was unclear.")
                
            attempts += 1  

        print(f"You have entered a unclear answer {maxTry} times")
        return False

    def ShowUsers(self,users):
        if(users is not None and len(users)==0):
            print(f"There is not User")
            return

        print(f"{"UserId".ljust(20)} {"FirstName".ljust(20)} {"LastName".ljust(20)} {"NationalCode".ljust(20)} ")
        for row in users:
            print(f"{str(row[0]).ljust(20)} {str(row[1]).ljust(20)} {str(row[2]).ljust(20)} {str(row[3]).ljust(20)} ")
        
    def get_time_from_input(self, title):
        maxTry = self.__MaxCountTry

        attempts = 0 
        while attempts < maxTry:
            time_str = input(f"Enter {title} (HH:MM or H:M format): ") 

            # بررسی فرمت با regex (قبول کردن هر دو فرمت HH:MM و H:M)
            if re.match(r"^\d{1,2}:\d{1,2}$", time_str):
                try:
                    hour, minute = map(int, time_str.split(":"))

                    if 0 <= hour <= 23 and 0 <= minute <= 59:
                        return True, hour, minute  

                    else:
                        print("Invalid time. Hour must be between 0-23 and minute must be between 0-59.")
                except ValueError:
                    print("Invalid time format. Please enter hour and minute as numbers.")
            else:
                print("Invalid format. Please enter the time in HH:MM or H:M format.")

            attempts += 1  

        print(f"You have entered invalid input {maxTry} times")
        return False, 0, 0  

    def get_shamsi_date_from_input(self):

        maxTry=self.__MaxCountTry
        attempts = 0  
        while attempts < maxTry:
            date_str = input("Enter shamsi date (YYYY/MM/DD or YYYY/M/D): ")  

            match = re.match(r"(\d{4})/(\d{1,2})/(\d{1,2})", date_str)

            if match:
                year, month, day = map(int, match.groups())

                if 1370 <= year <= 1500 and 1 <= month <= 12 and 1 <= day <= 31:

                    return True,year, month, day
                else:
                    print("Invalid date. Year must be between 1370 and 1500, month between 1 and 12, and day between 1 and 31.")
            else:
                print("Invalid format. Please enter the date in YYYY/MM/DD or YYYY/M/D format.")

            attempts += 1  

        print(f"You have entered invalid input {maxTry} times")
        return False,0,0,0

    def get_NationalCode_from_input(self):
        maxTry=self.__MaxCountTry
        attempts = 0  
        while attempts < maxTry:
            nationalCode_str = input("Enter NationalCode :  ")  

            
            match = re.match(r"^\d{10}$", nationalCode_str)

            if match:
                return True,nationalCode_str

            else:
                print("Invalid format. Please enter a ten-digit number for the national code.")
                
            attempts += 1  

        print(f"You have entered invalid input {maxTry} times")
        return False,""

    def get_WorkNumber_from_input(self,listWorkNumbers):
        maxTry=self.__MaxCountTry
        attempts = 0  
        while attempts < maxTry:
            workNumber_str = input("Enter a Work Number :  ") 
            
            match = re.match(r"^\d+$", workNumber_str)

            if match:
                
                if int(workNumber_str) in listWorkNumbers:
                    workNumber=int(workNumber_str)
                    return True,workNumber
                else:
                    print("The entered work number is not in the list.")
            else:
                print("Invalid format. Please enter a Number in the menu.")
                
            attempts += 1  

        print(f"You have entered invalid input {maxTry} times")
        return False,0
    
    
    def get_UserId_from_input(self):
        maxTry=self.__MaxCountTry
        attempts = 0  
        while attempts < maxTry:
            userId_str = input("Enter ID :  ") 
            
            match = re.match(r"^\d+$", userId_str)
            if match:
                return True,int(userId_str)
            else:
                print("Invalid format. Please enter a valid Number.")
                
            attempts += 1  

        print(f"You have entered invalid input {maxTry} times")
        return False,0
    
    def get_WayNumberForDeleteUser_from_input(self):
        print("How do you want to delete the user? Delete by ID or delete by national code.")
        print("choose one")
        print("1 - Delete by ID")
        print("2 - Delete by national code")
        print()
        maxTry=self.__MaxCountTry
        attempts = 0  
        while attempts < maxTry:
            wayNumber_str = input("Enter the desired option number  :  ") 
            
            match = re.match(r"^\d+$", wayNumber_str)

            if match:
                
                if int(wayNumber_str) in (1,2):
                    wayNumber=int(wayNumber_str)
                    return True,wayNumber
                else:
                    print("The entered number is not in the list.")
            else:
                print("The answer was unclear.")
                
            attempts += 1  

        print(f"You have entered a unclear answer {maxTry} times")
        return False,0
    

    def get_WhenDate_input(self):
        print("When do you plan to register for traffic?")
        print("choose one")
        print("1 - Today")
        print("2 - Yesterday")
        print("3 - Other dates")
        print()

        maxTry=self.__MaxCountTry
        attempts = 0  
        while attempts < maxTry:
            answerNumber_str = input("Enter the desired option number  :  ") 
            
            match = re.match(r"^\d+$", answerNumber_str)

            if match:
                
                if int(answerNumber_str) in (1,2,3):
                    answerNumber=int(answerNumber_str)
                    return True,answerNumber
                else:
                    print("The entered number is not in the list.")
            else:
                print("The answer was unclear.")
                
            attempts += 1  

        print(f"You have entered a unclear answer {maxTry} times")
        return False,0
    
    def get_firstName_input(self):
        firstName= input("Enter FirstName :  ")
        return firstName
        
    def get_lastName_input(self):
        firstName= input("Enter LastName :  ")
        return firstName
    