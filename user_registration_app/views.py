from django.shortcuts import render , redirect , HttpResponseRedirect
from .models.student_reg import student_registration
from pages_app.views import index_view


def student_registration_view(request):
    if request.method == 'GET':
        return render(request, 'student_registration.html')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')

        new_student = student_registration(first_name=first_name, last_name=last_name, email=email, contact=contact)
        new_student.register()
        return redirect(index_view)


