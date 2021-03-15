from .models import *
from django.db.models import Count, Q, F

def get_query_position(position):
    positions = ["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen"]
    returnArr = []
    for pos in positions:
        if pos != position:
            returnArr.append(pos)
        else:
            break
    returnArr.append(position)
    return returnArr

def programToId(program):
    return Program.objects.get(program_name=program).id

def programToKey(program):
    return Program.objects.get(program_name=program).key

def filter_time(data,before,after):
    if before != '':
        data = data.filter(time__lte=before)
    if after != '':
        data = data.filter(time__gte=after)
    return data