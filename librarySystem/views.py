from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'dashbord/index.html')
def staff(request):
    return render(request, 'dashbord/staff.html')
