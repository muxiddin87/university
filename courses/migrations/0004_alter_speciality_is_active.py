# Generated by Django 4.1 on 2022-09-27 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speciality',
            name='is_active',
            field=models.BooleanField(),
        ),
    ]