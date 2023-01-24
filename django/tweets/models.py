from django.db import models
from django.contrib.auth.models import User


class Tweet(models.Model):
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f'Tweet - {self.id} Author -  {self.author}'