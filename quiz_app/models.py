from django.db import models


class Quiz(models.Model):
    title = models.CharField(max_length=250)


class Question(models.Model):
    text = models.TextField()

    quiz = models.ForeignKey(
        Quiz,
        related_name='questions',
        on_delete=models.CASCADE
    )


class Choice(models.Model):
    text = models.TextField()
    is_correct = models.BooleanField()

    question = models.ForeignKey(
        Question,
        related_name='choices',
        on_delete=models.CASCADE
    )
