from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from datetime import date

class CustomUser(AbstractUser):
  username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
  email = models.EmailField(_('email address'), unique = True)
  uuid_field = models.UUIDField(null=False,primary_key=True)
  phone_no = models.CharField(max_length = 10,db_index=True)
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['phone_no','username']
  def __str__(self):
      return "{}".format(self.email)
  class Meta: 
    db_table = 'custom_user_table'