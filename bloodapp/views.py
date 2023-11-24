from django.shortcuts import render,redirect
from bloodapp.forms import DonorForm,DonationForm,Donation_CenterForm,BloodtypeForm,Blood_TransferForm
from bloodapp.models import Donor,Donation,Donation_Center,Bloodtype,Blood_Transfer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required
def index_view(request):
    return render(request, 'index.html')

@login_required
def tables_view(request):
    return render(request, 'tables.html')

@login_required
def add_donor_view(request):
    message = ''
    if request.method == "POST":
        donor_form = DonorForm(request.POST,request.FILES)

        if donor_form.is_valid():
            donor_form.save()
            messages.success(request,"Donor added successfully")
    
    donor_form = DonorForm()
    donors = Donor.objects.all() 
    context = {
        'form':donor_form,
        'msg': message,
        'donors': donors
    }
    

    return render(request, "add_donor.html", context)

@login_required
def add_donation_view(request):
    message = ''
    if request.method == "POST":
        donation_form = DonationForm(request.POST)

        if donation_form.is_valid():
            donation_form.save()
            messages.success(request,"Donation added successfully")
    
    donation_form = DonationForm()
    donations = Donation.objects.all()
    context = {
        'form':donation_form,
        'msg': message,
        'donations': donations
    }

    return render(request, "add_donation.html", context)

@login_required
def add_center_view(request):
    message = ''
    if request.method == "POST":
        center_form = Donation_CenterForm(request.POST)

        if center_form.is_valid():
            center_form.save()
            messages.success(request,"Center added successfully")
    
    center_form = Donation_CenterForm()
    centers = Donation_Center.objects.all()
    context = {
        'form':center_form,
        'msg': message,
        'centers': centers
    }

    return render(request, "add_center.html", context)

@login_required
def add_bloodtype_view(request):
    message = ''
    if request.method == "POST":
        bloodtype_form = BloodtypeForm(request.POST)

        if bloodtype_form.is_valid():
            bloodtype_form.save()
            messages.success(request,"Bloodtype added successfully")
    
    bloodtype_form = BloodtypeForm()
    bloodtypes = Bloodtype.objects.all()
    context = {
        'form':bloodtype_form,
        'msg': message,
        'bloodtypes': bloodtypes
    }

    return render(request, "add_bloodtype.html", context)

@login_required
def add_transfer_view(request):
    message = ''
    if request.method == "POST":
        transfer_form = Blood_TransferForm(request.POST)

        if transfer_form.is_valid():
            transfer_form.save()
            messages.success(request,"Transfer added successfully")
    
    transfer_form = Blood_TransferForm()
    transfers = Blood_Transfer.objects.all()
    context = {
        'form':transfer_form,
        'msg': message,
        'transfers':transfers
    }

    return render(request, "add_transfer.html", context)

@login_required
def edit_donor_view(request, donor_id):
    message=''
    donor = Donor.objects.get(id=donor_id)

    if request.method == "POST":
        donor_form = DonorForm(request.POST, request.FILES, instance=donor)

        if donor_form.is_valid():
            donor_form.save()
            message = "changes saved successfully"
            return redirect(add_donor_view)
        else:
            message = "Form has invalid data"
    else:
        donor_form = DonorForm(instance = donor)

    context = {
        'form': donor_form,
        'donor': donor,
        'message':message
    }
    return render(request,'edit_donor.html',context)

@login_required
def edit_donation_view(request, donation_id):
    message=''
    donation = Donation.objects.get(id=donation_id)

    if request.method == "POST":
        donation_form = DonationForm(request.POST, instance=donation)
       
        if donation_form.is_valid():
            donation_form.save()
            message = "changes saved successfully"
            return redirect(add_donation_view)
        else:
            message = "Form has invalid data"
    else:
        donation_form = DonationForm(instance = donation)

    context = {
        'form': donation_form,
        'donation': donation,
        'message':message
    }
    return render(request,'edit_donation.html',context)

@login_required
def edit_center_view(request, center_id):
    message=''
    center = Donation_Center.objects.get(id=center_id)

    if request.method == "POST":
        center_form.save()
        center_form = Donation_CenterForm(request.POST, instance=center)

        if center_form.is_valid():
            message = "changes saved successfully"
            center_form.save()
        else:
            message = "Form has invalid data"
            return redirect(add_center_view)
    else:
        center_form = Donation_CenterForm(instance = center)

    context = {
        'form': center_form,
        'center': center,
        'message':message
    }
    return render(request,'edit_center.html',context)

@login_required
def edit_bloodtype_view(request, bloodtype_id):
    message=''
    bloodtype = Bloodtype.objects.get(id=bloodtype_id)

    if request.method == "POST":
        bloodtype_form = BloodtypeForm(request.POST,instance=bloodtype)
        

        if bloodtype_form.is_valid():
            bloodtype_form.save()
            message = "changes saved successfully"
            return redirect(add_bloodtype_view)
        else:
            message = "Form has invalid data"
    else:
        bloodtype_form = BloodtypeForm(instance = bloodtype)

    context = {
        'form': bloodtype_form,
        'bloodtype': bloodtype,
        'message':message
    }
    return render(request,'edit_bloodtype.html',context)

@login_required
def edit_transfer_view(request, transfer_id):
    message=''
    transfer = Blood_Transfer.objects.get(id=transfer_id)

    if request.method == "POST":
        transfer_form = Blood_TransferForm(request.POST,instance=transfer)

        if transfer_form.is_valid():
            transfer_form.save()
            message = "changes saved successfully"
            return redirect(add_transfer_view)
        else:
            message = "Form has invalid data"
    else:
        transfer_form = Blood_TransferForm(instance = transfer)

    context = {
        'form': transfer_form,
        'transfer': transfer,
        'message':message
    }
    return render(request,'edit_transfer.html',context)

def delete_donor_view(request,donor_id):
    donor = Donor.objects.get(id=donor_id)
    donor.delete()
    return redirect(add_donor_view)

def delete_donation_view(request,donation_id):
    donation = Donation.objects.get(id=donation_id)
    donation.delete()
    return redirect(add_donation_view)

def delete_center_view(request,center_id):
    donation = Donation_Center.objects.get(id=center_id)
    donation.delete()
    return redirect(add_center_view)

def delete_bloodtype_view(request,bloodtype_id):
    bloodtype = Bloodtype.objects.get(id=bloodtype_id)
    bloodtype.delete()
    return redirect(add_bloodtype_view)

def delete_transfer_view(request,transfer_id):
    transfer = Blood_Transfer.objects.get(id=transfer_id)
    transfer.delete()
    return redirect(add_transfer_view)

def signup_view(request):
    if request.method == "POST":
        signup_form = UserCreationForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            message = 'User created sussessfully'
        else:
            message = 'Something went wrong'
    else:
        signup_form = UserCreationForm()

    context = {
        'form': signup_form,  
    }
            
    return render(request,'registration/signup.html',context)
