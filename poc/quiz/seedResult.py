from .models import *
from random import randint, shuffle
from datetime import datetime

d1 = datetime.strptime('1/1/2015 1:30 PM', '%m/%d/%Y %I:%M %p')
d2 = datetime.strptime('1/1/2021 4:50 AM', '%m/%d/%Y %I:%M %p')

def random_date(start, end):
    return start + datetime.timedelta( seconds = randint(0,int((end-start).total_seconds()))

programList = []
for program in Program.objects.all():
    programList.append(program)

for i in range(5000):
    shuffle(programList)
    res = Result()
    res.one = programList[0]
    res.two = programList[1]
    res.three = programList[2]
    res.four = programList[3]
    res.five = programList[4]
    res.six = programList[5]
    res.seven = programList[6]
    res.eight = programList[7]
    res.nine = programList[8]
    res.ten = programList[9]
    res.eleven = programList[10]
    res.twelve = programList[11]
    res.thirteen = programList[12]
    res.fourteen = programList[13]
    res.fifteen = programList[14]
    res.time = random_date(d1,d2)
    res.save()