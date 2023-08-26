from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=150) 
    def __str__(self):
        return self.name

class Courses(models.Model):
    image = models.ImageField(upload_to='courses', default='default.jpg')
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=100)
    content = models.TextField()
    price = models.IntegerField(default=0)
    teacher = models.CharField(max_length=50)




    def __str__(self):
        return self.title
