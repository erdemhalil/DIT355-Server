from django.db import models

from dentists.models import Dentist
from users.models import User

# Create your models here.

class Appointment(models.Model):
    date = models.DateTimeField(unique=True)
    completed = models.BooleanField(default=False)
    description = models.CharField(max_length=300)
    dentist = models.ForeignKey(Dentist, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
