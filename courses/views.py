from django.shortcuts import render
from .models import Courses


def courses(request):
    courses = Courses.objects.all()
    context = {
        'courses': courses,
        }
    return render (request , 'courses/courses.html', context=context)

# Create your views here.
