from django.shortcuts import render
# import googlemaps
# from .mapsGitHub import Client
# todo: python is not recognizing googlemaps module even though I can see it on pip list

# gmaps = googlemaps.Client(key='AIzaSyAcVeR1EcysjeZr4eQE_mtiJ6suMxXY52Y')
# find a way to securely pass my key so I don't get charged

def index(request):
    # todo: probably shouldn't render map like this (doesn't matter till I can import module)
    # let embedMap = new google.maps.Map{
    #     center: {lat: -34.397, lng: 150.644},
    #     zoom: 8
    # }
    context = {
        # 'map': embedMap
    }
    return render(request, 'travelApp/index.html', context)


# def test():
#     geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
#     print(geocode_result)


def location_details(request):
    return render(request, 'travelApp/locationDetails.html')


def log_details(request):
    return render(request, 'travelApp/logDetails.html')
