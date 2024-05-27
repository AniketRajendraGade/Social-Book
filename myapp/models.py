from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from datetime import date
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractBaseUser, PermissionsMixin):
    gender_choice = [
      ("Male", "Male"),
      ("Female", "Female"),
      ("Other","Other")
    ]
    
    email = models.EmailField(_("email address"), unique=True)
    user_name = models.CharField(max_length=255, blank=True)
    full_name = models.CharField(max_length=255, blank=True)
    gender = models.CharField(choices=gender_choice, max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    public_visibility = models.BooleanField(default=True)
    birth_year = models.PositiveIntegerField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    
    def save(self, *args, **kwargs):
        if self.birth_year:
            today = date.today()
            self.age = today.year - self.birth_year
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email
    
#upload books model
class Books(models.Model):
  user_id = models.IntegerField(null=True)
  title = models.CharField(max_length=255)
  image = models.ImageField(upload_to='cover_page/', null=True, default=None)
  description = models.CharField(max_length=500)
  visibility = models.BooleanField(default=True)
  cost = models.IntegerField()
  year_publish = models.IntegerField()
  file = models.FileField(upload_to='books/', null=True, default=None)





class BulkData(models.Model):
    Mobile = models.CharField(max_length=200)  
    Pincode = models.CharField(max_length=200)
    Name = models.CharField(max_length=200)
    Address = models.CharField(max_length=500)
    WhatsApp_Status = models.CharField(max_length=200)
    Blaster_Status = models.CharField(max_length=200)