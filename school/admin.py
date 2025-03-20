
from django.contrib import admin
from .models import SchoolImage, Student,News
from .views import news_list

admin.site.register(SchoolImage)
admin.site.register(Student)
admin.site.register(News)

