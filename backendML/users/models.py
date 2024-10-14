from django.db import models

# Create your models here.

class User(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    office_location = models.CharField(max_length=100)
    security_question = models.CharField(max_length=100)
    two_fa = models.BooleanField(default=False)

    class Meta:
        db_table = 'users'
