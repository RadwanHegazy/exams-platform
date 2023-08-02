from django.contrib import admin
from . import models
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {
            'fields': ( 'username','email','level')
        }),
    )


admin.site.unregister(Group)
admin.site.register(models.Student,CustomUserAdmin)
admin.site.register(models.Level)
admin.site.register(models.Exam)
admin.site.register(models.Question)
admin.site.register(models.Round)