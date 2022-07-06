import calendar
from datetime import datetime, timedelta

def getRelativeHoliday(year: int, month: int, weekday: calendar.weekday, position: int, dayAfter:bool = False):
    calFactory = calendar.Calendar(weekday) #Calendar month with the week day fo the holiday as first day in week
    checkDay = next(calFactory.itermonthdays(year, month)) #if the date of the first day is 0, then it's from the previous month
    dateList = [d for d in calFactory.itermonthdates(year, month) if d.weekday() == weekday] #get list of all the first week days
    if(checkDay != 0 and position >= 0):  #if the first day is not 0, then the first day is the desired weekday
        position -= 1
    holiday = dateList[position]  #get the date

    if(dayAfter):
        holiday += timedelta(days=1)

    return holiday

# hol = getRelativeHoliday(2022, 5, calendar.MONDAY, -1)
# print(hol)

def getDateHoliday(year: int, month: int, day: int):
    holiday = datetime(year, month, day).date()
    if holiday.weekday() == 5:
        holiday -= timedelta(days=1)
    elif holiday.weekday() == 6:
        holiday += timedelta(days=1)
    return holiday

def getNewYears(year: int):
    return getDateHoliday(year, 1, 1)

def getMartinLutherKing(year: int):
    return getRelativeHoliday(year, 1, calendar.MONDAY, 3)

def getPresidents(year: int):
    return getRelativeHoliday(year, 2, calendar.MONDAY, 3)

def getBirthday(year: int):
    return getDateHoliday(year, 3, 1)

def getMemorial(year: int):
    return getRelativeHoliday(year, 5, calendar.MONDAY, -1)

def getJuneteenth(year: int):
    return getDateHoliday(year, 6, 19)

def getIndependence(year: int):
    return getDateHoliday(year, 7, 4)

def getLabor(year: int):
    return getRelativeHoliday(year, 9, calendar.MONDAY, 1)

def getThanksgiving(year: int):
    return getRelativeHoliday(year, 11, calendar.THURSDAY, 3)

def getAfterThanksgiving(year: int):
    return getRelativeHoliday(year, 11, calendar.THURSDAY, 3, True)

def getChristmas(year: int):
    return getDateHoliday(year, 12, 25)

def getHolidayList(year: int):
    retVal = []
    retVal.append(getNewYears(year))
    retVal.append(getMartinLutherKing(year))
    retVal.append(getPresidents(year))
    if(year > 2022):
        retVal.append(getBirthday(year))
    retVal.append(getMemorial(year))
    if(year > 2022):
        retVal.append(getJuneteenth(year))
    retVal.append(getIndependence(year))
    retVal.append(getLabor(year))
    retVal.append(getThanksgiving(year))
    if(year > 2021):
        retVal.append(getAfterThanksgiving(year))
    retVal.append(getChristmas(year))
    return retVal

# holiday2020 = getHolidayList(2020)
# holiday2022 = getHolidayList(2022)
# holiday2024 = getHolidayList(2024)

# print(holiday2020)
# print(holiday2022)
# print(holiday2024)