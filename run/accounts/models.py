from django.contrib.auth.hashers import make_password
from django.db import models


# Create your models here.
class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=120)
    username = models.CharField(max_length=10)
    user_skill = models.IntegerField(default=0)

    @classmethod
    def create_user(cls, email, password, username, location):
        user = cls(email=email, password=make_password(password), username=username, user_skill=0)
        user.save()
        return user