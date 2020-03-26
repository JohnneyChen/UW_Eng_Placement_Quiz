from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.quiz, name='quiz'),
    path('recommendations', views.recommendations, name='recommendations'),
    path('recommendations', views.email, name='emailSubmit' ),
    url(r'submit', views.submit, name='submit'),
    url(r'startQuiz', views.quiz, name='startQuiz'),
    url(r'programInfo', views.programs, name='programInfo'),
    url(r'about', views.about, name='about')
]
