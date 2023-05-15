from django.shortcuts import render
from .models import Person


# Create your views here.
def team(request):
    persons = Person.objects.all()
    return render(request, "person/index.html", {"persons": persons})
