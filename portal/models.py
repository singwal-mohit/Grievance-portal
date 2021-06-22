from django.db import models
from django.contrib.auth.models import User
from django.core.validators import EmailValidator,validate_email

# Create your models here.
class Student(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=10, null=True)
    email = models.CharField(max_length=200, null=True,validators=[EmailValidator("Email is not valid")])
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Complaint(models.Model):
    title = models.CharField(max_length=200)
    Area_choices= (
        ('Hostel','Hostel'),
        ('Academics','Academics'),
        ('Administrative','Administrative'),
        ('N','none'),
    )
    area=models.CharField(max_length=25,choices=Area_choices,default='N')

    Department_choice=(
        ('Computer Engineering' ,'Computer Engineering'),
        ('Electronics Engineering','Electronics Engineering'),
        ('Electrical Engineering','Electrical Engineering'),
        ('Civil Engineering','Civil Engineering'),
        ('Information Technology','Information Technology'),
        ('None','None'),

    )
    STATUS=(
        ('Pending','Pending'),
        ('Solved','Solved'),
    )
    status=models.CharField(max_length=8,null=True,choices=STATUS,default='Pending')
    Department=models.CharField(max_length=35,choices=Department_choice,default='N')
    details = models.TextField(blank=True)
    pub_date = models.DateTimeField(auto_now=True)
    student=models.ForeignKey(Student,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.title






