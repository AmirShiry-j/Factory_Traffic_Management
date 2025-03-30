from Services.AccountManagerService import AccountManagerService
from Utilities.UI_Helper import UI_Helper
from Utilities.PromptManager import PromptManager

managerService = AccountManagerService()
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
        print("Works...")
    else: 
        pass
    #Ask to conuinue
    isYes = promptManager.ShowPromptWantToContinueYesOrNo()
    
promptManager.Exist()


