"""
URL configuration for djblood project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include 
from django.conf import settings
from django.conf.urls.static import static
from bloodapp.views import index_view,tables_view,add_donor_view,add_donation_view,add_center_view,add_bloodtype_view,add_transfer_view,edit_donor_view,edit_donation_view,edit_center_view,edit_bloodtype_view,edit_transfer_view,delete_donor_view,delete_donation_view,delete_center_view,delete_transfer_view,delete_bloodtype_view,signup_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index_view,name='homepage'),
    path('signup/',signup_view,name='signup_page'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('page2/',tables_view,name='page two'),
    path('add_donor/',add_donor_view,name="add_donor_page"),
    path('add_donation/',add_donation_view,name="add_donation_page"),
    path('add_center/',add_center_view,name="add_center_page"),
    path('add_bloodtype/',add_bloodtype_view,name="add_bloodtype_page"),
    path('add_transfer/',add_transfer_view,name="add_transfer_page"),
    path('edit_donor/<int:donor_id>/',edit_donor_view,name="edit_donor_page"),
    path('edit_donation/<int:donation_id>/',edit_donation_view,name="edit_donation_page"),
    path('edit_center/<int:center_id>/',edit_center_view,name="edit_center_page"),
    path('edit_bloodtype/<int:bloodtype_id>/',edit_bloodtype_view,name="edit_bloodtype_page"),
    path('edit_transfer/<int:transfer_id>/',edit_transfer_view,name="edit_transfer_page"),
    path('delete_donor/<int:donor_id>/',delete_donor_view,name="delete_donor_page"),
    path('delete_donation/<int:donation_id>/',delete_donation_view,name="delete_donation_page"),
    path('delete_center/<int:center_id>/',delete_center_view,name="delete_center_page"),
    path('delete_bloodtype/<int:bloodtype_id>/',delete_bloodtype_view,name="delete_bloodtype_page"),
    path('delete_transfer/<int:transfer_id>/',delete_transfer_view,name="delete_transfer_page"),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)