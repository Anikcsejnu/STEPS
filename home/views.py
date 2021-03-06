from django.shortcuts import render
from course.models import Tutorial, Course
from teacher.models import TeachersInfo
import random


# Create your views here.

def index(request):
	return render(request, 'home/index.html')


def about(request):
	#print(TeachersInfo.objects.all().count(), Tutorial.objects.all().count())
	context = {
		'number_of_teacher':TeachersInfo.objects.all().count(),
		'number_of_course' : Course.objects.all().count(),
		'number_of_tutorial':Tutorial.objects.all().count(),
	}
	return render(request, 'home/about.html', context)


def developer(request):
	return render(request, 'home/developer.html')




