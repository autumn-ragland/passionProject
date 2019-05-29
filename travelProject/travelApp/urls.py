from django.urls import path
from . import views

urlpatterns = [
    # landing page route
    path('', views.index, name='index'),
]
