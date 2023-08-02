from django.db import models
from app.models import Student, Exam, Question


class Student_Exam_Details (models.Model) :
    exam = models.ForeignKey(Exam,null=True,blank=True,on_delete=models.CASCADE)
    student = models.ForeignKey(Student,null=True,blank=True,on_delete=models.CASCADE)
    mark = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True,null=True)

    def __str__(self) :
        return f'{self.student}, {self.mark}'
    
class Student_Question_Details (models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE,null=True,blank=True)
    student = models.ForeignKey(Student,on_delete=models.CASCADE,null=True,blank=True)
    student_answer = models.CharField(max_length=100)
    correct_answer = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.student} | {self.question}'