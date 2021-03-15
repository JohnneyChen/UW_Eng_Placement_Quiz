"""poc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from . quiz import views

urlpatterns = [
    path('', views.home, name='home'),
    path('programs', views.programs, name='programs'),
    path('quiz/', include('poc.quiz.urls')),
    path('admin/', admin.site.urls),
    path('login/', views.user_login, name='login'),
    path('signup/', views.signup, name="signup"),
    path('queryform/', views.query_form),
    path('api/all_data', views.get_all_data, name='all_data_api'),
    path('api/program_data', views.get_programs_data, name='programs_data_api'),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('api/all_charts', views.charts_api, name='chart_api'),
    path('reorder_dashboard/', views.reorder_dashboard, name="reorder_dashboard"),
    path('edit_chart/', views.edit_chart, name='edit_chart'),
    path('delete_chart/', views.delete_chart, name='delete_chart')
]
