from .models import *
from .queryHelper import *
from django.db.models import Count, Q, F

# helper to group results based on the 1st recommended program
def group_program(data):
    # returns a new QuerySet containing results in format {program_id: id, times_suggested: <INT>}
    return data.values(program_id=F('one_id')).annotate(times_suggested=Count('program_id'))

# herlper to reformat QuerySet object into an array of results
def process_grouped_data_to_json(data):
    processedData = []
    # iterates through the QuerySet and appends to the processedData array a dict containing result information for that iteration
    for row in data:
        # each program has a corresponding result dict with containing the program's name, key, and total recommendations
        processedData.append({
            'program': Program.objects.get(pk=row['program_id']).program_name,
            'key' : Program.objects.get(pk=row['program_id']).key,
            'total_recommendations': row['times_suggested']
        })
    return processedData

# returns payload to send after query request for all program's times-recommended
def all_filter( before, after):
    # gets all of the results stored
    data = Result.objects.all()
    # keeps only results in specified time range
    data = filter_time(data, before, after)
    # groups results based on 1st recommendation
    data = group_program(data)
    # returns data reformated for JSON
    return process_grouped_data_to_json(data)
