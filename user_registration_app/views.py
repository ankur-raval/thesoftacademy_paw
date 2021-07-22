from django.http.response import HttpResponse
from django.shortcuts import render , redirect , HttpResponseRedirect
from .models.student_reg import student_registration
from .models.free_session_registration import free_session_registration
from pages_app.views import index_view
from django.contrib.auth.hashers import make_password, check_password
import random
import string
from django.contrib import messages



def free_session_reg_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        time_slot = request.POST.get('time_slot')
        email = request.POST.get('email')
        contact = request.POST.get('contact')        

        try:
            if free_session_registration.objects.get(email=email):
                messages.error(request, 'You have already registered. Please Check your email for ZOOM meeting link...')            
                return redirect(index_view)
        except:
            free_user = free_session_registration(first_name=first_name, last_name=last_name, city=city, state=state, country=country, 
                                            time_slot=time_slot, email=email, contact=contact)
            free_user.register()
            messages.success(request, 'Welcome... You have successfully registered our FREE SESSION. We will send you a link via email for ZOOM meeting. Thank You...')
            return render(request, 'free_session_registration.html')
    else:
        return render(request, 'free_session_registration.html')






def student_registration_view(request):
    error_msg = None
    if request.method == 'GET':
        return render(request, 'student_registration.html')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        length = 8
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        num = string.digits
        symbols = string.punctuation
        all = lower + upper + num + symbols
        temp = random.sample(all,length)
        password = "".join(temp)
        all = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.sample(all,length))



        try:
            if student_registration.objects.get(email=email):
                error_msg = "Email is already taken..."
                return render(request, 'student_registration.html', {'error':error_msg})
        except:       
            new_student = student_registration(first_name=first_name, last_name=last_name, email=email, contact=contact, password=password)
            new_student.register()
            return redirect(login_view)


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        error_msg_login = None
        student = student_registration.objects.filter(email=email)
        if student:
            flag = check_password(password, student_registration.password)
            if flag:
                # request.session['student_registration.id'] = student.id
                # request.session['email'] = student.email
                print('login successfully...')
                return redirect(index_view)
            else:
                error_msg_login = 'Invalid Credencials...'
                print('Invalid Credencials...')
                return render(request, 'login.html', {'error_msg_login':error_msg_login})
        else:
            error_msg_login = 'Invaid Credencials...'
            return render(request, 'login.html', {'error_msg_login':error_msg_login})
    else:
        return render(request, 'login.html')


