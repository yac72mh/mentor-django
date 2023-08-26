from django.db import models

class Courses(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    price = models.IntegerField(default=0)


def __str__(self):
    return self.title
