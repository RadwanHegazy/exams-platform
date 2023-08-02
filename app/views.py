from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Student, Level, Exam, Round
from django.contrib.auth import authenticate
from django.contrib.auth.views import auth_login
from exam_app.models import Student_Question_Details, Student_Exam_Details
from django.core.paginator import Paginator

def index (request) :


    # start make round maker

    # round_range = 2
    # level = Level.objects.get( name = 'الصف الثالث الثانوي' )
    
    # exam = Exam.objects.filter( level = level)

    # pagin = Paginator( exam , per_page=round_range)

    # myRange = pagin.num_pages

    # for i in range(1,myRange) :
    #     print(i)
    #     pagin = Paginator( exam , per_page=round_range)
    #     pagin = pagin.get_page(i)
    
    #     for page in pagin.object_list :
    #         print(page.id)
    #     print('_'*20)




        
        
    # end round maker


    levels = Level.objects.all()

    
    level = levels[0]


    if 'level' in request.GET :
        level = Level.objects.get( name = request.GET['level'] )
    
    exams_list = {}

    students = Student.objects.filter( level = level )
    
    last_exam = Exam.objects.filter( level = level ).last()

    exams = Student_Exam_Details.objects.filter( exam = last_exam ).order_by('-mark')


    context = {}

    context['exams'] = exams
    context['levels'] = levels

    return render(request,'index.html',context)



@login_required
def wrong_questions (request) :
    
    context = {}

    student = request.user
    questions = Student_Question_Details.objects.filter( student = student ).exclude( is_correct = True )

    valid_data = []

    for question in questions :

        q = question.question

        choices = [
            q.c_1,
            q.c_2,
            q.c_3,
            q.c_4,
        ]

        correct_choice = question.correct_answer
        student_choice = question.student_answer


        new_questions = {
            'name' : q.name,
            'choices' : choices ,
            'correct' : correct_choice ,
            'student_answer' : student_choice ,
        }

        if q.note :
            new_questions['note'] = q.note

        if q.exam.can_view_correct_answer :
            valid_data.append(new_questions)


    context['questions'] = valid_data
    context['count'] = len(valid_data)
    

    return render(request,'wrong_questions.html',context) 

@login_required
def profile (request) :
    return render(request,'profile.html')


@login_required
def update_info (request) :

    if request.method == "POST" :
        
        username = request.POST['username']
        email = request.POST['email']

        user = request.user

        user.username = username
        user.email = email

        try :
            user.save()
        except Exception as error :
            return redirect('update_info')

        return redirect('profile')


    return render(request,'update-info.html')


@login_required
def update_password (request) :
    
    context = {}
    user = request.user

    if request.method == 'POST' :

        new_pas = request.POST['new_pas'] 
        new_pas_2 = request.POST['new_pas_2'] 

        if new_pas == new_pas :
            user.set_password(new_pas)
            user.save()

            auth_login(request,user)
            return redirect('profile')
        
        else :
            context['msg'] = 'كلمتي السر غير متطابقتين'
        
        

    return render(request,'update-pas.html',context)

