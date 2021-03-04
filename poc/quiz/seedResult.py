from .models import *
from random import randint, shuffle
import datetime

d1 = datetime.datetime.strptime('1/1/2015 1:30 PM', '%m/%d/%Y %I:%M %p')
d2 = datetime.datetime.strptime('1/1/2021 4:50 AM', '%m/%d/%Y %I:%M %p')

def random_date(start, end):
    return start + datetime.timedelta( seconds=randint(0, int((end - start).total_seconds())),
    )

programs = list()

for program in Program.objects.all():
    programs.append(program)

for i in range(5000):
    shuffle(programList)
    res = Result()
    res.one = programs[0]
    res.two = programs[1]
    res.three = programs[2]
    res.four = programs[3]
    res.five = programs[4]
    res.six = programs[5]
    res.seven = programs[6]
    res.eight = programs[7]
    res.nine = programs[8]
    res.ten = programs[9]
    res.eleven = programs[10]
    res.twelve = programs[11]
    res.thirteen = programs[12]
    res.fourteen = programs[13]
    res.fifteen = programs[14]
    res.time = random_date(d1,d2)
    res.save()