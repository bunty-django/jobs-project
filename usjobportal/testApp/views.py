from django.shortcuts import render
from testApp.models import *
# Create your views here.


def index(request):
    return render(request, 'testApp/home.html')


def hydjob(request):
    job_list = hydjobs.objects.order_by('date')
    my_dict = {'job_list': job_list}
    return render(request, 'testApp/hyd.html', context=my_dict)


def blrjob(request):
    job_list = blrjobs.objects.order_by('date')
    my_dict = {'job_list': job_list}
    return render(request, 'testApp/blr.html', context=my_dict)


def bbsjob(request):
    job_list = bbsjobs.objects.order_by('date')
    my_dict = {'job_list': job_list}
    return render(request, 'testApp/bbs.html', context=my_dict)