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
    donor_photo = models.ImageField(upload_to="images/")
    def __str__(self):
        return  f"{self.name}"

class Donation_Center(models.Model):
    center_name = models.CharField(max_length=50,verbose_name="Donation center")
    location = models.CharField(max_length=50,verbose_name="Location",null=True,blank=True,default="N/A")
    def __str__(self):
        return  f"{self.center_name}-{self.location}"

class Donation(models.Model):
    quantity = models.IntegerField()
    donor_name = models.ForeignKey(Donor,on_delete=models.CASCADE)
    dntn_date = models.DateField()
    center = models.ForeignKey(Donation_Center,on_delete=models.CASCADE)
    def __str__(self):
        return  f"{self.quantity}-{self.dntn_date}-{self.center}"

class Bloodtype(models.Model):
    bloodtype = models.CharField(max_length=5,verbose_name="Blood type")
    units_in_stock = models.IntegerField()
    def __str__(self):
        return  f"{self.bloodtype}"

class Blood_Transfer(models.Model):
    transfer_date = models.DateField()
    bloodtype = models.ForeignKey(Bloodtype,on_delete=models.CASCADE)
    recipient_name = models.CharField(max_length=50,verbose_name="Recipient name")
    qty = models.IntegerField()
    def __str__(self):
        return  f"{self.transfer_date}-{self.bloodtype}-{self.recipient_name}-{self.qty}"
