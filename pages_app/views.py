from django.shortcuts import render, redirect



def index_view(request):
    return render(request, 'index.html')


def courses_view(request):
    return render(request, 'courses.html')

def free_session_view(request):
    return render(request, 'courses_list/free_session.html')

def basic_course_view(request):
    return render(request, 'courses_list/basic_course.html')

def advance_course_view(request):
    return render(request, 'courses_list/advance_course.html')

def events_view(request):
    return render(request, 'events.html')

def blogs_view(request):
    return render(request, 'blogs.html')

def contact_view(request):
    return render(request, 'contact.html')

def services_view(request):
    return render(request, 'services.html')


