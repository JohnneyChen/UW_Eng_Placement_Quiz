from .models import *
from .queryHelper import *
from django.db.models import Count, Q, F

def filter_program_position(data, program, position):
    program_id = programToId(program)
    label = "{program}/{position}".format(program=programToKey(program), position=position)
    query = {}
    key = '{}_id'.format(position)
    query[key]=program_id
    return {
        'program_position':label, 
        'total_recommendations':data.filter(**query).count()
    }

def filter_program_count(data, program, position):
    positions = get_query_position(position)
    totalRes = Result.objects.none()
    program_id = programToId(program)
    for position in positions:
        query = {}
        key = '{}_id'.format(position)
        query[key] = program_id
        totalRes = totalRes | data.filter(**query)
    return {
        'program' : programToKey(program),
        'total_recommendations': totalRes.count()
    }

def program_position_query(programs, position, before, after):
    positions = get_query_position(position)
    data = Result.objects.all()
    data = filter_time(data, before, after)
    returnArr = []
    for program in programs:
        for position in positions:
            returnArr.append(filter_program_position(data, program, position))
    return returnArr

def program_count_query(programs, position, before, after):
    data = Result.objects.all()
    data = filter_time(data, before, after)
    returnArr = []
    for program in programs:
        returnArr.append(filter_program_count(data, program, position))
    return returnArr