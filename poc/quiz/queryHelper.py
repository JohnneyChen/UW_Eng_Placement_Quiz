from .models import *
from django.db.models import Count, Q, F

# function that recieves a single position and returns an array with positions preceeding and including that position
# example: if three was the position, it would return [one, two, three]
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

# helper to convert a program name into the program's id
def programToId(program):
    return Program.objects.get(program_name=program).id

# helper to convert a program name into the program's key
def programToKey(program):
    return Program.objects.get(program_name=program).key
    
# helper that recieves a query set and returns results in a specified date range
def filter_time(data,before,after):
    if before != '':
        # removes all results after the specified range
        data = data.filter(time__lte=before)
    if after != '':
        # removes all results before the specified range
        data = data.filter(time__gte=after)
    return data