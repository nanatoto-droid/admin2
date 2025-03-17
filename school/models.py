from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class SchoolImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='home_images/')

    def __str__(self):
        return self.title
