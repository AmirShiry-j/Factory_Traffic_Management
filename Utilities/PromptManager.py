import sys

class PromptManager:
    
    def __init__(self):  
        self.listWorkNumbers=(1,2)
        self.__MaxAskQueation=4

    def ShowPromptWantToContinueYesOrNo(self):
        numberOfQestionsRemaining=self.__MaxAskQueation

        while(numberOfQestionsRemaining>0):

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
        print("The program is over.")
        sys.exit()
    
    def ShowMenu(self):
        print("1 - Register new User")
        print("2 - List Users")
        print()
            
    def TakeWorkNumber(self):
        numberOfQestionsRemaining=self.__MaxAskQueation
        strWorkNumber=""
        workNumberIsValid=False

        while(workNumberIsValid==False and numberOfQestionsRemaining>0):
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