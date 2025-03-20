from django import forms
from .models import Student
from .models import News
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'
