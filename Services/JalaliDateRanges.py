import jdatetime
import datetime

class JalaliDateRanges:
    @staticmethod
    def _to_unix(jdt):
        return int(jdt.togregorian().timestamp())

    @staticmethod
    def today():
        today = jdatetime.date.today()
        start = jdatetime.datetime(today.year, today.month, today.day, 0, 0, 0)
        end = jdatetime.datetime(today.year, today.month, today.day, 23, 59, 59)
        return JalaliDateRanges._to_unix(start), JalaliDateRanges._to_unix(end)

    @staticmethod
    def yesterday():
        today = jdatetime.date.today()
        yesterday = today - datetime.timedelta(days=1)
        start = jdatetime.datetime(yesterday.year, yesterday.month, yesterday.day, 0, 0, 0)
        end = jdatetime.datetime(yesterday.year, yesterday.month, yesterday.day, 23, 59, 59)
        return JalaliDateRanges._to_unix(start), JalaliDateRanges._to_unix(end)

    @staticmethod
    def this_month():
        today = jdatetime.date.today()
        start = jdatetime.datetime(today.year, today.month, 1, 0, 0, 0)

        if today.month == 12:
            days_in_month = 29 if today.year % 4 != 3 else 30
        elif today.month <= 6:
            days_in_month = 31
        else:
            days_in_month = 30

        end = jdatetime.datetime(today.year, today.month, days_in_month, 23, 59, 59)
        return JalaliDateRanges._to_unix(start), JalaliDateRanges._to_unix(end)

    @staticmethod
    def last_month():
        today = jdatetime.date.today()

        if today.month == 1:
            year = today.year - 1
            month = 12
        else:
            year = today.year
            month = today.month - 1

        if month == 12:
            days_in_month = 29 if year % 4 != 3 else 30
        elif month <= 6:
            days_in_month = 31
        else:
            days_in_month = 30

        start = jdatetime.datetime(year, month, 1, 0, 0, 0)
        end = jdatetime.datetime(year, month, days_in_month, 23, 59, 59)
        return JalaliDateRanges._to_unix(start), JalaliDateRanges._to_unix(end)

    @staticmethod
    def this_year():
        today = jdatetime.date.today()
        start = jdatetime.datetime(today.year, 1, 1, 0, 0, 0)
        end = jdatetime.datetime(today.year, 12, 29 if today.year % 4 != 3 else 30, 23, 59, 59)
        return JalaliDateRanges._to_unix(start), JalaliDateRanges._to_unix(end)

    @staticmethod
    def last_year():
        today = jdatetime.date.today()
        last_year = today.year - 1
        start = jdatetime.datetime(last_year, 1, 1, 0, 0, 0)
        end = jdatetime.datetime(last_year, 12, 29 if last_year % 4 != 3 else 30, 23, 59, 59)
        return JalaliDateRanges._to_unix(start), JalaliDateRanges._to_unix(end)
    
    @staticmethod
    def custom_range_unix(start_day, start_month, start_year, end_day, end_month, end_year):
        start_jdt = jdatetime.datetime(start_year, start_month, start_day, 0, 0, 0)
        end_jdt = jdatetime.datetime(end_year, end_month, end_day, 23, 59, 59)

        # تبدیل به datetime میلادی و سپس گرفتن timestamp یونیکس
        start_gdt = start_jdt.togregorian()
        end_gdt = end_jdt.togregorian()

        start_unix = int(start_gdt.timestamp())
        end_unix = int(end_gdt.timestamp())

        return start_unix, end_unix