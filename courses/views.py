from django.shortcuts import render,redirect
from .models import Speciality
from .models import Teacher
from .models import Subject
from .forms import SpecialityForm
from .forms import TeacherForm
from .forms import SubjectForm
from  django.http import HttpResponse

"""def hello_world(request):
    name = request.GET.get('name', 'Django')
    return render (request,'courses/home.html', {'name' :name})"""

def speciality_view(request):
    specialities = Speciality.objects.all()
    return render(request, 'courses/speciality.html', {'specialities' :specialities,})


def teacher_view(request):
    search = request.GET.get('search')
    if search is None:
        teachers = Teacher.objects.all()
    else:
        teachers = Teacher.objects.filter(first_name__contains=search)
    #if len(teachers) == 0:
        #return HttpResponse('No teachers')
    return render(request, 'courses/teacher.html', {'teachers': teachers, })


def subject_detail(request, pk):
    subject = Subject.objects.get(pk=pk)
    teachers = subject.teachers.all()
    specialities = subject.specialities.all()
    return render(request, 'courses/subject_info.html', {'subject': subject, 'teachers': teachers, 'specialities': specialities})

def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'courses/subject.html', {'subjects': subjects, })


def speciality_create(request):
    if request.method == 'GET':
        form = SpecialityForm
    else:
        form = SpecialityForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Speciality.objects.create(
                name=data['name'],
                code=data['code'],
                start_date=data['start_date'],
                is_active=data['is_active']
            )
            return redirect("speciality")
    return render(request, 'courses/speciality_create.html', {"form": form,})

    form = SpecialityForm(request.POST)
    print(form.is_valid())
    print(form.cleaned_data)
    return render(request, 'courses/speciality_create.html', {"form": form, })

def teacher_create(request):
    form = TeacherForm()
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher')

    context = {'form' :form}
    return render(request, 'courses/teacher_create.html', context)

def subject_create(request):
    form = SubjectForm()
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subject-list')

    context = {'form' :form}
    return render(request, 'courses/subject_create.html', context)







