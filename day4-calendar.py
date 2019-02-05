'''
Function:       Print calendar to command line
Date:           02.05.2019
Created By:     Anonymous Systems
'''
import calendar
import datetime


def printCalendar(year, month):
    cal = calendar.TextCalendar(calendar.SUNDAY).formatmonth(year, month)
    print(cal)


if __name__ == '__main__':
    now = datetime.datetime.now()
    dayweek_month_day = now.strftime('%A, %b %-d')
    currentYear = now.year
    currentMonth = now.month
    printCalendar(currentYear, currentMonth)
    print(f'Today is {dayweek_month_day}')
