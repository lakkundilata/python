
from datetime import date
def calculateage(birthdate):
    today=date.today()
    age=today.year-birthdate.year-((today.month,today.day)<(birthdate.month,birthdate.day))
    return age
print(calculateage(date(2002,2,19)),"years")