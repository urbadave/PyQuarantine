
from datetime import date
from Workdays import computeDays

begin = date(2020, 3, 16)
end = date.today()
result = computeDays(begin, end)

print('Total of', result.allDays, 'days since', result.startDay)
print(result.workDays, 'were work days')
print(result.weekendDays, 'were weekend days')
print(result.holidayDays, 'were holidays')
