from django.shortcuts import render
from .models import Courses
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage


def courses(request , cat=None , teacher=None):
    if cat:
        courses = Courses.objects.filter(category__name=cat)
    elif teacher:
        courses = Courses.objects.filter(teacher__info__username=teacher)
    elif request.GET.get('search'):
        courses = Courses.objects.filter(content__contains=request.GET.get('search'))
    else:
        courses = Courses.objects.filter(status=True)
    
    
    courses = Paginator(courses, 2)
    try:
        page_number = request.Get.get('page')
        courses = courses.get_pages(page_number)
    except EmptyPage:
        courses = courses.get_pages(1)
    except PageNotAnInteger:
        courses = courses.get_pages(1)

    context = {
        'courses': courses,
        }                     
    return render (request , 'courses/courses.html', context=context)

# Create your views here.
