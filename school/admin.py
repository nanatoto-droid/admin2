
from django.contrib import admin
from .models import SchoolImage, Student
from .views import news_list

admin.site.register(SchoolImage)
admin.site.register(Student)
# admin.site.register(news_list(news_list))

# Register your models here.
