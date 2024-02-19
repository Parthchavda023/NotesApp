from django.db import models

# Create your models here.
class signupModel(models.Model):
    ctrated = models.DateTimeField(auto_now_add = True)

    firstname = models.CharField(max_length = 18)
    lastname = models.CharField(max_length = 18)
    username = models.EmailField()
    password = models.CharField(max_length = 18)
    city = models.CharField(max_length = 18)
    state = models.CharField(max_length = 18)
    mobile = models.CharField(max_length = 18)

class notesModel(models.Model):
    ctrated = models.DateTimeField(auto_now_add = True)

    title = models.CharField(max_length = 18)
    cate = models.CharField(max_length = 18)
    myfile = models.FileField(upload_to='Notes_errors')
    desc = models.TextField()

class feedbackModel(models.Model):
    ctrated = models.DateTimeField(auto_now_add = True)

    name = models.CharField(max_length = 51)
    email = models.EmailField()
    subject = models.CharField(max_length = 108)
    msg = models.TextField()
