from django.db import models
import datetime
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=150) 
    def __str__(self):
        return self.name
    
class Skills(models.Model):
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name
    
class Trainer(models.Model):
    info = models.ForeignKey(User , on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skills)
    description = models.TextField()
    image = models.ImageField(upload_to='trainer', default='teacher.jpg') 
    twiter = models.CharField(max_length=255, default='#')
    instagram = models.CharField(max_length=255, default='#')
    facebook = models.CharField(max_length=255, default='#')
    linkdine = models.CharField(max_length=255, default='#')
    statuse = models.BooleanField(default=False)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.info.username

class Courses(models.Model):
    image = models.ImageField(upload_to='courses', default='default.jpg')
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=100)
    content = models.TextField()
    price = models.IntegerField(default=0)
    teacher = models.ForeignKey(Trainer , on_delete=models.CASCADE)
    counted_views = models.IntegerField(default=0)
    counted_like = models.IntegerField(default=0)
    available_seat = models.IntegerField(default=0)
    schedule = models.DateField(default=datetime.datetime.now())
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        ordering = ('-created_date',)
    def __str__(self):
        return self.title
