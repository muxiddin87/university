from django.urls import path
from .views import speciality_view
from .views import teacher_view
from .views import subject_list
from .views import subject_detail, speciality_create, teacher_create, subject_create
urlpatterns = [

    path('speciality/', speciality_view, name='speciality'),
    path('teacher/', teacher_view, name='teacher'),
    path('', subject_list, name='subject-list'),
    path('subject/<int:pk>', subject_detail, name="subject-detail"),
    path('speciality/create/', speciality_create, name="speciality_create"),
    path('teacher/create/', teacher_create, name="teacher_create"),
    path('subject/create/', subject_create, name="subject_create")

           ]