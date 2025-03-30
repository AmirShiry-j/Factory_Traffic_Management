from Utilities.UI_Helper import UI_Helper
from Utilities.PromptManager import PromptManager

uI_Helper=UI_Helper()
promptManager=PromptManager()

isYes = True

while isYes:
    #clear screen
    promptManager.ClearScreen()
    #say hello
    promptManager.SayHello()
    #show menu
    promptManager.ShowMenu()
    #take work number
    (isSuccessTakeWorkNumber,WorkNumber) = promptManager.TakeWorkNumber()
    if isSuccessTakeWorkNumber==True:
        match  WorkNumber:
            case 1:
                print("1")
            case 2:#show list users                
                promptManager.ShowListUsers()
    else: 
        pass
    #Ask to conuinue
    isYes = promptManager.ShowPromptWantToContinueYesOrNo()
    
promptManager.Exist()


