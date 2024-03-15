from django.shortcuts import render,redirect, reverse
from django.http import HttpResponseRedirect
from . import forms,models
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from django.contrib import auth
from django.contrib.auth.decorators import login_required,user_passes_test
from datetime import datetime,timedelta,date
from django.core.mail import send_mail
from library_management_system.settings import EMAIL_HOST_USER
from  django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login

def is_admin(user):
    return user.is_authenticated and user.is_admin

def is_authenticated(user):
    return user.is_authenticated

def index_view(request):
    return render(request,'librarySystem/index.html')

#for showing signup/login button for student
def studentclick_view(request):
    return render(request,'User/Student/studentclick.html')

#for showing signup/login button for teacher
def adminclick_view(request):
    return render(request,'User/Admin/adminclick.html')
def studentafterlogin_view(request):
    return render(request, 'User/Student/studentafterlogin.html')

def studentsignup_view(request):
    form1 = forms.StudentUserForm()
    form2 = forms.StudentExtraForm()
    mydict = {'form1': form1, 'form2': form2}

    if request.method == 'POST':
        form1 = forms.StudentUserForm(request.POST)
        form2 = forms.StudentExtraForm(request.POST)

        if form1.is_valid() and form2.is_valid():
            user = form1.save(commit=False)
            user.set_password(user.password)
            user.save()

            f2 = form2.save(commit=False)
            f2.user = user  # Assigning the User instance correctly.
            f2.save()

            # Assigning the user to the 'STUDENT' group
            # the two lines bellow cause errors 
            # my_student_group, _ = Group.objects.get_or_create(name='STUDENT')
            # my_student_group.user_set.add(user)

            # Redirecting to the student login page upon successful signup
            print("Redirecting to student_after_login page")
            return redirect(reverse('student_after_login'))
        else:
            mydict['form1'] = form1
            mydict['form2'] = form2
    else:
        form1 = forms.StudentUserForm()
        form2 = forms.StudentExtraForm()

    context = {'form1': form1, 'form2': form2}
    return render(request, 'User/Student/studentsignup.html', context)

    return render(request, 'User/Student/studentsignup.html', context=mydict)



def adminsignup_view(request):
    form = forms.AdminSigupForm()

    if request.method == 'POST':
        form = forms.AdminSigupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Assign user to 'ADMIN' group
            # admin_group, created = Group.objects.get_or_create(name='ADMIN')
            # user.groups.add(admin_group)

            from django.core.mail import send_mail
            send_mail(
                'New Admin Signup Approval Needed',
                f'Hi, a new admin with username {user.username} has signed up. Please approve their account.',
                # {user.email},
                ['bigidovi@gmail.com'],  # Superadmin's email
                fail_silently=False,
            )

            return redirect('admin_login')
    return render(request, 'User/Admin/adminsignup.html', {'form': form})


def student_login_view(request):
    error_message = None

    if request.method == 'POST':
        form = forms.StudentLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # login(request, user)
                return redirect(reverse('student_after_login'))
            else:
                error_message = "Invalid username or password."
        else:
            error_message = "Invalid form data. Please check your input."
    else:
        form = forms.StudentLoginForm()

    return render(request, 'User/Student/studentlogin.html', {'form': form, 'error_message': error_message})
    
def studentLogout(request):
    return render(request, 'User/Student/studentlogout.html')

def AdminLogin(request):
    return render(request, 'User/Admin/adminlogin.html')

@user_passes_test(is_admin)
def navbaradmin_view(request):
    return render(request, 'librarySystem/navbaradmin.html')

# @user_passes_test(is_authenticated)
def navbarstudent_view(request):
    return render(request, 'librarySystem/navbarstudent.html')


def aboutus_view(request):
    return render(request,'librarySystem/aboutus.html')

def contactus_view(request):
    sub = forms.ContactusForm()
    if request.method == 'POST':
        sub = forms.ContactusForm(request.POST)
        if sub.is_valid():
            email = sub.cleaned_data['Email']
            name=sub.cleaned_data['Name']
            message = sub.cleaned_data['Message']
        try:
            send_mail(
                str(name) + ' || ' + str(email),
                message,
                EMAIL_HOST_USER,
                ['bigidovi@gmail.com'], 
                fail_silently=False
            )
            return render(request, 'librarySystem/contactussuccess.html')
        except Exception as e:
            error_message = f"An error occurred while sending the email: {str(e)}"
            return render(request, 'librarySystem/contactus.html', {'form': sub, 'error_message': error_message})
    return render(request, 'librarySystem/contactus.html', {'form':sub})