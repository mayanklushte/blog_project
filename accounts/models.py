from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager

class User(AbstractUser):
    username = None
    email = models.EmailField(_('Email Address'), unique=True)
    mobile_no = models.CharField(max_length=10)
    address = models.CharField(max_length=60)
    City = models.CharField(max_length=20)
    State = models.CharField(max_length=20)
    Country = models.CharField(max_length=20)
    PinCode = models.CharField(max_length=6)
    Profile_Image = models.ImageField(upload_to='profile_images')
    is_bloger = models.BooleanField(default=False)
    is_reader = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


