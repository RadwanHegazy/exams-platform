from django.shortcuts import render, redirect
from app.models import Student, Level
from django.contrib.auth.views import auth_login
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


# Create your views here.



def register (request) :
    
    context = {

        'levels':Level.objects.all()
    
    }


    if request.method == 'POST' :



        username = request.POST['username']
        password = request.POST['password']
        level = request.POST['level']
        email = request.POST['email']

        student = Student.objects

        if student.filter(username=username).exists() :
            
            context['msg'] = 'اسم المستخدم هذا موجود بالفعل جرب  اسم  مستخدم اخر'
        elif student.filter(email=email).exists():
            context['msg'] = 'الايميل هذا موجود بالفعل جرب  ايميل اخر'

        else:
            student = student.create(
                username = username,
                email = email,
                level = Level.objects.get(name=level),
            )
            
            student.set_password(password)

            student.save()



            auth_login(request,student)
            
            return redirect('index')


        
    return render(request,'auth/register.html',context)


def login (request) :
    
    context = {}
    
    if request.method == 'POST' :

        email = request.POST['email']
        password = request.POST['password']

        student = Student.objects

        if student.filter(email=email).exists() :
            
            student = student.filter(email=email).first()

            auth = authenticate(username=student.username,password=password)


            if auth is not None :

                auth_login(request,student)

                return redirect('profile')

            else:

                context['msg'] = 'البيانات التي ادخلتها غير صحيحة'
            
        else:
            context['msg'] = 'البيانات التي ادخلتها غير صحيحة'


    return render(request,'auth/login.html',context)
