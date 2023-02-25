<<<<<<< HEAD
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
=======
# from django.db import models

# Create your models here.
<<<<<<< Updated upstream
>>>>>>> 0b691d5363afa313b4a49b63f8f5bd38e1838c7b
=======
>>>>>>> 6057bc7c6736643eccf0c8100cf7d040fbc5ba66
>>>>>>> Stashed changes
