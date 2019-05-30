from django.urls import path
from . import views

urlpatterns = [
    # landing page route
    path('', views.index, name='index'),
    # test route to do a simple API query
    path('test/', views.test, name='test'),
    # location details route
    path('location_details/', views.location_details, name='location_details'),
    # log details route
    path('log_details/', views.log_details, name='log_details'),
    # profile page
    path('profile/', views.profile, name='profile'),
    # new user path
    path('newUser/', views.newUser, name='newUser'),
    # places api hit attempt
    # path('find_place/<str:input>/<str:input_type>/', views.find_place, name='find_place'),
]
