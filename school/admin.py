
from django.contrib import admin
from .models import SchoolImage, Student,News
from .views import news_list

admin.site.register(SchoolImage)
admin.site.register(Student)
# admin.site.register(News)
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_event', 'event_date', 'date_posted')
    search_fields = ('title', 'content')
    list_filter = ('is_event', 'date_posted')
    ordering = ('-date_posted',)
