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
    path('logDetails/<int:logID>/', views.logDetails, name='logDetails'),

    # add new log
    path('newLog/', views.newLog, name='newLog'),

    # edit log
    path('editLog/<int:logID>', views.editLog, name='editLog'),

    # delete log
    path('deleteLog/<int:logID>', views.deleteLog, name='deleteLog'),

    # search bar
    path('searchLocation/', views.searchLocation, name='searchLocation'),


    # todo: routes below this comment don't work or are not finished

    # dynamically add a marker from search results
    path('addMarker/', views.addMarker, name='addMarker')

]
