from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import UserForm, UserModel, LogForm, LocationLog
from django.db.models import Q
import googlemaps


# find a way to securely pass my key so I don't get charged
gmaps = googlemaps.Client(key='AIzaSyAcVeR1EcysjeZr4eQE_mtiJ6suMxXY52Y')


# home page
def index(request):
    # grab all logs
    locationLogs = LocationLog.objects.all()
    # pass all logs
    context = {
        'allLogs': locationLogs
    }
    # render home page
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
        form = LogForm(request.POST or None, request.FILES or None)
        # determine logged in user
        current_user = UserModel.objects.get(username=request.user)
        if request.method == 'POST':

            # allow a default image/no image selection
            tempImageFile = request.FILES
            if not request.FILES:
                tempImageFile = '/images/NoImage.png'
            else:
                tempImageFile = tempImageFile["image"]

            # on submit add log to model with logged in user fk
            LocationLog.objects.create(location=request.POST['location'],
                                       location_lat=request.POST['location_lat'],
                                       location_long=request.POST['location_long'],
                                       date_of_visit=request.POST['date_of_visit'],
                                       summary=request.POST['summary'],
                                       safety=request.POST['safety'],
                                       affordability=request.POST['affordability'],
                                       accessibility=request.POST['accessibility'],
                                       image=tempImageFile,
                                       userModel_fk=current_user)
            # on submit render home page
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
        # on submit redirect to my logs page
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


# list logs
def myLogs(request):
    # grab current user
    current_user = UserModel.objects.get(username=request.user)
    # grab logs by current user
    user_logs = LocationLog.objects.filter(userModel_fk=current_user)
    context = {
        'myLogs': user_logs
    }
    return render(request, 'travelApp/profile.html', context)


# search bar submit form
def searchLocation(request):
    # grab user search
    searchItem = request.POST['searchBar']
    # search google api
    geocode_result = gmaps.geocode(searchItem)
    # search my models
    locationLogs = LocationLog.objects.filter(Q(location__contains=request.POST['searchBar']) |
                                              Q(summary__contains=request.POST['searchBar']))
    allLogs = LocationLog.objects.all()
    context = {
        "search": geocode_result,
        "input": searchItem,
        # 'searchLogs': locationLogs,
        # 'allLogs': allLogs
        'allLogs': locationLogs
    }
    return render(request, 'travelApp/searchResults.html', context)


# log details page
def logDetails(request, logID):
    # get specific log
    log = LocationLog.objects.get(pk=logID)
    context = {
        'log': log,
    }
    return render(request, 'travelApp/logDetails.html', context)




