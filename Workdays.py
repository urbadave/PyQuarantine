import Holidays
from datetime import date, timedelta
from collections import namedtuple

DaysReturn = namedtuple('DaysReturn', 'allDays startDay workDays weekendDays holidayDays')

def computeDays(startDay: date, endDay: date):
    hols = Holidays.getAllHolidays(startDay.year, endDay.year)
    addADay = timedelta(days=1)
    endDay += addADay
    allDays = 0
    workDays = 0
    weekendDays = 0
    holidayDays = 0
    day = startDay
    while(day < endDay):        
        allDays += 1
        if(day.weekday() < 5): #5 and 6 are weekend days
            if(day not in hols):
                workDays += 1
            else:
                holidayDays += 1
        else:
            weekendDays += 1
        day += addADay
    retVal = DaysReturn(allDays=allDays, startDay=startDay, workDays=workDays, weekendDays=weekendDays, holidayDays=holidayDays)
    return retVal
