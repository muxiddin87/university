# Generated by Django 4.1 on 2022-09-27 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('code', models.IntegerField(max_length=512)),
                ('start_date', models.DateField()),
                ('is_active', models.CharField(max_length=200)),
            ],
        ),
    ]
