from django.shortcuts import render
from .models import jobs

def home(request):
    Jobs  =  jobs.objects.all()
    return render(request,'jobs/home.html',{"Jobs":Jobs})
