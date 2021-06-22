# Generated by Django 3.1.7 on 2021-05-02 19:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0007_student_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.CharField(max_length=200, null=True, validators=[django.core.validators.EmailValidator('Email is not valid')]),
        ),
    ]
