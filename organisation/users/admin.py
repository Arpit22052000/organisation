from django.contrib import admin
from .models import Organisation, CustomUser, Notes

# Register your models here.
admin.site.register(Organisation)
admin.site.register(CustomUser)
admin.site.register(Notes)
