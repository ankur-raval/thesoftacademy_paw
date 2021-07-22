from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('registration',views.student_registration_view,name='registration'),
    path('free_session_registartion',views.free_session_reg_view,name='free_session_registartion'),
    path('login',views.login_view,name='login'),


    





    
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)