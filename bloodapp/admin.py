from django.contrib import admin

# Register your models here.
from .models import Donor,Donation,Donation_Center,Bloodtype,Blood_Transfer

class DonorAdmin(admin.ModelAdmin):
    list_display = ("name","contact","email","birthdate","no_of_donations","address","gender")
admin.site.register(Donor,DonorAdmin)

class DonationAdmin(admin.ModelAdmin):
    list_display = ("quantity","donor_name","dntn_date","center")
admin.site.register(Donation,DonationAdmin)

class Donation_CenterAdmin(admin.ModelAdmin):
    list_display = ("center_name","location")
admin.site.register(Donation_Center,Donation_CenterAdmin)

class BloodtypeAdmin(admin.ModelAdmin):
    list_display = ("bloodtype","units_in_stock")
admin.site.register(Bloodtype,BloodtypeAdmin)

class Blood_TransferAdmin(admin.ModelAdmin):
    list_display = ("transfer_date","bloodtype","recipient_name","qty")
admin.site.register(Blood_Transfer,Blood_TransferAdmin)