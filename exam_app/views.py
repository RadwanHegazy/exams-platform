from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from app.models import Exam, Question
from django.views.decorators.csrf import csrf_exempt
from .models import Student_Exam_Details, Student_Question_Details




@csrf_exempt
@login_required
def enter_exam(request, examid) :
    
    student = request.user

    context = {}

    get_exam = get_object_or_404(Exam,id=examid)
    
    if request.method == "POST" :

        all_questions = request.POST.getlist('questions[]')
        all_answers = request.POST.getlist('answers[]')


        total_mark = 0
        total_question_number = len(all_questions)

        for i in range(0,len(all_answers)):
            
            q_id = all_questions[i]
            student_answer = str(all_answers[i]).split(')')[0]

            get_q = Question.objects.get( id = q_id )

            all_question_choices = [
                get_q.c_1,
                get_q.c_2,
                get_q.c_3,
                get_q.c_4,
            ]


            details = Student_Question_Details.objects.create(
                question = get_q,
                student_answer = all_question_choices[int(student_answer) - 1],
                correct_answer = all_question_choices[int(get_q.correct_choice) - 1] ,
                student = student ,
            )

            if get_q.correct_choice == student_answer :
                total_mark = total_mark + 1
                details.is_correct = True
            
            details.save()


        Student_Exam_Details.objects.create(
            student = student,
            exam = get_exam,
            mark = f'{total_mark} / {total_question_number}'
        ).save()


            


    if student.level == get_exam.level and Student_Exam_Details.objects.filter( student = student, exam = get_exam).exists() == False :
        
    
        questions = Question.objects.filter(exam=get_exam).order_by('-id')

        context['questions'] = questions
        context['exam'] = get_exam



    else:
        return redirect('user_exams')

    return render(request,'exam_app/enter-exam.html',context)




@login_required
def view_user_exams (request) :
    

    student = request.user
    
    exams = Student_Exam_Details.objects.filter( student = student ).order_by('-id')

    context = {
        'exams' : exams
    }

    return render(request,'exam_app/user-exams.html',context)


@login_required
def view_exams_answers (request,examid) :

    exam = get_object_or_404( Exam, id = examid )

    if exam.can_view_correct_answer is not True :
        return redirect('user_exams')
    
    questions = Question.objects.filter( exam = exam ).order_by('-id')

    student = request.user

    invalid_questions = []

    for question in questions :
        
        answers = [
            question.c_1,
            question.c_2,
            question.c_3,
            question.c_4,
        ]

        correct_answer  = answers[ int( question.correct_choice)  - 1 ]


        student_answer = Student_Question_Details.objects.get( question = question , student = student )
        
        data =  {
            'name' : question.name,
            'choices' : answers,
            'correct' : correct_answer,
        }

        if question.note :
            data['note'] = question.note

        if student_answer.is_correct == False:
            data['student_answer'] = student_answer.student_answer

        invalid_questions.append(data)
    
    return render(request,'exam_app/exam-answers.html',{'questions':invalid_questions,'exam':exam})



