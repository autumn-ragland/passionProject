from django.shortcuts import render
# import googlemaps


def index(request):
    # map = new google.maps.Map(document.getElementById('map'), {
    #     center: {lat: -34.397, lng: 150.644},
    #     zoom: 8
    # })
    context = {
        'map': map
    }
    return render(request, 'travelApp/index.html', context)


def location_details(request):
    return render(request, 'travelApp/locationDetails.html')


def log_details(request):
    return render(request, 'travelApp/logDetails.html')
