from django.contrib import admin

from .models import Teacher, Speciality, Subject

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    search_fields = ("first_name", "last_name")
    list_filter = ("degree",)

@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    search_fields = ("name", "code")


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name",)
    autocomplete_fields = ("specialities", "teachers")



