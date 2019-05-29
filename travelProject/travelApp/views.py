from django.shortcuts import render
# import googlemaps
# todo: python is not recognizing googlemaps module even though I can see it on pip list

# gmaps = googlemaps.Client(key='Add Your Key here')
# find a way to securely pass my ley so I don't get charged


def index(request):
    # todo: probably shouldn't render map like this (doesn't matter till I can import module)
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
