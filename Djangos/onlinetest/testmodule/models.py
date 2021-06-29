from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

import uuid
import datetime

 
# Create your models here.


IDENTIFICATION=(("STU","Student"),
                ("STA","Staff"),
                ("TEA","Teacher"))

class Profile(AbstractUser):
 
    identification = models.CharField(verbose_name='Identification',max_length=20,choices=IDENTIFICATION,default=None,null=True,blank=True)
 