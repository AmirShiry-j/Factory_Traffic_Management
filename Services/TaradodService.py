from Repositories.TaradodsRepository import TaradodsRepository
from Repositories.UsersRepository import UsersRepository
from Services.DateConverter import DateConverter

class TaradodService:

    def __init__(self):
        self.__taradodsRepository = TaradodsRepository()
        self.__usersRepository = UsersRepository()
        self.__dateConverter = DateConverter()

    def RegisterTaradod(self, NationalCode, Year, Month, Day, ArHour, ArMinute , DeHour , DeMinute):        
        # check exist recore
        user = self.__usersRepository.GetUserByNationalCode(NationalCode)
        if user is None:
            return (False,f"User with national code {NationalCode} does not exist.")
        
        # check exist recore
        existing_taradod = self.__taradodsRepository.GetTaradod(user[0], Year, Month, Day)
        if existing_taradod is not None:
            return (False, "A record for this date and user already exists.")
        
        #convet shamsi time to unix
        ArrivalTimeUnix = self.__dateConverter.ConvertShamsiToUnix(Year,Month,Day,ArHour,ArMinute)
        DepartureTimeUnix = self.__dateConverter.ConvertShamsiToUnix(Year,Month,Day,DeHour,DeMinute)

        #Checking the reasonableness of Arrival and Departure times
        if not ArrivalTimeUnix<DepartureTimeUnix:
            return (False, "The check-in and check-out times are not reasonable. The check-in time cannot be after the check-out time.")

        # insert
        self.__taradodsRepository.Insert(user[0], Year, Month, Day, ArrivalTimeUnix, DepartureTimeUnix)
        return (True, "Taradod successfully registered.")

    def UpdateTaradod(self, Id, Year, Month, Day, ArrivalTimeUnix, DepartureTimeUnix):
        # check exist recore
        existing_taradod = self.__taradodsRepository.GetTaradodById(Id)
        if existing_taradod is None:
            return (False, f"Taradod with ID {Id} does not exist.")

        # update
        self.__taradodsRepository.Update(Id, Year, Month, Day, ArrivalTimeUnix, DepartureTimeUnix)
        return (True, "Taradod successfully updated.")

    def DeleteTaradodById(self, Id):
        # check exist recore
        existing_taradod = self.__taradodsRepository.GetTaradodById(Id)
        if existing_taradod is None:
            return (False, f"Taradod with ID {Id} does not exist.")
        
        # delete it
        self.__taradodsRepository.DeleteById(Id)
        return (True, "Taradod successfully deleted.")

    def GetTaradod(self, UserId, Year, Month, Day):
        # check exist recore
        taradod = self.__taradodsRepository.GetTaradod(UserId, Year, Month, Day)
        if taradod is None:
            return (False, "No Taradod found for the given user and date.")
        
        return (True, taradod)
    
    
    def GetReportForOneUser(self, NationalCode, start_unix,end_unix):        
        # check exist recore
        user = self.__usersRepository.GetUserByNationalCode(NationalCode)
        if user is None:
            return (False,f"User with national code {NationalCode} does not exist.",None)
        
        #Checking the reasonableness of Dates times
        if not start_unix<end_unix:
            return (False, "The start and exit dates are not reasonable. The start date cannot be after the end date.",None)

        # get gozaresh from db
        result= self.__taradodsRepository.GetReportForOneUser(user[0], start_unix, end_unix)
        return (True, "",result)




