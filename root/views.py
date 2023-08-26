from django.shortcuts import render
from .models import Services
from courses.models import Courses , Trainer

def home(request):
    service = Services.objects.filter(status=True)
    last_three_courses = Courses.objects.filter(status=True)[:3]
    last_three_Trainer = Trainer.objects.filter(status=True)[:3]
    context = {
        'service': service,
        'courses' : last_three_courses,
        'trainer': last_three_Trainer,
   }
    return render (request , "root/index.html", context= context)

def about(request):
    return render (request , "root/about.html")

def contact(request):
    return render (request , "root/contact.html")

def trainer(request):
    return render (request , "root/trainers.html")


