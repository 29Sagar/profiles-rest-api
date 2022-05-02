from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager

# Create your models here.

class UserProfileManager(BaseUserManager):
    def create_user(self,email,name,password = None):
        if not email:
            return ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.moadal(email = email,name= name)

        user.setpassword(password)
        user.save()

        return user


    def create_superuser(self,email,name,password):
        user = self.create_user(email,name,password)

        user.is_superuser = True
        user.is_staff = True
        user.save() 

        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False )

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'


    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email