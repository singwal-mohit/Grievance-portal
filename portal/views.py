from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import *
from .forms import ComplaintForm, CreateUserForm
from .filters import ComplaintFilter
from .decorators import unauthenticated_user

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            username = form.cleaned_data.get('username')
            email=form.cleaned_data.get('email')
            group=Group.objects.get(name='student')
            user.groups.add(group)
            Student.objects.create(
                user=user,
                name=user.username,
                email=user.email,
            )                   
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')

    context = {
        'form': form
    }

    return render(request, 'register.html', context)

@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'username or password is incorrect')

    context = {}

    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home2')

def homePage(request):

    context = {}
    return render(request, 'home2.html', context)
 


@login_required(login_url='login')
def home(request):
    complaints = Complaint.objects.all()
    student = Student.objects.all()
    total_students = student.count()
    total_complaints = complaints.count()
    solved = complaints.filter(status='Solved').count()
    pending = complaints.filter(status='Pending').count()


    group=None
    if request.user.groups.exists():
        group=request.user.groups.all()[0].name

    if group == 'student':
        student=Student.objects.get(id=request.user.student.id)
        complaints = request.user.student.complaint_set.all()
        total_complaints = complaints.count()
        solved = complaints.filter(status='Solved').count()
        pending = complaints.filter(status='Pending').count()
        

        
    context = {
        'student': student,
        'complaints': complaints,
        'total_complaints': total_complaints,
        'solved': solved,
        'pending': pending
    }
    return render(request, 'dashboard.html', context)

@login_required(login_url='login')
def students(request, pk_test):
    student = Student.objects.get(id=pk_test)
    complaints = student.complaint_set.all()
    myFilter = ComplaintFilter(request.GET, queryset=complaints)
    complaints = myFilter.qs
    context = {
        'student': student,
        'complaints': complaints,
        'myFilter': myFilter
    }
    return render(request, 'student.html', context)

@login_required(login_url='login')
def complaintinfo(request, pk_test):
    complaint = Complaint.objects.get(id=pk_test)
    context = {
        'complaint': complaint
    }
    return render(request, 'complaints.html', context)

@login_required(login_url='login')
def createComplaint(request, pk):
    student = Student.objects.get(id=pk)
    form = ComplaintForm(initial={'student': student})

    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form,
        'student': student
    }
    return render(request, 'complaint_form.html', context)

@login_required(login_url='login')
def updateComplaint(request, pk):

    complaint = Complaint.objects.get(id=pk)
    form = ComplaintForm(instance=complaint)

    context = {'form': form}
    if request.method == 'POST':
        form = ComplaintForm(request.POST, instance=complaint)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'complaint_form.html', context)

@login_required(login_url='login')
def deleteComplaint(request, pk):
    complaint = Complaint.objects.get(id=pk)
    context = {
        'item': complaint
    }

    if request.method == 'POST':
        complaint.delete()
        return redirect('home')

    return render(request, 'delete_complaint.html', context)
