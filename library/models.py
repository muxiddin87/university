from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=512)
    author = models.CharField(max_length=512)
    count = models.IntegerField(default=1)
    class Meta:
        db_table = 'books'

TEACHER = "teacher"
STUDENT = "student"
ROLES = (

    (STUDENT,"Student"),
    (TEACHER,"Teacher")

)

class User(models.Model):
    role = models.CharField(max_length=10,choices=ROLES)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)


