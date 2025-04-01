from Repositories.TaradodsRepository import TaradodsRepository

class TaradodService:

    def __init__(self):
        self.__taradodsRepository = TaradodsRepository()

    def RegisterNewTaradod(self, UserId, Year, Month, Day, ArrivalTimeUnix, DepartureTimeUnix):
        # check exist recore
        existing_taradod = self.__taradodsRepository.GetTaradod(UserId, Year, Month, Day)
        if existing_taradod is not None:
            return (False, "A record for this date and user already exists.")
        
        # insert
        self.__taradodsRepository.Insert(UserId, Year, Month, Day, ArrivalTimeUnix, DepartureTimeUnix)
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
