from django.conf.urls.static import static
from django.urls import path

from admin2 import settings
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.student_create, name='student_create'),
    path('students/edit/<int:pk>/', views.student_update, name='student_update'),
    path('students/delete/<int:pk>/', views.student_delete, name='student_delete'),
    path('news/', views.news_list, name='news_list'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('student/<int:student_id>/', views.student_detail, name='student_detail'),
    path('news/', views.news_list, name='news_list'),
    path('news/add/', views.add_news, name='add_news'),
    path('news/edit/<int:news_id>/', views.edit_news, name='edit_news'),
    path('news/delete/<int:news_id>/', views.delete_news, name='delete_news'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



