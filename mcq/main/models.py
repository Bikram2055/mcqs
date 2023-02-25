from django.db import models


# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=500)
    sub_topic = models.CharField(max_length=30)
    topic = models.CharField(max_length=30)
    field = models.CharField(max_length=30)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    ans1 = models.CharField(max_length=30)
    ans2 = models.CharField(max_length=30)
    ans3 = models.CharField(max_length=30)
    ans4 = models.CharField(max_length=30)
    reason = models.CharField(max_length=500)
