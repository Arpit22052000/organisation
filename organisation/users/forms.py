from django import (
    forms,
)  # this imports forms module from django web framework, used to handle html using python
from .models import CustomUser, Notes  # imports CustomUser from models

from django.contrib.auth.forms import (
    UserCreationForm,
)  # used for django user registration and account creation, it includes fields such as username and password and handles the necessary validation

from django.forms import ModelForm  # importing model form module from django.forms

from django.urls import reverse_lazy


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)


# UserCreationForm is class that checks the username and doesn't let allow similar username even with case(i.e, Arpit is same as arpit)
class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser  # the form is associated with the CustomUser model, meaning that when the form is submitted, it will create or update instances of the CustomUser model in the database. so when we will se in admin, then in customuser we will have and updated cutomuser database.
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "pet_name",
        ]  # the form will have these fields


# writing the notes class imported from models


class NotesForm(ModelForm):
    class Meta:
        model = Notes  # when we will make a notes, then it will be saved in notes database, as seen before in regostration form (the model is of Notes)
        fields = ["notes"]  # these are the fields of the notes


class PasswordResetForm(forms.Form):
    email = forms.EmailField()
    pet_name = forms.CharField(max_length=50)


class PasswordResetDoneForm(forms.Form):
    username = forms.CharField(disabled=True)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
