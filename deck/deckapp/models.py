
from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from datetime import datetime


# Create your models here.

class User(AbstractUser):
    pass


class Deck(models.Model):
    users = models.ManyToManyField(User, related_name='group_users',blank=True)
    group_admin = models.ForeignKey(User,on_delete=models.CASCADE, related_name='group_admin')
    users_limit = models.IntegerField(default=0)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=550)
    group_profile = models.ImageField(upload_to='uploads/', default='uploads/groupofpeople.png')
    created_at = models.DateTimeField(default=datetime.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class SecurityKeys(models.Model):
    deck = models.ForeignKey(Deck,on_delete=models.CASCADE, related_name="deck")
    keys = models.CharField(max_length=500)

class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user_msg')
    deck = models.ForeignKey(Deck,on_delete=models.CASCADE, related_name="deck_msg")
