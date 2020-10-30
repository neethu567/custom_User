from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
import datetime
# Create your models here.
class User(AbstractBaseUser,PermissionsMixin):
    username=models.CharField(max_length=22,unique=True,db_index=True)
    email=models.EmailField(max_length=300,unique=True,db_index=True)
    is_verified=models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS =['username']

    objects=BaseUserManager()

    def __str__(self):
        return self.email
    def tokens(selfs):
        return ''



class UserManager(BaseUserManager):
    # use_in_migrations=True
    def create_user(self,email,username,date_of_birth,password=None):
        if username is None:
            raise TypeError('User should have a username')
        if email is None:
            raise TypeError('User  should have an email')
        user=self.model(username=username,email=self.normalize_email())
        user.set_password(password)
        user.save()


    def create_super_user(self,email,username,date_of_birth,password=None):
        if password is None:
            raise TypeError('password should not be none')

        user=self.create_user(username,email,password)
        user.is_superuser=True
        user.is_staff=True
        user.save()
        return user
