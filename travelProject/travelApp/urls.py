from django.urls import path
from . import views

urlpatterns = [
    # landing page route
    path('', views.index, name='index'),
    path('location_details/', views.location_details, name='location_details'),
    path('log_details/', views.log_details, name='log_details'),
]
