from . import views
from django.urls import path


urlpatterns = [
    path('enter-exam/<int:examid>/',views.enter_exam,name='enter_exam'),
    path('user-exams/',views.view_user_exams,name='user_exams'),
    path('user-exams/answer/<int:examid>/',views.view_exams_answers,name='exam_answers'),
]