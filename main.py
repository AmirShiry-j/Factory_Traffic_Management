from Utilities.UI_Helper import UI_Helper
from Utilities.PromptManager import PromptManager

promptManager=PromptManager()

#say hello
promptManager.SayHello()

isYes = True

while isYes:
    #show menu
    print()
    promptManager.ShowMenu()

    print()
    #take work number
    (isSuccessTakeWorkNumber,WorkNumber) = promptManager.TakeWorkNumber()
    if isSuccessTakeWorkNumber==True:
        match  WorkNumber:
            case 1:
                promptManager.Report()

            case 2:      
                promptManager.RegisterTaradod()

            case 3:
                promptManager.ShowListUsers()
                
            case 4:
                promptManager.RegisterNewUser()
                
            case 5:
                promptManager.UpdateUser()
                
            case 6:
                promptManager.DeleteUser()

            case 0:
                promptManager.Exist()
    else: 
        pass
    #Ask to conuinue
    print()
    isYes = promptManager.ShowPromptWantToContinueYesOrNo()
    
    if isYes:
        #clear screen
        promptManager.ClearScreen()
    

promptManager.Exist()


