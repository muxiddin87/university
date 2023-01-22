from django.db import models

class Speciality(models.Model):
    name = models.CharField(max_length=200)
    code = models.IntegerField()
    start_date = models.DateField()
    is_active = models.BooleanField()

    def __str__(self):
        return f"{self.name} {self.code} {self.start_date} {self.is_active}"




class Teacher(models.Model):
    PROFESSOR = "professor"
    RECTOR = "rector"
    DEGREE = (
        (PROFESSOR, "Professor"),
        (RECTOR, "Rector")
    )
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    degree = models.CharField(max_length=10,choices=DEGREE)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.degree}"


class Subject(models.Model):
    name = models.CharField(max_length=200)
    specialities = models.ManyToManyField(Speciality)
    teachers = models.ManyToManyField(Teacher)

    def __str__(self):
        return f"{self.name}"








