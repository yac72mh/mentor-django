from django.shortcuts import render

def courses(request):
    return render (request , 'course/courses.html')

# Create your views here.
