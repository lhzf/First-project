from django.forms import ModelForm
from bloodapp.models import Donor,Donation,Donation_Center,Bloodtype,Blood_Transfer

class DonorForm(ModelForm):
    class Meta:
        model = Donor
        fields = '__all__'

class DonationForm(ModelForm):
    class Meta:
        model = Donation
        fields = '__all__'        

class Donation_CenterForm(ModelForm):
    class Meta:
        model = Donation_Center
        fields = '__all__'       

class BloodtypeForm(ModelForm):
    class Meta:
        model = Bloodtype
        fields = '__all__'

class Blood_TransferForm(ModelForm):
    class Meta:
        model = Blood_Transfer
        fields = '__all__'