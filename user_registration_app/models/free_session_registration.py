from django.db import models



class free_session_registration(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    email = models.EmailField()
    time_slot = models.CharField(max_length=100,default=None)

    
    def register(self):
        self.save()


    # @staticmethod
    # def get_student_by_email(email):
    #     try:
    #         return student_registration.objects.get(email=email)
    #     except:
    #         return False

   
