from django.db import models
from django.contrib.auth.models import (
BaseUserManager, AbstractBaseUser
)
 
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
        email=self.normalize_email(email),
        **extra_fields

        )

        user.set_password(password)
        user.save()
        return user


    def create_superuser(self, email, password, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser has to be a staff')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser has to be a is_superuser True')    

        user = self.create_user(
        email=email,
        password=password,
        **extra_fields,
        )
        # user.staff = True
        # user.admin = True
        user.save()
        return user
class User(AbstractBaseUser):
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField()(max_length=255,unique=True)
    is_company = models.BooleanField(default=False)
    is_advocate = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.email}'
