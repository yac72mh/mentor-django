from django.shortcuts import render
from .models import Services
from courses.models import Courses , Trainer , Category
from django.contrib.auth.models import User

def home(request):
    service_count = Services.objects.filter(status=True).count()
    course_count = Courses.objects.filter(status=True).count()
    trainer_count = Trainer.objects.filter(status=True).count()
    user_count = User.objects.filter(is_active=True).count()
    category = Category.objects.all()
    service = Services.objects.filter(status=True)
    last_three_courses = Courses.objects.filter(status=True)[:3]
    last_three_Trainer = Trainer.objects.filter(status=True)[:3]
    context = {
        'service': service,
        'courses' : last_three_courses,
        'trainer': last_three_Trainer,
        'category' : category,
        'sc' : service_count,
        'cc' : course_count,
        "tc" : trainer_count,
        'us' : user_count
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


