class UI_Utility:
    
    def __init__(self):  
        pass

    def ShowUsers(self,users):
        print(f"{"UserId".ljust(20)} {"FirstName".ljust(20)} {"LastName".ljust(20)} {"NationalCode".ljust(20)} ")
        for row in users:
            print(f"{str(row[0]).ljust(20)} {str(row[1]).ljust(20)} {str(row[2]).ljust(20)} {str(row[3]).ljust(20)} ")
        if(users is not None and len(users)==0):
            print(f"There is not User")

