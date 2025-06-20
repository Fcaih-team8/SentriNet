from django.db import models

class QuestionAnswer(models.Model):
    question = models.TextField(unique=True)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

