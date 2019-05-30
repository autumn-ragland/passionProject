from django.shortcuts import render
from django.http import HttpResponse
import googlemaps

# find a way to securely pass my key so I don't get charged
gmaps = googlemaps.Client(key='AIzaSyAcVeR1EcysjeZr4eQE_mtiJ6suMxXY52Y')


def index(request):
    return render(request, 'travelApp/index.html')


# test request to do a simple query on the API
def test(request):
    geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
    return HttpResponse(geocode_result)


# location details page
def location_details(request):
    return render(request, 'travelApp/locationDetails.html')


# log details page
def log_details(request):
    return render(request, 'travelApp/logDetails.html')
