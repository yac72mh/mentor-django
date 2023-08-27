from django.shortcuts import render , get_object_or_404
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
    first_page = 1
    last_page = courses.num_pages

    try:
        page_number = request.Get.get('page')
        courses = courses.get_pages(page_number)
    except EmptyPage:
        courses = courses.get_pages(1)
    except PageNotAnInteger:
        courses = courses.get_pages(1)


    context = {
        'courses': courses,
        'first_page' : first_page,
        'last_page': last_page,
        }                     
    return render (request , 'courses/courses.html', context=context)

def courses_details(request, id):
    courses = get_object_or_404(Courses, id=id)
    context = {
        'courses': courses,
        }                     
    return render (request , 'courses/courses-details.html', context=context)



