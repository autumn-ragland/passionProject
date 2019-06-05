from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import UserForm, UserModel, LogForm, LocationLog
import googlemaps


# find a way to securely pass my key so I don't get charged
gmaps = googlemaps.Client(key='AIzaSyAcVeR1EcysjeZr4eQE_mtiJ6suMxXY52Y')


# landing page
def index(request):
    locationLogs = LocationLog.objects.all()
    context = {
        'allLogs': locationLogs
    }
    return render(request, 'travelApp/index.html', context)


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


# create a new log
def newLog(request):
    # for logged in users
    if request.user.is_authenticated:
        # get empty log form
        form = LogForm(request.POST or None)
        # determine logged in user
        current_user = UserModel.objects.get(username=request.user)
        if request.method == 'POST':
            # on submit add log to model with logged in user fk
            LocationLog.objects.create(location=request.POST['location'],
                                       location_lat=request.POST['location_lat'],
                                       location_long=request.POST['location_long'],
                                       date_of_visit=request.POST['date_of_visit'],
                                       summary=request.POST['summary'],
                                       safety=request.POST['safety'],
                                       affordability=request.POST['affordability'],
                                       accessibility=request.POST['accessibility'],
                                       image=request.FILES['image'],
                                       userModel_fk=current_user)
            # on submit render profile page
            return redirect('index')
        # pass empty log form
        context = {
            'form': form
        }
    # for users not logged in
    else:
        form = ''
        context = {
            'form': form
        }
    # render new log form page
    return render(request, 'travelApp/newLog.html', context)


# edit log
def editLog(request, logID):
    # grab log to edit
    log = get_object_or_404(LocationLog, pk=logID)
    # populate log form
    form = LogForm(request.POST or None, request.FILES or None, instance=log)

    if request.method == 'POST':
        # on submit save edits
        form.save()
        # on submit redirect to my entries page
        return redirect('myLogs')
    # pass populated entry form
    context = {
        'form': form,
    }
    return render(request, 'travelApp/editLog.html', context)


# delete log
def deleteLog(request, logID):
    # grab specific log
    log = get_object_or_404(LocationLog, pk=logID)

    if request.method == 'POST':
        # on submit delete log
        log.delete()
        # on submit render my logs page
        return redirect('myLogs')
    # pass specific log
    context = {
        'log': log
    }
    # render confirmation form
    return render(request, 'travelApp/deleteLog.html', context)


# list logs (currently lists all logs)
def myLogs(request):
    current_user = UserModel.objects.get(username=request.user)
    user_logs = LocationLog.objects.filter(userModel_fk=current_user)
    context = {
        'myLogs': user_logs
    }
    return render(request, 'travelApp/profile.html', context)


# search bar submit form
def searchLocation(request):
    searchItem = request.POST['searchBar']
    geocode_result = gmaps.geocode(searchItem)
    locationLogs = LocationLog.objects.all()
    context = {
        "search": geocode_result,
        "input": searchItem,
        'allLogs': locationLogs
    }
    return render(request, 'travelApp/searchResults.html', context)


# log details page
def logDetails(request, logID):
    # get entry
    log = LocationLog.objects.get(pk=logID)
    # pass entry and related info
    context = {
        'log': log,
    }
    return render(request, 'travelApp/logDetails.html', context)




