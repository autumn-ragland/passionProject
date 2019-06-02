from django.urls import path
from . import views

urlpatterns = [
    # landing page
    path('', views.index, name='index'),

    # profile page
    path('myLogs/', views.myLogs, name='myLogs'),

    # add new user
    path('newUser/', views.newUser, name='newUser'),

    # location details
    path('locationDetails/', views.locationDetails, name='locationDetails'),

    # log details
    path('logDetails/', views.logDetails, name='logDetails'),

    # add new log
    path('newLog/', views.newLog, name='newLog'),

    # search bar
    path('searchLocation/', views.searchLocation, name='searchLocation'),

    # todo: routes below this comment don't work

    # places api hit attempt
    path('find_place/', views.find_place, name='find_place'),

]
