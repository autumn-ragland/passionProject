from django.urls import path
from . import views

urlpatterns = [
    # landing page route (test)
    path('', views.index, name='index'),
]
