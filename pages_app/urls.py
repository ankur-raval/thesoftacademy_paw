from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index_view,name='index'),
    path('courses',views.courses_view,name='courses'),
    path('free_session',views.free_session_view,name='free_session'),
    path('basic_course',views.basic_course_view,name='basic_course'),
    path('advance_course',views.advance_course_view,name='advance_course'),
    path('events',views.events_view,name='events'),
    path('blogs',views.blogs_view,name='blogs'),
    path('contact',views.contact_view,name='contact'),
    path('services',views.services_view,name='services'),








    





    
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)