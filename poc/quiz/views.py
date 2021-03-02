import csv
from datetime import datetime
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.mail import send_mail
from django.forms.models import model_to_dict
from django.template.loader import render_to_string
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
    programs = Program.objects.order_by("program_name").all()
    return render(request, 'quiz/programs.html', {'programs': programs})

def email(request):
        try:
                if request.method == 'POST':
                        if request.POST.get('email'):
                                email = request.POST.get('email')
                                result_id = request.session.get('result_id', '')
                                if result_id == '':
                                    HttpResponse("Please finish the quiz first")
                                result = Result.obejcts.get(pk=result_id)
                                wantUpdate = request.POST.get('register', False)
                                wantResult = request.POST.get('sendRes', False)
                                if wantUpdate == 'on':
                                    result.email = email
                                    result.save()
                                if wantResult == 'on':
                                    configs = {
                                        'best_program': result.one.program_name
                                        'best_program_details': result.one.description
                                        'best_program_site': result.one.site
                                        'programs': [
                                            {
                                            'program_name': result.two.program_name
                                            'program_site': result.two.site
                                            },
                                            {
                                            'program_name': result.three.program_name
                                            'program_site': result.three.site
                                            },
                                            {
                                            'program_name': result.four.program_name
                                            'program_site': result.four.site
                                            },
                                            {
                                            'program_name': result.five.program_name
                                            'program_site': result.five.site
                                            },
                                            {
                                            'program_name': result.six.program_name
                                            'program_site': result.six.site
                                            },
                                            {
                                            'program_name': result.seven.program_name
                                            'program_site': result.seven.site
                                            },
                                            {
                                            'program_name': result.eight.program_name
                                            'program_site': result.eight.site
                                            },
                                            {
                                            'program_name': result.nine.program_name
                                            'program_site': result.nine.site
                                            },
                                            {
                                            'program_name': result.ten.program_name
                                            'program_site': result.ten.site
                                            },
                                            {
                                            'program_name': result.eleven.program_name
                                            'program_site': result.eleven.site
                                            },
                                            {
                                            'program_name': result.twelve.program_name
                                            'program_site': result.twelve.site
                                            },
                                            {
                                            'program_name': result.thirteen.program_name
                                            'program_site': result.thirteen.site
                                            },
                                            {
                                            'program_name': result.fourteen.program_name
                                            'program_site': result.fourteen.site
                                            },
                                            {
                                            'program_name': result.fifteen.program_name
                                            'program_site': result.fifteen.site
                                            }
                                        ]
                                    }
                                    msg_html = render_to_string('email_template.html', configs)
                                    msg_txt = render_to_string('email_template.txt', configs)
                                    send_mail(
                                        'Your Engineering Department Quiz Results',
                                        msg_txt,
                                        'johnneychendev@gmail.com',
                                        [email],
                                        html_message=msg_html,
                                        fail_silently=False,
                                    )
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
    result_list= []
    for code in results:
        result_list.append(Program.objects.get(key=code))
    res = Result()
    res.one = result_list[0]
    res.two = result_list[1]
    res.three = result_list[2]
    res.four = result_list[3]
    res.five = result_list[4]
    res.six = result_list[5]
    res.seven = result_list[6]
    res.eight = result_list[7]
    res.nine = result_list[8]
    res.ten = result_list[9]
    res.eleven = result_list[10]
    res.twelve = result_list[11]
    res.thirteen = result_list[12]
    res.fourteen = result_list[13]
    res.fifteen = result_list[14]
    res.time = datetime.today()
    res.save()
    request.session['saved_result'] = res.id
    return render(request, 'quiz/recommendations.html', {'result':res})
