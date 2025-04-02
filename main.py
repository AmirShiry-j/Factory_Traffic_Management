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
            case 1:#Register Taradod
                promptManager.RegisterTaradod()

            case 2:#show list users                
                promptManager.ShowListUsers()

            case 3:#Register new user
                promptManager.RegisterNewUser()

            case 4:#Update user
                promptManager.UpdateUser()

            case 5:#Delete user
                promptManager.DeleteUser()

            case 0:#Delete user
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


