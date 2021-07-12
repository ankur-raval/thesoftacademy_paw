from django.contrib import admin
from .models.student_reg import student_registration


class AdminStudentRegistration(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','contact']


admin.site.register(student_registration, AdminStudentRegistration)



