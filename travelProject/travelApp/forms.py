from django import forms
from .models import UserModel


# user form to add
class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        exclude = ['user_fk']
