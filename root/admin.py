from django.contrib import admin
from .models import Services




class Adminservices(admin.ModelAdmin):
    list_display=['title','content']
    list_filter=['status']
    search_fields=['title']

 
admin.site.register(Services, Adminservices)
# Register your models here.
