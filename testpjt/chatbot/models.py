from django.db import models

# Create your models here.

class Qna(models.Model):
    question = models.CharField(max_length=50)
