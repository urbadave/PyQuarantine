import Holidays
from datetime import date, timedelta

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
    print('Total of ', allDays, 'days since', startDay)
    print(workDays, 'were work days')
    print(weekendDays, 'were weekend days')
    print(holidayDays, 'were holidays')
    
begin = date(2020, 3, 16)
end = date.today()
computeDays(begin, end)
