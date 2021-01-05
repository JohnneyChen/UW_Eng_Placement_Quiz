import csv
from datetime import datetime
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import json
import pickle
import numpy as np
import sys

from . models import *
from . data_load import *
from . activate_model import *

def about(request):
    return render(request, 'quiz/about.html')

def home(request):
    return render(request, 'quiz/home.html')

def quiz(request):
    return render(request, 'quiz/quiz.html')

def programs(request):
    results = list(sorted(READ_PROGRAMS.keys()))
    return_list = []
    for key in results:
        return_list.append(Recommendation.objects.get(code=READ_PROGRAMS[key]))

    comparison_set = Comparison.objects.all()
    description_set = Description.objects.all()
    course_set = Course.objects.all()
    career_set = Career.objects.all()
    context ={
            'recommendation_set':return_list,
            'comparison_set':list(comparison_set),
            'course_set':list(course_set),
            'career_set':list(career_set),
            'description_set':list(description_set)
            }
    return render(request,'quiz/programs.html',context)

def email(request):
        try:
                print("Accessed submit...")
                if request.method == 'POST':
                        if request.POST.get('email'):
                                email = Email()
                                email.email = request.POST.get('email')
                                # email.save()
                                return render(request,'quiz/emailSubmission.html')
        except:
                print("Unexpected error:", sys.exc_info()[0])
        return HttpResponse("Something went wrong...Your email was not submitted")


def submit(request):
    try:
        print("Accessed submit...")
        if request.method == 'POST':
            print("Post method received")
            post_dict = request.POST
            print(post_dict)
            return recommendations(request,post_dict)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        return HttpResponse("Something went wrong...create) 3")

