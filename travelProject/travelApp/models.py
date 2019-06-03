from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# django user model
class UserModel(models.Model):
    username = models.CharField(max_length=500, default='')
    password = models.CharField(max_length=500, default='')
    email = models.EmailField(default='')
    user_fk = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.username


# location log
class LocationLog(models.Model):
    location = models.CharField(max_length=500, default='')
    location_lat = models.FloatField(default=0)
    location_long = models.FloatField(default=0)
    date_of_visit = models.DateTimeField(default=datetime.today)
    summary = models.TextField(default='')
    safety = models.IntegerField(default=0)
    affordability = models.IntegerField(default=0)
    accessibility = models.IntegerField(default=0)
    userModel_fk = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.location


# location rating
class LocationRating(models.Model):
    rating = models.IntegerField(default=0)
    locationModel_fk = models.ForeignKey(LocationLog, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.rating

