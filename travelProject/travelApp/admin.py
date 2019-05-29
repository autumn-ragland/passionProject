from django.contrib import admin
from .models import UserModel, LocationLog, LocationRating


# Register your models here.
admin.site.register(UserModel)
admin.site.register(LocationLog)
admin.site.register(LocationRating)