def recommendations(request,post_dict):
    model_name = MODEL_NAME
    post_dict = transform_post_dict(post_dict)
    print("Entered Response Creation...")

    encoded_dictionary = get_encoded_dict(model_name)
    print("encoded_dictionary retrieved...")

    # problem_type = encoded_dictionary['problem_type']['problem_type']
    creative = encoded_dictionary['creative']['creative']
    outdoors = encoded_dictionary['outdoors']['outdoors']
    career = encoded_dictionary['career']['career']
    group_work = encoded_dictionary['group_work']['group_work']
    liked_courses = encoded_dictionary['liked_courses']['liked_courses']
    disliked_courses = encoded_dictionary['disliked_courses']['disliked_courses']
    # programming = encoded_dictionary['programming']['programming']
    join_clubs = encoded_dictionary['join_clubs']['join_clubs']
    not_clubs = encoded_dictionary['not_clubs']['not_clubs']
    liked_projects = encoded_dictionary['liked_projects']['liked_projects']
    disliked_projects = encoded_dictionary['disliked_projects']['disliked_projects']
    # tv_shows = encoded_dictionary['tv_shows']['tv_shows']
    alternate_degree = encoded_dictionary['alternate_degree']['alternate_degree']
    # expensive_equipment = encoded_dictionary['expensive_equipment']['expensive_equipment']
    drawing = encoded_dictionary['drawing']['drawing']
    essay = encoded_dictionary['essay']['essay']
    architecture = encoded_dictionary['architecture']['architecture']
    automotive = encoded_dictionary['automotive']['automotive']
    business = encoded_dictionary['business']['business']
    construction = encoded_dictionary['construction']['construction']
    health = encoded_dictionary['health']['health']
    environment = encoded_dictionary['environment']['environment']
    manufacturing = encoded_dictionary['manufacturing']['manufacturing']
    technology = encoded_dictionary['technology']['technology']

    print("Labels encoded..")

	# Prepare the feature vector for prediction

    print("Loading new_vector....")
    pkl_file = open('poc/quiz/exported_model_files/'+model_name+'_cat', 'rb')
    index_dict = pickle.load(pkl_file)
    new_vector = np.zeros(21)

    print("Loading response into new_vector...")

    # new_vector[0] =  0 #problem_type[post_dict['problem_type'][0]]
    new_vector[0] =  creative[post_dict['creative'][0]]
    new_vector[1] =  outdoors[post_dict['outdoors'][0]]
    new_vector[2] =  career[post_dict['career'][0]]
    new_vector[3] =  group_work[post_dict['group_work'][0]]
    new_vector[4] =  liked_courses[post_dict['liked_courses'][0]]
    new_vector[5] =  disliked_courses[post_dict['disliked_courses'][0]]
    # new_vector[7] =  0 #programming[post_dict['programming'][0]]
    new_vector[6] =  join_clubs[post_dict['join_clubs'][0]]
    new_vector[7] =  not_clubs[post_dict['not_clubs'][0]]
    new_vector[8] = liked_projects[post_dict['liked_projects'][0]]
    new_vector[9] = disliked_projects[post_dict['disliked_projects'][0]]
    # new_vector[12] = 0 #tv_shows[post_dict['tv_shows'][0]]
    new_vector[10] = alternate_degree[post_dict['alternate_degree'][0]]
    # new_vector[14] = 0 #expensive_equipment[post_dict['expensive_equipment'][0]]
    new_vector[11] = drawing[post_dict['drawing'][0]]
    new_vector[12] = essay[post_dict['essay'][0]]
    new_vector[13] = architecture[post_dict['architecture'][0]]
    new_vector[14] = automotive[post_dict['automotive'][0]]
    new_vector[15] = business[post_dict['business'][0]]
    new_vector[16] = construction[post_dict['construction'][0]]
    new_vector[17] = health[post_dict['health'][0]]
    new_vector[18] = environment[post_dict['environment'][0]]
    new_vector[19] = manufacturing[post_dict['manufacturing'][0]]
    new_vector[20] = technology[post_dict['technology'][0]]

    if 'ohe' in model_name:
        print("entered ohe model handling")
        new_vector = list(new_vector)
        for i in range(len(new_vector)):
            new_vector[i]  = str(int(new_vector[i]))
        columns = [
                    'creative',
                    'outdoors',
                    'career',
                    'group_work',
                    'liked_courses',
                    'disliked_courses',
                    'join_clubs',
                    'not_clubs',
                    'liked_projects',
                    'disliked_projects',
                    'alternate_degree',
                    'drawing',
                    'essay',
                    'architecture',
                    'automotive',
                    'business',
                    'construction',
                    'health',
                    'environment',
                    'manufacturing',
                    'technology'
        ]
        t7 = get_label_encoded_data('poc/quiz/exported_model_files/t7.csv',model_name='t7',column_list=columns,drop_not_happy='H',data_balance=False)[0]
        data_to_append = {}
        for i in range(len(columns)):
            data_to_append[t7.columns[i]] = int(new_vector[i])
        t7 = t7.append(data_to_append, ignore_index = True)
        t7 = pd.get_dummies(t7,columns=columns)
        rename_columns = {
            'architecture_1':'architecture',
            'automotive_1':'automotive',
            'business_1':'business',
            'construction_1':'construction',
            'health_1':'health',
            'environment_1':'environment',
            'manufacturing_1':'manufacturing',
            'technology_1':'technology'
        }
        drop_columns = [
            'architecture_0',
            'automotive_0',
            'business_0',
            'construction_0',
            'health_0',
            'environment_0',
            'manufacturing_0',
            'technology_0'
        ]
        t7 = t7.rename(index=str,columns = rename_columns)
        t7 = t7.drop(drop_columns, axis=1)
        new_vector = np.array(t7[len(t7)-1:len(t7)])

    print("Loading model...")
    print(MODEL_NAME)
    pkl_file = open('poc/quiz/exported_model_files/'+model_name+'.pkl', 'rb')
    model = pickle.load(pkl_file)
    try:
        prediction = model.predict_proba([new_vector])
    except:
        prediction = model.predict_proba(new_vector)
    print("Prediction created...")

    # Getting Ordered Results
    results_dict = retrieve_prediction_labels(model,prediction)
    results = list(sorted(results_dict, key=lambda key: results_dict[key],reverse=True))
    return_list = []
    for key in results:
        return_list.append(Recommendation.objects.get(code=key))

    print("Weights of Results")
    print(results_dict)
    print("Response Created...")

    print("Creating new record...")
    new_record = Result()
    new_record.time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    # new_record.problem_type = post_dict['problem_type']
    new_record.creative = post_dict['creative']
    new_record.outdoors = post_dict['outdoors']
    new_record.career = post_dict['career']
    new_record.group_work = post_dict['group_work']
    new_record.liked_courses = post_dict['liked_courses']
    new_record.disliked_courses = post_dict['disliked_courses']
    # new_record.programming = post_dict['programming']
    new_record.join_clubs = post_dict['join_clubs']
    new_record.not_clubs = post_dict['not_clubs']
    new_record.liked_projects = post_dict['liked_projects']
    new_record.disliked_projects = post_dict['disliked_projects']
    # new_record.tv_shows = post_dict['tv_shows']
    new_record.alternate_degree = post_dict['alternate_degree']
    # new_record.expensive_equipment = post_dict['expensive_equipment']
    new_record.drawing = post_dict['drawing']
    new_record.essay = post_dict['essay']
    new_record.architecture = post_dict['architecture']
    new_record.automotive = post_dict['automotive']
    new_record.business = post_dict['business']
    new_record.construction = post_dict['construction']
    new_record.health = post_dict['health']
    new_record.environment = post_dict['environment']
    new_record.manufacturing = post_dict['manufacturing']
    new_record.technology = post_dict['technology']

    new_record.arch = results_dict['arch']
    new_record.arche = results_dict['arch-e']
    new_record.bmed = results_dict['bmed']
    new_record.ce = results_dict['ce']
    new_record.cive = results_dict['chem']
    new_record.chem = results_dict['cive']
    new_record.env = results_dict['elec']
    new_record.elec = results_dict['env']
    new_record.geo = results_dict['geo']
    new_record.mech = results_dict['mech']
    new_record.msci = results_dict['msci']
    new_record.nano = results_dict['nano']
    new_record.syde = results_dict['swe']
    new_record.swe = results_dict['syde']
    new_record.tron = results_dict['tron']
    print("new record information collected...")
    print("new record not saved. DB CLOSED 4 BIZNESS..")

    # new_record.save()
    print("new record saved...")

    comparison_set = Comparison.objects.all()
    description_set = Description.objects.all()
    course_set = Course.objects.all()
    career_set = Career.objects.all()
    context ={
            'recommendation_set':return_list,
            'comparison_set':list(comparison_set),
            'course_set':list(course_set),
            'career_set':list(career_set),
            'description_set':list(description_set)
            }
    return render(request,'quiz/recommendations.html',context)
