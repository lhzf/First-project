from django.db import models

# Create your models here.

class Donor(models.Model):
    Gender_Options = [("M","Male"),("F","Female"),]
    name = models.CharField(max_length=50,verbose_name="Donor name")
    contact = models.CharField(max_length=10)
    email = models.EmailField(max_length=200)
    birthdate = models.DateField(auto_now=False,auto_now_add=False)
    no_of_donations = models.IntegerField()
    address = models.CharField(max_length=100,null=True,blank=True,default="N/A")
    gender = models.CharField(max_length=2,choices=Gender_Options)

class Donation(models.Model):
    quantity = models.IntegerField()
    donor_name = models.ForeignKey(Donor,on_delete=models.CASCADE)
    dntn_date = models.DateField()
