from django import forms
from datetime import date
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

    # validation
    def clean_safety(self):
        safety_data = self.cleaned_data['safety']
        if safety_data > 5:
            raise forms.ValidationError('Choose a number between 0 and 5')
        return safety_data

    def clean_affordability(self):
        affordability_data = self.cleaned_data['affordability']
        if affordability_data > 5:
            raise forms.ValidationError('Choose a number between 0 and 5')
        return affordability_data

    def clean_accessibility(self):
        accessibility_data = self.cleaned_data['accessibility']
        if accessibility_data > 5:
            raise forms.ValidationError('Choose a number between 0 and 5')
        return accessibility_data

    def clean_date_of_visit(self):
        date_of_visit_data = self.cleaned_data['date_of_visit']
        if date_of_visit_data > date.today():
            raise forms.ValidationError('Choose a valid date')
        return date_of_visit_data
