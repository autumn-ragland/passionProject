from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import UserForm, UserModel
import googlemaps

# find a way to securely pass my key so I don't get charged
gmaps = googlemaps.Client(key='AIzaSyAcVeR1EcysjeZr4eQE_mtiJ6suMxXY52Y')


def index(request):
    return render(request, 'travelApp/index.html')


# create new user
def newUser(request):
    # grab empty user form
    form = UserForm(request.POST or None)

    if request.method == 'POST':
        # on submit add users to model and django table
        User.objects.create_user(request.POST['username'], "", request.POST['password'])
        form.save()
        # on submit render home page
        return redirect('index')
    # pass empty user form
    context = {
        'form': form
    }
    # render user form page
    return render(request, 'travelApp/newUser.html', context)

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


# profile page
def profile(request):
    return render(request, 'travelApp/profile.html')
