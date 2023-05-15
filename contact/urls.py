from django.conf.urls import url, include
from django.urls import path
from .views import contactus, all_contacts


app_name = "contact"

urlpatterns = [
    path('',  contactus, name="contactus"),
    path("list/", view=all_contacts, name="contactlist"),

]