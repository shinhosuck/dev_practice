from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone



class Tweet(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    img = models.ImageField(default='/tweet-images', null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_edited = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f'Title:{self.title} ID:{self.id}'
