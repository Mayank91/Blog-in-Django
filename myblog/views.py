from django.shortcuts import render
from models import Contact
from django.views.generic import TemplateView
from models import Contact
from forms import ContactForm
from django.http import HttpResponse
import json
# Create your views here.
def home(request):
    context = {}
    context['all_obj'] = Contact.objects.all()
    return render(request,'index.html',context)

def post(request):
    form = ContactForm
    return render(request,'form.html',{'form' : form})

def contact(request):
    if request.method == 'POST':
        c = ContactForm(request.POST)
        if c.is_valid():
            # c.save()
            print c.cleaned_data
            return HttpResponse("hello" )