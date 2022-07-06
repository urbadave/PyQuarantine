import calendar
from datetime import datetime, timedelta

def getRelativeHoliday(year: int, month: int, weekday: calendar.weekday, position: int, dayAfter:bool = False):
    calFactory = calendar.Calendar(weekday) #Calendar month with the week day fo the holiday as first day in week
    checkDay = next(calFactory.itermonthdays(year, month)) #if the date of the first day is 0, then it's from the previous month
    dateList = [d for d in calFactory.itermonthdates(year, month) if d.weekday() == weekday] #get list of all the first week days
    if(checkDay != 0):  #if the first day is not 0, then the first day is the desired weekday
        position -= 1
    holiday = dateList[position]  #get the date

    if(dayAfter):
        holiday += timedelta(days=1)

    return holiday

def getDateHoliday(year: int, month: int, day: int):
    holiday = datetime(year, month, day).date()
    if holiday.weekday() == 5:
        holiday -= timedelta(days=1)
    elif holiday.weekday() == 6:
        holiday += timedelta(days=1)
    return holiday

