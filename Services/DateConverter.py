import jdatetime
import time
from datetime import datetime

class DateConverter:
    def __init__(self):
        pass
    
    def convert_shamsi_to_unix(self,year_shamsi, month_shamsi, day_shamsi, hour, minute):
        # تبدیل تاریخ شمسی به تاریخ میلادی
        date_shamsi = jdatetime.date(year_shamsi, month_shamsi, day_shamsi)
        date_miladi = date_shamsi.togregorian()

        # تبدیل تاریخ میلادی به datetime
        datetime_miladi = datetime(date_miladi.year, date_miladi.month, date_miladi.day, hour, minute)

        # تبدیل به یونیکس (ثانیه‌ها از 1970-01-01)
        unix_timestamp = int(time.mktime(datetime_miladi.timetuple()))

        return unix_timestamp