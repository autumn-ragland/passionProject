from django.conf import settings
from django.views.static import serve

from . import views
from django.urls import path

urlpatterns = [
    # landing page
    path('', views.index, name='index'),

    # profile page
    path('myLogs/', views.myLogs, name='myLogs'),

    # add new user
    path('newUser/', views.newUser, name='newUser'),

    # log details
    path('logDetails/<int:logID>/', views.logDetails, name='logDetails'),

    # add new log
    path('newLog/', views.newLog, name='newLog'),
    # edit log
    path('editLog/<int:logID>', views.editLog, name='editLog'),
    # delete log
    path('deleteLog/<int:logID>', views.deleteLog, name='deleteLog'),

    # favorite log
    path('favoriteLogs/<int:logID>/<slug:userID>', views.favoriteLogs, name='favoriteLogs'),
    path('viewFavorites/<slug:userID>', views.viewFavorites, name='viewFavorites'),

    # search bar
    path('searchLocation/', views.searchLocation, name='searchLocation'),

    # image field
    path('images/<path:path>/', serve, {'document_root': settings.MEDIA_ROOT, }),

]
