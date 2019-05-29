from django.shortcuts import render
# import googlemaps


def index(request):
    # map = new google.maps.Map
    # ({
    #     center: {lat: -35.1495, lng: 90.0490},
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
