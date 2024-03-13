from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from . import forms,models
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from django.contrib import auth
from django.contrib.auth.decorators import login_required,user_passes_test
from datetime import datetime,timedelta,date
from django.core.mail import send_mail
from library_management_system.settings import EMAIL_HOST_USER


def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'librarySystem/index.html')

#for showing signup/login button for student
def studentclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'librarySystem/studentclick.html')

#for showing signup/login button for teacher
def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'librarySystem/adminclick.html')



def adminsignup_view(request):
    form=forms.AdminSigupForm()
    if request.method=='POST':
        form=forms.AdminSigupForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()


            my_admin_group = Group.objects.get_or_create(name='ADMIN')
            my_admin_group[0].user_set.add(user)

            return HttpResponseRedirect('adminlogin')
    return render(request,'librarySystem/adminsignup.html',{'form':form})






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
            my_student_group, _ = Group.objects.get_or_create(name='STUDENT')
            my_student_group.user_set.add(user)

            # Redirecting to the student login page upon successful signup
            return redirect('studentlogin')

    return render(request, 'librarySystem/studentsignup.html', context=mydict)




def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()

def afterlogin_view(request):
    if is_admin(request.user):
        return render(request,'librarySystem/adminafterlogin.html')
    else:
        return render(request,'librarySystem/studentafterlogin.html')


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def addbook_view(request):
    #now it is empty book form for sending to html
    form=forms.BookForm()
    if request.method=='POST':
        #now this form have data from html
        form=forms.BookForm(request.POST)
        if form.is_valid():
            user=form.save()
            return render(request,'librarySystem/bookadded.html')
    return render(request,'librarySystem/addbook.html',{'form':form})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def viewbook_view(request):
    books=models.Book.objects.all()
    return render(request,'librarySystem/viewbook.html',{'books':books})




@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def issuebook_view(request):
    form=forms.IssuedBookForm()
    if request.method=='POST':
        #now this form have data from html
        form=forms.IssuedBookForm(request.POST)
        if form.is_valid():
            obj=models.IssuedBook()
            obj.enrollment=request.POST.get('enrollment2')
            obj.book_isbn=request.POST.get('isbn2')    # This line might be causing the issue
            obj.save()
            return render(request,'librarySystem/bookissued.html')
    return render(request,'librarySystem/issuebook.html',{'form':form})



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def viewissuedbook_view(request):
    issuedbooks = models.IssuedBook.objects.all()
    li = []
    
    for ib in issuedbooks:
        issdate = str(ib.issuedate.day) + '-' + str(ib.issuedate.month) + '-' + str(ib.issuedate.year)
        expdate = str(ib.expirydate.day) + '-' + str(ib.expirydate.month) + '-' + str(ib.expirydate.year)
        
        # Fine calculation
        days = (date.today() - ib.issuedate)
        d = days.days
        fine = 0
        if d > 15:
            day = d - 15
            fine = day * 10

        books = list(models.Book.objects.filter(book_isbn=ib.book_isbn))
        students = list(models.StudentExtra.objects.filter(enrollment=ib.enrollment))

        # Iterate over pairs of books and students
        for book, student in zip(books, students):
            t = (student.get_name, student.enrollment, book.book_name, book.book_author, issdate, expdate, fine)
            li.append(t)

    return render(request, 'librarySystem/viewissuedbook.html', {'li': li})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def viewstudent_view(request):
    students=models.StudentExtra.objects.all()
    return render(request,'librarySystem/viewstudent.html',{'students':students})


@login_required(login_url='studentlogin')
def viewissuedbookbystudent(request):
    student_queryset = models.StudentExtra.objects.filter(user_id=request.user.id)
    
    # Check if the student exists
    if student_queryset.exists():
        student = student_queryset.first()
        issued_books = models.IssuedBook.objects.filter(enrollment=student.enrollment)

        li1 = []
        li2 = []

        for issued_book in issued_books:
            books = models.Book.objects.filter(isbn=issued_book.isbn)
            for book in books:
                t = (request.user, student.enrollment, student.branch, book.name, book.author)
                li1.append(t)
            issdate = f"{issued_book.issuedate.day}-{issued_book.issuedate.month}-{issued_book.issuedate.year}"
            expdate = f"{issued_book.expirydate.day}-{issued_book.expirydate.month}-{issued_book.expirydate.year}"

            # Fine calculation
            days = (date.today() - issued_book.issuedate).days
            fine = max(0, (days - 15) * 10) if days > 15 else 0

            t = (issdate, expdate, fine)
            li2.append(t)
    else:
        # If the student doesn't exist, set the lists to empty
        li1 = []
        li2 = []

    return render(request, 'librarySystem/viewissuedbookbystudent.html', {'li1': li1, 'li2': li2})

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
             send_mail(str(name)+' || '+str(email),message, EMAIL_HOST_USER, ['tesfayegebrehiwot123@gmail.com'], fail_silently = False)
           
        return render(request, 'librarySystem/contactussuccess.html')
    return render(request, 'librarySystem/contactus.html', {'form':sub})
