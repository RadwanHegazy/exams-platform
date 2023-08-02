from django.urls import path
from . import views




urlpatterns = [
    path('',views.index,name='index'),
    path('profile/',views.profile,name='profile'),
    path('update-info/',views.update_info,name='update_info'),
    path('update-password/',views.update_password,name='update_pas'),
    path('wrong-answers/',views.wrong_questions,name='wrong_answers')

]