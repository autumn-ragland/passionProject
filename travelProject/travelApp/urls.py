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

    # test route to do a simple API query
    path('test/', views.test, name='test'),

    # places api hit attempt
    # path('find_place/', views.find_place, name='find_place'),
    # test route to create a marker
    # path('testMarker/', views.testMarker, name='testMarker'),
]
