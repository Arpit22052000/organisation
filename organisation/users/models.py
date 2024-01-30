from django.db import models
from django.contrib.auth.models import AbstractUser

# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from django.contrib import admin


# The common codes in all the classes are written in this method
class BaseModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True
    )  # auto_now_add, saves the date and time only once that is when the instance is created.
    updated_at = models.DateTimeField(
        auto_now=True
    )  # but auto_now saves the date and time all the time when they get updated

    class Meta:
        abstract = True


# Create your models here.
class Organisation(BaseModel):
    name = models.CharField(max_length=100, default="NULL")
    department = models.CharField(max_length=50)
    number_of_employees = models.IntegerField()
    location = models.CharField(max_length=100, blank=True)
    NetWorth_in_Cr = models.IntegerField()
    ceo = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    # The meta class are made to do other things such as verbose etc..
    class Meta:
        verbose_name = "CustomUser"

    role_choices = ((1, "HR"), (2, "Lead"), (3, "Director"))
    role = models.IntegerField(choices=role_choices, default=1)
    pet_name = models.CharField(max_length=50, unique=True, null=False)


class Notes(BaseModel):
    notes = models.TextField()
    employee = models.ForeignKey(CustomUser, default=1, on_delete=models.CASCADE)
