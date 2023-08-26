from django.shortcuts import render
from .models import Services

def home(request):
    service = Services.objects.filter(status=True)
    context = {
        'service': service,
   }
    return render (request , "root/index.html", context= context)

def about(request):
    return render (request , "root/about.html")

def contact(request):
    return render (request , "root/contact.html")


