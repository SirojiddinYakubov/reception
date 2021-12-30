from django.db import models

# Create your models here.
from user.base import BaseModel


class Vacancy(BaseModel):
    title = models.CharField(max_length=150)
    desc = models.TextField()
    form = models.TextField()