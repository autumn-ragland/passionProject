from django import forms
from .models import UserModel, LocationLog


# user form to add
class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        exclude = ['user_fk']


# log form to add
class LogForm(forms.ModelForm):
    class Meta:
        model = LocationLog
        exclude = ['userModel_fk']
