from .models import *
from .queryHelper import *

# helper for filtering without summing all the recommendations at each position
# only returns result for one program at one position (eg. computer engineering at four)
def filter_program_position(data, program, position):
    # gets the id of the program to filter by id
    program_id = programToId(program)
    # creates a label for the recommendation count
    label = "{program}/{position}".format(program=programToKey(program), position=position)
    # creates a query to get all results where a specific program is recommended at a specific position
    # example: query for computer engineering (id=1) being recommended as the fourth program to consider will have query dict {'four_id':1}
    # this would return the exact same results as data.filter(four_id=1)
    query = {}
    key = '{}_id'.format(position)
    query[key]=program_id
    # returns an dict with program_position key used to label count data and total_recommendations key containing actual count of recommendations
    return {
        'program_position':label, 
        'total_recommendations':data.filter(**query).count()
    }

# helper for filtering while summing all recommendations at each position for a specific program
# returns the total recommendations for one program before(and including) a certain position
# example: filter_program_count(data, 'Computer Engineering', 'three') would return how many times comupter engineering has been recommended as the 1st, 2nd, or 3rd place recommendation
def filter_program_count(data, program, position):
    # gets array of positions before and including the specified position (see queryHelper.py for more details)
    positions = get_query_position(position)
    #empty query object for Result model to later append querys of Result to
    totalRes = Result.objects.none()
    # gets the id of the program to filter by id
    program_id = programToId(program)
    # iterates through each position and appends all the results of the program being recommended at that specific position to the total results
    for position in positions:
        # creates a query to get all results where a specific program is recommended at a specific position
        # example: query for computer engineering (id=1) being recommended as the fourth program to consider will have query dict {'four_id':1}
        # this would return the exact same results as data.filter(four_id=1)
        query = {}
        key = '{}_id'.format(position)
        query[key] = program_id
        # appends the result query to total results
        totalRes = totalRes | data.filter(**query)
    # returns an dict with program key used to label count data and total_recommendations key containing actual count of recommendations    
    return {
        'program' : programToKey(program),
        'total_recommendations': totalRes.count()
    }

# returns payload to send after query request to seperate recommendations for programs by what position it was recommended
def program_position_query(programs, position, before, after):
    # gets array of positions before and including the specified position (see queryHelper.py for more details)
    positions = get_query_position(position)
    # gets all of the results stored
    data = Result.objects.all()
    # keeps only results in specified time range
    data = filter_time(data, before, after)
    # returns an array containing recommendation_count/program_position datasets for each program at each position
    returnArr = []
    for program in programs:
        for position in positions:
            returnArr.append(filter_program_position(data, program, position))
    return returnArr

# returns payload to send after query request to sum up recommendations by program regardless of what position it was recommended
def program_count_query(programs, position, before, after):
    # gets all of the results stored
    data = Result.objects.all()
    # keeps only results in specified time range
    data = filter_time(data, before, after)
    # returns an array containing recommendation_count/program datasets for each program
    returnArr = []
    for program in programs:
        returnArr.append(filter_program_count(data, program, position))
    return returnArr