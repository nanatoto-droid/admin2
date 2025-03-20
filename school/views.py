
from django.shortcuts import render, redirect,get_object_or_404
from .models import Student, SchoolImage, News
from .forms import StudentForm
from  .forms import  NewsForm
from django.db.models import Count
def dashboard(request):
    students = Student.objects.all()  # Fetch all students
    news = News.objects.order_by('-date_posted')[:5]  # Fetch latest 5 news articles
    return render(request, 'dashboard.html', {'students': students, 'news': news})

def home(request):
    latest_news = News.objects.filter(is_event=False).order_by('-date_posted')[:3]
    upcoming_events = News.objects.filter(is_event=True).order_by('event_date')[:3]

    return render(request, 'home.html', {
        'latest_news': latest_news,
        'upcoming_events': upcoming_events})

def student_list(request):
    query = request.GET.get('search', '')
    students = Student.objects.filter(name__icontains=query) if query else Student.objects.all()
    return render(request, 'student_list.html', {'students': students, 'query': query})


def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})

def student_update(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_form.html', {'form': form, 'student': student})

def student_delete(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()
    return redirect('student_list')

def home(request):
    images = SchoolImage.objects.all()  # Fetch all uploaded images
    return render(request, 'home.html', {'images': images})

def news_list(request):
    news = News.objects.order_by('-date_posted')
    return render(request, 'news_list.html', {'news': news})
def add_news(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = NewsForm()
    return render(request, 'news_form.html', {'form': form})

def edit_news(request, news_id):
    news = get_object_or_404(News, id=news_id)
    if request.method == "POST":
        form = NewsForm(request.POST, instance=news)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = NewsForm(instance=news)
    return render(request, 'news_form.html', {'form': form})

def delete_news(request, news_id):
    news = get_object_or_404(News, id=news_id)
    if request.method == "POST":
        news.delete()
        return redirect('news_list')
    return render(request, 'news_confirm_delete.html', {'news': news})

def student_detail(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request, 'student_detail.html', {'student': student})



