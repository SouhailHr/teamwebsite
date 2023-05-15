from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Contact
from .forms import ContactForm


# Create your views here.

def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact/success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact/contact.html', context)


def all_contacts(request):
    contacts = Contact.objects.all()
    paginator = Paginator(contacts, 9)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request, "contact/allcontacts.html", {"contacts": contacts})
