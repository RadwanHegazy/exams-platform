# Generated by Django 4.0 on 2023-03-20 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0003_student_question_details_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_question_details',
            name='date',
        ),
        migrations.AddField(
            model_name='student_exam_details',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
