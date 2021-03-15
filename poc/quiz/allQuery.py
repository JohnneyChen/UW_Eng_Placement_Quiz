from .models import *
from django.db.models import Count, Q, F

def filter_time(data,before,after):
    if before != '':
        data = data.filter(time__lte=before)
    if after != '':
        data = data.filter(time__gte=after)
    return data

def group_program(data):
    return data.values(program=F('one_id')).annotate(times_suggested=Count('program'))

def all_filter( before, after):
    data = Result.objects.all()
    data = filter_time(data, before, after)
    data = group_program(data)
    return process_grouped_data_to_json(data)

def process_grouped_data_to_json(data):
    processedData = []
    for row in data:
        processedData.append({
            'program': Program.objects.get(pk=row['program']).program_name,
            'key' : Program.objects.get(pk=row['program']).key,
            'total_recommendations': row['times_suggested']
        })
    return processedData