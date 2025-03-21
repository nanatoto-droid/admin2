from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    course = models.CharField(max_length=100)
    class_name = models.CharField(max_length=50,null=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')],null=True)

    enrollment_date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name

class SchoolImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='home_images/')

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    is_event = models.BooleanField(default=False)  # True if it's a school event
    event_date = models.DateField(null=True, blank=True)  # Event date (optional)

    def __str__(self):
        return self.title


