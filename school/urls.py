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


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



