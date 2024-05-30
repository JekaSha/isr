from django.db import models

from django.utils import timezone
from django.conf import settings





# Create your models here.

class Task(models.Model):
    caption = models.CharField(max_length=100)
    body = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.caption



class Token(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    token = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.token
