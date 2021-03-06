from django.shortcuts import render
from .models import TeachersInfo
from django.views.generic import DetailView

# Create your views here.


def teacher_hsc(request):
	context = {
		'teacher_details' : TeachersInfo.objects.filter(level="hsc").order_by('hsc_year'),
		'flag' : True
	}
	return render(request, 'teacher/teacher.html', context)


def teacher_ssc(request):
	context = {
		'teacher_details' : TeachersInfo.objects.filter(level="ssc").order_by('hsc_year')
	}
	return render(request, 'teacher/teacher.html', context)


class TeacherDetialsView(DetailView):
	model = TeachersInfo



