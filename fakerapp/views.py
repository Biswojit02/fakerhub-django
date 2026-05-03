from django.shortcuts import render
from .models import Student

# Create your views here.

def student_data_view(request):
    student_list = Student.objects.all().order_by('name')
    # student_list = Student.objects.all()
    # student_list= Student.objects.filter(marks__gt=500)
    # student_list= Student.objects.filter(marks__lt=50)
    # student_list= Student.objects.filter(marks__gte=80)
    # student_list= Student.objects.filter(marks__lte=80)
    # student_list=Student.objects.filter(marks__range=(60,100))
    # student_list= Student.objects.filter(name__startswith='A')
    # student_list=Student.objects.filter(name__endswith='s')
    # student_list=Student.objects.filter(address__contains='p')
    # student_list=Student.objects.filter(address__icontains='P')
    # student_list=Student.objects.filter(email__iexact='xyz@gmail.com')
    # student_list = Student.objects.all().order_by('marks')
    # student_list = Student.objects.all().order_by('-marks')
    # student_list = Student.objects.all().order_by('-name')
    
    my_dict={'student_list': student_list}
    return render(request, 'fakerapp/student.html', context=my_dict)