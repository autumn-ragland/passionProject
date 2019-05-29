from django.shortcuts import render


def index(request):
    return render(request, 'travelApp/index.html')


def location_details(request):
    return render(request, 'travelApp/locationDetails.html')


def log_details(request):
    return render(request, 'travelApp/logDetails.html')
