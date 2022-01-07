from django.contrib.auth import get_user_model
from django.db import models

from user.base import BaseModel

User = get_user_model()

class CallToExam(BaseModel):
    pupil = models.CharField(max_length=255)
    phone = models.CharField(max_length=9)
    coming_date = models.DateTimeField()
    is_send = models.BooleanField(default=False)
