from django import forms
from django.forms import ModelForm
from .models import Teacher,Subject

class SpecialityForm(forms.Form):
    name = forms.CharField(max_length=200)
    code = forms.IntegerField()
    start_date = forms.DateField()
    is_active = forms.BooleanField()

class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'


class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'

