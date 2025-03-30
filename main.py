from Utilities.UI_Helper import UI_Helper
from Utilities.PromptManager import PromptManager

uI_Helper=UI_Helper()
promptManager=PromptManager()

#say hello
promptManager.SayHello()

isYes = True

while isYes:
    #show menu
    promptManager.ShowMenu()
    #take work number
    (isSuccessTakeWorkNumber,WorkNumber) = promptManager.TakeWorkNumber()
    if isSuccessTakeWorkNumber==True:
        match  WorkNumber:
            case 1:#Register new user
                promptManager.RegisterNewUser()

            case 2:#show list users                
                promptManager.ShowListUsers()
    else: 
        pass
    #Ask to conuinue
    isYes = promptManager.ShowPromptWantToContinueYesOrNo()
    
    if isYes:
        #clear screen
        promptManager.ClearScreen()
    
promptManager.Exist()


