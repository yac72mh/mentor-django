from django.shortcuts import render
from .models import Services
from courses.models import Courses , Trainer , Category

def home(request):
    category = Category.objects.all()
    service = Services.objects.filter(status=True)
    last_three_courses = Courses.objects.filter(status=True)[:3]
    last_three_Trainer = Trainer.objects.filter(status=True)[:3]
    context = {
        'service': service,
        'courses' : last_three_courses,
        'trainer': last_three_Trainer,
        'category' : category
   }
    return render (request , "root/index.html", context= context)

def about(request):
    category = Category.objects.all()
    context = {
        'category' : category
   }
    return render (request , "root/about.html", context= context)

def contact(request):
    context = {
        'category' : category
   }
    category = Category.objects.all()
    return render (request , "root/contact.html", context= context)

def trainer(request):
    context = {
        'category' : category
   }
    category = Category.objects.all()
    return render (request , "root/trainers.html", context= context)


