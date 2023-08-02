from django.db import models
from django.contrib.auth.models import AbstractUser






class Level (models.Model) :
    name = models.CharField(max_length=100)

    def __str__(self) : 
        return f'{self.name}'


class Student (AbstractUser) :
    level = models.ForeignKey(Level,null=True,blank=True,on_delete=models.CASCADE)
    email = models.EmailField(unique=True)


    def __str__(self) :
        return self.username





class Exam (models.Model) :
    name = models.CharField(max_length=500)
    level = models.ForeignKey(Level,on_delete=models.PROTECT)
    date = models.DateField(auto_now_add=True)
    total_questions = models.IntegerField(default=0)
    time = models.CharField(max_length=100,null=True,blank=True)
    can_view_correct_answer = models.BooleanField(default=False)

    def __str__(self) :
        return f' {self.level} | {self.name}'


class Question (models.Model) :
    exam = models.ForeignKey(Exam,on_delete=models.CASCADE)
    name = models.CharField(max_length=10000)
    c_1 = models.CharField(max_length=10000)
    c_2 = models.CharField(max_length=10000)
    c_3 = models.CharField(max_length=10000)
    c_4 = models.CharField(max_length=10000)
    note = models.CharField(max_length=10000,null=True,blank=True)
    choices = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
    )
    correct_choice = models.CharField(max_length=100,choices=choices,null=True,blank=True)

    def __str__(self) :
        return f'{self.name}'


class Round (models.Model) :
    exam = models.ManyToManyField(Exam,related_name='round_exams')
    max_roounds = models.IntegerField(default=0)
    name = models.CharField(max_length=10000,null=True,blank=True)

    def __str__(self) :
        return f'{self.name}'