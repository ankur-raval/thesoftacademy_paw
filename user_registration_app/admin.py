from django.contrib import admin
from .models.student_reg import student_registration
from .models.free_session_registration import free_session_registration


class AdminStudentRegistration(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','contact']

class AdminFreeRegistration(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','contact', 'time_slot', 'city', 'state' , 'country']


admin.site.register(student_registration, AdminStudentRegistration)
admin.site.register(free_session_registration, AdminFreeRegistration)




