from django.contrib import admin

# Register your models here.
from .models import Donor,Donation

class DonorAdmin(admin.ModelAdmin):
    list_display = ("name","contact","email","birthdate","no_of_donations","address","gender")
admin.site.register(Donor,DonorAdmin)