import re

class UI_Helper:
    
    def __init__(self):  
        self.__MaxCountTry=2


    def ShowUsers(self,users):
        if(users is not None and len(users)==0):
            print(f"There is not User")
            return

        print(f"{"UserId".ljust(20)} {"FirstName".ljust(20)} {"LastName".ljust(20)} {"NationalCode".ljust(20)} ")
        for row in users:
            print(f"{str(row[0]).ljust(20)} {str(row[1]).ljust(20)} {str(row[2]).ljust(20)} {str(row[3]).ljust(20)} ")
        
    def get_time_from_input(self,title):
        maxTry=self.__MaxCountTry
        attempts = 0  # شمارنده تلاش‌های ناموفق
        while attempts < maxTry:
            print()
            time_str = input(f"Enter {title} (HH:MM format): ")  # گرفتن زمان به فرمت HH:MM
            # بررسی فرمت ورودی
            if len(time_str) == 5 and time_str[2] == ":":
                try:
                    hour, minute = map(int, time_str.split(":"))  # جدا کردن ساعت و دقیقه
                    # بررسی صحت ساعت و دقیقه
                    if 0 <= hour <= 23 and 0 <= minute <= 59:
                        return True,hour, minute
                        # return True,time_str
                    
                    else:
                        print("Invalid time. Hour must be between 0-23 and minute must be between 0-59.")
                except ValueError:
                    print("Invalid time format. Please enter hour and minute as numbers.")
            else:
                print("Invalid format. Please enter the time in HH:MM format.")

            attempts += 1  # افزایش شمارنده تلاش‌های ناموفق

        print(f"You have entered invalid input {maxTry} times")
        return False,0, 0  # خارج شدن از برنامه
        # return True,time_str

    def get_shamsi_date_from_input(self):

        maxTry=self.__MaxCountTry
        attempts = 0  # شمارنده تلاش‌های ناموفق
        while attempts < maxTry:
            print()
            date_str = input("Enter date (YYYY/MM/DD or YYYY/M/D): ")  # گرفتن تاریخ به فرمت شمسی

            # استفاده از الگوی رگولار برای بررسی تاریخ با فرمت صحیح
            match = re.match(r"(\d{4})/(\d{1,2})/(\d{1,2})", date_str)

            if match:
                year, month, day = map(int, match.groups())

                # بررسی صحت سال، ماه و روز
                if 1370 <= year <= 1500 and 1 <= month <= 12 and 1 <= day <= 31:
                    # اگر تاریخ صحیح باشد، مقدار برگشتی سال، ماه و روز است
                    return True,year, month, day
                else:
                    print("Invalid date. Year must be between 1370 and 1500, month between 1 and 12, and day between 1 and 31.")
            else:
                print("Invalid format. Please enter the date in YYYY/MM/DD or YYYY/M/D format.")

            attempts += 1  # افزایش شمارنده تلاش‌های ناموفق

        print(f"You have entered invalid input {maxTry} times")
        return False,0,0,0

    def get_NationalCode_from_input(self):

        maxTry=self.__MaxCountTry
        attempts = 0  
        while attempts < maxTry:
            print()
            nationalCode_str = input("Enter NationalCode :  ")  # گرفتن تاریخ به فرمت شمسی

            
            match = re.match(r"^\d{10}$", nationalCode_str)

            if match:
                return True,nationalCode_str

            else:
                print("Invalid format. Please enter a ten-digit number for the national code.")

            attempts += 1  # افزایش شمارنده تلاش‌های ناموفق

        print(f"You have entered invalid input {maxTry} times")
        return False,""
