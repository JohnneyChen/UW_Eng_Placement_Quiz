from django.db.models import Count, F

from .models import *
from .queryHelper import *

def group_program(data):
    return data.values(program=F('one_id__program_name'), program_key=F('one_id__key')).annotate(times_suggested=Count('program'))

def all_filter( before, after):
    data = Result.objects.select_related('one').all()
    data = filter_time(data, before, after)
    data = group_program(data)
    return process_grouped_data_to_json(data)

def process_grouped_data_to_json(data):
    processedData = []
    for row in data:
        processedData.append({
            'program': row['program'],
            'key': row['program_key'],
            'total_recommendations': row['times_suggested']
        })
    return processedData