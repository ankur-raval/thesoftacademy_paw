from django.db import models


class student_registration(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    email = models.EmailField()

    def register(self):
        self.save()
