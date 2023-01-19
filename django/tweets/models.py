from django.db import models



class Tweet(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f'Tweet - {self.id}'